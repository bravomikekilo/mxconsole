/* Copyright 2015 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var Plottable;
(function (Plottable) {
    var DragZoomLayer = (function (_super) {
        __extends(DragZoomLayer, _super);
        /**
         * Constructs a SelectionBoxLayer with an attached DragInteraction and
         * ClickInteraction. On drag, it triggers an animated zoom into the box
         * that was dragged. On double click, it zooms back out to the original
         * view, before any zooming.
         * The zoom animation uses an easing function (default
         * d3.ease('cubic-in-out')) and is customizable.
         * Usage: Construct the selection box layer and attach x and y scales,
         * and then add the layer over the plot you are zooming on using a
         * Component Group.
         * TODO(danmane) - merge this into Plottable
         */
        function DragZoomLayer(xScale, yScale) {
            var _this = _super.call(this) || this;
            _this.isZoomed = false;
            _this.easeFn = d3.ease('cubic-in-out');
            _this._animationTime = 750;
            _this.xScale(xScale);
            _this.yScale(yScale);
            _this._dragInteraction = new Plottable.Interactions.Drag();
            _this._dragInteraction.attachTo(_this);
            _this._doubleClickInteraction = new Plottable.Interactions.DoubleClick();
            _this._doubleClickInteraction.attachTo(_this);
            _this.setupCallbacks();
            return _this;
        }
        /**
         * Register a method that calls when the DragZoom interaction starts.
         */
        DragZoomLayer.prototype.interactionStart = function (cb) { this.onStart = cb; };
        /**
         * Register a method that calls when the DragZoom interaction ends.
         */
        DragZoomLayer.prototype.interactionEnd = function (cb) { this.onEnd = cb; };
        DragZoomLayer.prototype.setupCallbacks = function () {
            var _this = this;
            var dragging = false;
            this._dragInteraction.onDragStart(function (startPoint) {
                _this.bounds({
                    topLeft: startPoint,
                    bottomRight: startPoint,
                });
                _this.onStart();
            });
            this._dragInteraction.onDrag(function (startPoint, endPoint) {
                _this.bounds({ topLeft: startPoint, bottomRight: endPoint });
                _this.boxVisible(true);
                dragging = true;
            });
            this._dragInteraction.onDragEnd(function (startPoint, endPoint) {
                _this.boxVisible(false);
                _this.bounds({ topLeft: startPoint, bottomRight: endPoint });
                if (dragging) {
                    _this.zoom();
                }
                else {
                    _this.onEnd();
                }
                dragging = false;
            });
            this._doubleClickInteraction.onDoubleClick(this.unzoom.bind(this));
        };
        DragZoomLayer.prototype.animationTime = function (animationTime) {
            if (animationTime == null) {
                return this._animationTime;
            }
            if (animationTime < 0) {
                throw new Error('animationTime cannot be negative');
            }
            this._animationTime = animationTime;
            return this;
        };
        /**
         * Set the easing function, which determines how the zoom interpolates
         * over time.
         */
        DragZoomLayer.prototype.ease = function (fn) {
            if (typeof (fn) !== 'function') {
                throw new Error('ease function must be a function');
            }
            if (fn(0) !== 0 || fn(1) !== 1) {
                Plottable.Utils.Window.warn('Easing function does not maintain invariant ' +
                    'f(0)==0 && f(1)==1. Bad behavior may result.');
            }
            this.easeFn = fn;
            return this;
        };
        // Zoom into extent of the selection box bounds
        DragZoomLayer.prototype.zoom = function () {
            var x0 = this.xExtent()[0].valueOf();
            var x1 = this.xExtent()[1].valueOf();
            var y0 = this.yExtent()[1].valueOf();
            var y1 = this.yExtent()[0].valueOf();
            if (x0 === x1 || y0 === y1) {
                return;
            }
            if (!this.isZoomed) {
                this.isZoomed = true;
            }
            this.interpolateZoom(x0, x1, y0, y1);
        };
        // Restore the scales to their state before any zoom
        DragZoomLayer.prototype.unzoom = function () {
            if (!this.isZoomed) {
                return;
            }
            this.isZoomed = false;
            // Some Plottable magic follows which ensures that when we un-zoom, we
            // un-zoom to the current extent of the data; i.e. if new data was loaded
            // since we zoomed, we should un-zoom to the extent of the new data.
            // this basically replicates the autoDomain logic in Plottable.
            // it uses the internal methods to get the same boundaries that autoDomain
            // would, but allows us to interpolate the zoom with a nice animation.
            var xScale = this.xScale();
            var yScale = this.yScale();
            xScale._domainMin = null;
            xScale._domainMax = null;
            yScale._domainMin = null;
            yScale._domainMax = null;
            var xDomain = xScale._getExtent();
            var yDomain = yScale._getExtent();
            this.interpolateZoom(xDomain[0], xDomain[1], yDomain[0], yDomain[1]);
        };
        // If we are zooming, disable interactions, to avoid contention
        DragZoomLayer.prototype.isZooming = function (isZooming) {
            this._dragInteraction.enabled(!isZooming);
            this._doubleClickInteraction.enabled(!isZooming);
        };
        DragZoomLayer.prototype.interpolateZoom = function (x0f, x1f, y0f, y1f) {
            var _this = this;
            var x0s = this.xScale().domain()[0].valueOf();
            var x1s = this.xScale().domain()[1].valueOf();
            var y0s = this.yScale().domain()[0].valueOf();
            var y1s = this.yScale().domain()[1].valueOf();
            // Copy a ref to the ease fn, so that changing ease wont affect zooms in
            // progress.
            var ease = this.easeFn;
            var interpolator = function (a, b, p) {
                return d3.interpolateNumber(a, b)(ease(p));
            };
            this.isZooming(true);
            var start = Date.now();
            var draw = function () {
                var now = Date.now();
                var passed = now - start;
                var p = _this._animationTime === 0 ?
                    1 :
                    Math.min(1, passed / _this._animationTime);
                var x0 = interpolator(x0s, x0f, p);
                var x1 = interpolator(x1s, x1f, p);
                var y0 = interpolator(y0s, y0f, p);
                var y1 = interpolator(y1s, y1f, p);
                _this.xScale().domain([x0, x1]);
                _this.yScale().domain([y0, y1]);
                if (p < 1) {
                    Plottable.Utils.DOM.requestAnimationFramePolyfill(draw);
                }
                else {
                    _this.onEnd();
                    _this.isZooming(false);
                }
            };
            draw();
        };
        return DragZoomLayer;
    }(Plottable.Components.SelectionBoxLayer));
    Plottable.DragZoomLayer = DragZoomLayer;
})(Plottable || (Plottable = {}));
