"use strict";
/* Copyright 2016 The TensorFlow Authors. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the 'License');
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an 'AS IS' BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================*/
var svgNS = 'http://www.w3.org/2000/svg';
// The values below are the global defaults for labels, colors, etc. They
// have to be defined here, in order to be referenced as fallback values for
// the parameters of createChartGroup() and as initial values for the internal
// fields in the Polymer element.
var labels = ['-Inf', '-', '0', '+', '+Inf', 'NaN'];
var colors = ['#22b0dc', '#1c1c1c', '#808080 ', '#ddd', '#ffdb00', '#c00'];
var heightWidthRatio = 0.2;
var heightToFontRatio = 1 / 6;
function attachChartGroup(data, width, parentElement, _labels, _colors, _heightWidthRatio, _heightToFontRatio) {
    if (_labels === void 0) { _labels = labels; }
    if (_colors === void 0) { _colors = colors; }
    if (_heightWidthRatio === void 0) { _heightWidthRatio = heightWidthRatio; }
    if (_heightToFontRatio === void 0) { _heightToFontRatio = heightToFontRatio; }
    // Calculate the total of all entries in the data array.
    var dataSum = data.reduce(function (prevResult, currValue) {
        return prevResult + currValue;
    });
    var height = width * _heightWidthRatio;
    // Render data.
    var outerGroup = document.createElementNS(svgNS, 'g');
    Polymer.dom(parentElement).appendChild(outerGroup);
    var currentOffset = 0;
    var currentDataLength = data.length;
    for (var slice = 0; slice < currentDataLength; slice++) {
        var sliceGroup = document.createElementNS(svgNS, 'g');
        Polymer.dom(outerGroup).appendChild(sliceGroup);
        var percentage = data[slice] / dataSum;
        var sliceWidth = percentage * width;
        // Create rectangle.
        var rect = createRect(currentOffset, sliceWidth, height, _colors[slice]);
        // Add to new rectangle to SVG.
        Polymer.dom(sliceGroup).appendChild(rect);
        // Add text to rectangle.
        var text = createText(currentOffset, sliceWidth, height, _labels[slice], _colors[slice], sliceGroup, _heightToFontRatio);
        // Add tooltip to rectangle and text.
        var rectTitle = createTitle(_labels[slice], data[slice]);
        var textTitle = createTitle(_labels[slice], data[slice]);
        Polymer.dom(rect).appendChild(rectTitle);
        Polymer.dom(text).appendChild(textTitle);
        currentOffset += sliceWidth;
    }
    return outerGroup;
}
exports.attachChartGroup = attachChartGroup;
function createText(currentOffset, sliceWidth, height, label, color, group, heightToFontRatio) {
    // Add text to rectangle.
    var text = document.createElementNS(svgNS, 'text');
    Polymer.dom(group).appendChild(text);
    text.innerHTML = label;
    // Set location.
    text.setAttribute('x', (currentOffset + sliceWidth / 2).toString());
    text.setAttribute('y', (height / 2).toString());
    // Set text properties.
    var textColor = getTextColor(color);
    text.setAttribute('fill', textColor);
    // Center text.
    text.setAttribute('text-anchor', 'middle');
    text.setAttribute('dominant-baseline', 'middle');
    // Font size.
    var fontSize = height * heightToFontRatio;
    text.setAttribute('font-size', fontSize.toString());
    var textWidth = text.getBoundingClientRect().width;
    var textHeight = text.getBoundingClientRect().height;
    // Hide text if text is wider than the slice.
    if (textWidth > sliceWidth || textHeight > height || fontSize < 7) {
        text.innerHTML = '';
    }
    return text;
}
function createTitle(label, numberOfEntries) {
    var title = document.createElementNS(svgNS, 'title');
    title.innerHTML = label + ': ' + numberOfEntries.toString();
    return title;
}
function createRect(currentOffset, sliceWidth, height, color) {
    // TODO(b/33428016): Remove this cast when TS 2.1 is in use, as it's
    // unnecessary.
    var rect = document.createElementNS(svgNS, 'rect');
    // Set location.
    rect.setAttribute('x', currentOffset.toString());
    rect.setAttribute('y', '0');
    // Set dimensions.
    rect.setAttribute('width', sliceWidth.toString());
    rect.setAttribute('height', height.toString());
    // Set colour.
    rect.setAttribute('fill', color);
    return rect;
}
function getTextColor(hexTripletColor) {
    var color = hexTripletColor;
    if (color.substring(0, 1) !== '#') {
        var convertedHex = colorToHex(color);
        if (convertedHex) {
            color = convertedHex;
        }
        else {
            // RGB string is currently not handled.
            /* tslint:disable:no-console */
            console.warn('WARNING: Could not convert color to hex,' +
                'please specify color as name or hex string.');
            return 'black';
        }
    }
    color = color.substring(1); // Remove #.
    if (color.length === 3) {
        color = color.split('').reduce(
        // Double every character.
        function (initial, current) {
            return initial + current + current;
        }, '' // Initial value.
        );
    }
    var colorInt = parseInt(color, 16); // Convert to integer.
    var r = (colorInt & 0xFF0000) >> 16; // Extract each color component.
    var g = (colorInt & 0x00FF00) >> 8;
    var b = colorInt & 0x0000FF;
    // Calculate human perceptible luminance.
    var alpha = 1 - (0.299 * r + 0.587 * g + 0.114 * b) / 255;
    if (alpha < 0.5) {
        return 'black';
    }
    else {
        return 'white';
    }
}
/**
 * Renders a pixel using the provided color string to an unattached canvas,
 * then reads and returns the rgb image data of the pixel.
 *
 * @param color The color string to be converted.
 *
 * @example
 * // Returns [0, 0, 255, 255]
 * colorToRGBA('blue')
 *
 * @returns Returns the rgba colors as an array, i.e.
 * [r, g, b, a]
 */
function colorToRgba(color) {
    var canvas = document.createElement('canvas');
    canvas.height = 1;
    canvas.width = 1;
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = color;
    ctx.fillRect(0, 0, 1, 1);
    var retArray = [];
    var imageData = ctx.getImageData(0, 0, 1, 1).data;
    imageData.forEach(function (d) {
        retArray.push(d);
    });
    return retArray;
}
/**
 * Turns a number (0-255) into a 2-character hex number (00-ff).
 * @param num
 *
 * @returns The converted string.
 */
function numToHex(num) {
    return ('0' + num.toString(16)).slice(-2);
}
/**
 * Converts any color string to its hex representation.
 * @param color The color string to be converted.
 *
 * @example
 * // Returns '#0000ff'
 * colorToHex('blue')
 *
 * @returns The hex color string.
 */
function colorToHex(color) {
    var rgba = colorToRgba(color);
    return '#' +
        rgba.slice(0, 3) // Remove alpha channel.
            .map(function (value) { return numToHex(value); })
            .join('');
}
Polymer({
    is: 'vz-data-summary',
    properties: {
        colors: {
            type: Array,
            // Has to match number of elements in the data array.
            observer: '_onColorsChange'
        },
        data: { type: Array, value: [], observer: '_onDataChange' },
        heightWidthRatio: { type: Number, value: heightWidthRatio, observer: '_onRatioChange' },
        heightToFontRatio: {
            type: Number,
            value: heightToFontRatio,
            observer: '_onFontRatioChange'
        },
        labels: { type: Array, observer: '_onLabelChange' },
        _colors: {
            type: Array,
            value: colors,
        },
        _data: Array,
        _labels: { type: Array, value: labels },
        _dataSum: { type: Number },
        _drawRequested: { type: Boolean, value: false },
        _height: { type: String },
        _isReady: { type: Boolean, value: false },
        _width: { type: Number }
    },
    behaviors: [Polymer.IronResizableBehavior],
    listeners: { 'iron-resize': '_onWidthChange' },
    ready: function () {
        this._isReady = true;
        this._updateDimensions();
        // Trigger rendering if draw was requested before element was ready.
        if (this._drawRequested) {
            this._renderData();
        }
    },
    attached: function () {
        if (this._isReady) {
            this._updateInternalVariables();
            this._renderData();
        }
    },
    /**
     * Observer for this.colors.
     * @private
     */
    _onColorsChange: function () {
        // Verify passed array is valid.
        if (this._isColorsValid()) {
            // Copy over the array to the internal field if it has the correct
            // length.
            this._updateInternalVariables();
            this._renderData();
        }
    },
    /**
     * Data change handler, if new data is valid, sets flag to indicate data
     * now valid, updates the data extent and renders the new data.
     */
    _onDataChange: function () {
        // Validate new data.
        if (!this._isDataValid(this.data)) {
            return;
        }
        this._updateInternalVariables(); // Update the internal variables.
        // Calculate the sum.
        this._dataSum =
            this.data.reduce(function (prevResult, currValue) {
                return prevResult + currValue;
            });
        this._renderData();
    },
    /**
     * Observer for this.labels. Validates that this.labels is an array of
     * 6 elements before copying its contents to an internal array.
     */
    _onLabelChange: function () {
        if (this._isLabelsValid()) {
            this._updateInternalVariables();
            this._renderData();
        }
    },
    _onFontRatioChange: function () {
        if ((typeof this.heightToFontRatio) === 'number') {
            this._renderData();
        }
    },
    /**
     * Observer for this.heightWidthRatio.
     */
    _onRatioChange: function () {
        if (this.heightWidthRatio) {
            this._renderData();
        }
    },
    /**
     * Observer for width change. Depends on iron-resizable-behavior.
     */
    _onWidthChange: function () {
        this._width = this.$.summary.parentNode.width;
        this._renderData();
    },
    _internalFieldsValid: function () {
        return !!(this._data && this._labels && this._colors);
    },
    /**
     * Renders data, if element is ready, the dimensions are set, and valid
     * data exists.
     * @private
     */
    _renderData: function () {
        if (!this._isReady || !this._internalFieldsValid()) {
            this._drawRequested = true;
            return;
        }
        // Ensure dimensions are up-to-date and valid before starting rendering.
        this._updateDimensions();
        if (!this._width || !this._height) {
            return;
        }
        // Find element to append heat map to and determine dimensions.
        var svgSelection = this.$.summary;
        // Clear the SVG.
        this.resetSVG();
        // Render data.
        attachChartGroup(this._data, this._width, svgSelection, this._labels, this._colors, this.heightWidthRatio, this.heightToFontRatio);
    },
    /**
     * Verifies whether input data is valid.
     * @param [internal] {bool} Whether to check the internal or external
     * field.
     * @private
     */
    _isDataValid: function (internal) {
        if (internal === void 0) { internal = false; }
        return this._validateArrayByName('data', internal, isNumeric);
    },
    _isColorsValid: function (internal) {
        if (internal === void 0) { internal = false; }
        return this._validateArrayByName('colors', internal, isString);
    },
    _isLabelsValid: function (internal) {
        if (internal === void 0) { internal = false; }
        return this._validateArrayByName('labels', internal, isString);
    },
    _validateArrayByName: function (name, internal, typeChecker) {
        if (internal) {
            name = '_' + name;
        }
        return _isValidArray(this[name], typeChecker);
    },
    _updateInternalVariables: function () {
        // If all new data is valid.
        var isDataValid = this._isDataValid();
        var isColorsValid = this._isColorsValid();
        var isLabelsValid = this._isLabelsValid();
        if (isDataValid && isColorsValid && isLabelsValid) {
            // Ensure they all have the same length.
            var length_1 = this.data.length;
            if (length_1 === this.labels.length && length_1 === this.colors.length) {
                this._data = this.data.slice();
                this._colors = this.colors.slice();
                this._labels = this.labels.slice();
            }
        }
        else {
            var internalDataValid = this._isDataValid(true);
            var internalColorsValid = this._isColorsValid(true);
            var internalLabelsValid = this._isLabelsValid(true);
            length = (internalDataValid && this._data.length) ||
                (internalColorsValid && this._colors.length) ||
                (internalLabelsValid && this._labels.length);
            this._updateIfSameLength(length, 'data');
            this._updateIfSameLength(length, 'colors');
            this._updateIfSameLength(length, 'labels');
        }
    },
    /**
     * Updates dimensions based on the width of the parent element.
     * @private
     */
    _updateDimensions: function () {
        var svgSelection = this.$.summary;
        // Recalculate height and width, and ensure data can be rendered.
        this._width = svgSelection.parentElement.clientWidth;
        this._height = this._width * this.heightWidthRatio;
        // Update the attribute height and width.
        svgSelection.setAttribute('height', this._height);
        svgSelection.setAttribute('width', this._width);
    },
    /**
     * Called when either colors, data, or labels are called. Copies calues
     * into internal fields iff the length of all three arrays is equal.
     */
    _updateIfSameLength: function (length, name) {
        if (this[name] && this[name].length === length) {
            this['_' + name] = this[name].slice();
        }
    },
    /**
     * Resets the SVG. Used by _renderData() but is exposed to provide the
     * user more control of the SVG's contents.
     */
    resetSVG: function () {
        // Reset the SVG.
        this.$.summary.innerHTML = '';
    }
});
function _isValidArray(newData, typeCheckingFunction) {
    return Array.isArray(newData) &&
        // Returns true is every element in the array is numeric.
        newData.every(typeCheckingFunction);
}
function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}
function isString(s) {
    return (typeof s) === 'string';
}
