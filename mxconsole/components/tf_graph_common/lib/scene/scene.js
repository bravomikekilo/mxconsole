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
var tf;
(function (tf) {
    var graph;
    (function (graph) {
        var scene;
        (function (scene) {
            var svgNamespace = 'http://www.w3.org/2000/svg';
            /** Enums element class of objects in the scene */
            scene.Class = {
                Node: {
                    // <g> element that contains nodes.
                    CONTAINER: 'nodes',
                    // <g> element that contains detail about a node.
                    GROUP: 'node',
                    // <g> element that contains visual elements (like rect, ellipse).
                    SHAPE: 'nodeshape',
                    // <*> element(s) under SHAPE that should receive color updates.
                    COLOR_TARGET: 'nodecolortarget',
                    // <text> element showing the node's label.
                    LABEL: 'nodelabel',
                    // <g> element that contains all visuals for the expand/collapse
                    // button for expandable group nodes.
                    BUTTON_CONTAINER: 'buttoncontainer',
                    // <circle> element that surrounds expand/collapse buttons.
                    BUTTON_CIRCLE: 'buttoncircle',
                    // <path> element of the expand button.
                    EXPAND_BUTTON: 'expandbutton',
                    // <path> element of the collapse button.
                    COLLAPSE_BUTTON: 'collapsebutton'
                },
                Edge: {
                    CONTAINER: 'edges',
                    GROUP: 'edge',
                    LINE: 'edgeline',
                    REF_LINE: 'refline',
                    STRUCTURAL: 'structural'
                },
                Annotation: {
                    OUTBOX: 'out-annotations',
                    INBOX: 'in-annotations',
                    GROUP: 'annotation',
                    NODE: 'annotation-node',
                    EDGE: 'annotation-edge',
                    CONTROL_EDGE: 'annotation-control-edge',
                    LABEL: 'annotation-label',
                    ELLIPSIS: 'annotation-ellipsis'
                },
                Scene: {
                    GROUP: 'scene',
                    CORE: 'core',
                    INEXTRACT: 'in-extract',
                    OUTEXTRACT: 'out-extract'
                },
                Subscene: { GROUP: 'subscene' },
                OPNODE: 'op',
                METANODE: 'meta',
                SERIESNODE: 'series',
                BRIDGENODE: 'bridge',
                ELLIPSISNODE: 'ellipsis'
            };
            ;
            ;
            scene.healthPillEntries = [
                {
                    background_color: '#CC2F2C',
                    label: 'NaN',
                },
                {
                    background_color: '#FF8D00',
                    label: '- ∞',
                },
                {
                    background_color: '#EAEAEA',
                    label: '-',
                },
                {
                    background_color: '#A5A5A5',
                    label: '0',
                },
                {
                    background_color: '#262626',
                    label: '+',
                },
                {
                    background_color: '#003ED4',
                    label: '+ ∞',
                },
            ];
            /**
             * Helper method for fitting the graph in the svg view.
             *
             * @param svg The main svg.
             * @param zoomG The svg group used for panning and zooming.
             * @param d3zoom The zoom behavior.
             * @param callback Called when the fitting is done.
             */
            function fit(svg, zoomG, d3zoom, callback) {
                var svgRect = svg.getBoundingClientRect();
                var sceneSize = null;
                try {
                    sceneSize = zoomG.getBBox();
                    if (sceneSize.width === 0) {
                        // There is no scene anymore. We have been detached from the dom.
                        return;
                    }
                }
                catch (e) {
                    // Firefox produced NS_ERROR_FAILURE if we have been
                    // detached from the dom.
                    return;
                }
                var scale = 0.9 *
                    Math.min(svgRect.width / sceneSize.width, svgRect.height / sceneSize.height, 2);
                var params = graph.layout.PARAMS.graph;
                var zoomEvent = d3zoom.scale(scale)
                    .on('zoomend.fitted', function () {
                    // Remove the listener for the zoomend event,
                    // so we don't get called at the end of regular zoom events,
                    // just those that fit the graph to screen.
                    d3zoom.on('zoomend.fitted', null);
                    callback();
                })
                    .translate([params.padding.paddingLeft, params.padding.paddingTop])
                    .event;
                d3.select(zoomG).transition().duration(500).call(zoomEvent);
            }
            scene.fit = fit;
            ;
            /**
             * Helper method for panning the graph to center on the provided node,
             * if the node is currently off-screen.
             *
             * @param nodeName The node to center the graph on
             * @param svg The root SVG element for the graph
             * @param zoomG The svg group used for panning and zooming.
             * @param d3zoom The zoom behavior.
             * @return True if the graph had to be panned to display the
             *            provided node.
             */
            function panToNode(nodeName, svg, zoomG, d3zoom) {
                var node = d3
                    .select('[data-name="' + nodeName + '"].' + scene.Class.Node.GROUP)
                    .node();
                if (!node) {
                    return false;
                }
                var translate = d3zoom.translate();
                // Check if the selected node is off-screen in either
                // X or Y dimension in either direction.
                var nodeBox = node.getBBox();
                var nodeCtm = node.getScreenCTM();
                var pointTL = svg.createSVGPoint();
                var pointBR = svg.createSVGPoint();
                pointTL.x = nodeBox.x;
                pointTL.y = nodeBox.y;
                pointBR.x = nodeBox.x + nodeBox.width;
                pointBR.y = nodeBox.y + nodeBox.height;
                pointTL = pointTL.matrixTransform(nodeCtm);
                pointBR = pointBR.matrixTransform(nodeCtm);
                var isOutsideOfBounds = function (start, end, bound) {
                    return end < 0 || start > bound;
                };
                var svgRect = svg.getBoundingClientRect();
                if (isOutsideOfBounds(pointTL.x, pointBR.x, svgRect.width) ||
                    isOutsideOfBounds(pointTL.y, pointBR.y, svgRect.height)) {
                    // Determine the amount to transform the graph in both X and Y
                    // dimensions in order to center the selected node. This takes into
                    // acount the position of the node, the size of the svg scene, the
                    // amount the scene has been scaled by through zooming, and any previous
                    // transform already performed by this logic.
                    var centerX = (pointTL.x + pointBR.x) / 2;
                    var centerY = (pointTL.y + pointBR.y) / 2;
                    var dx = ((svgRect.width / 2) - centerX);
                    var dy = ((svgRect.height / 2) - centerY);
                    var zoomEvent = d3zoom.translate([translate[0] + dx, translate[1] + dy])
                        .event;
                    d3.select(zoomG).transition().duration(500).call(zoomEvent);
                    return true;
                }
                return false;
            }
            scene.panToNode = panToNode;
            ;
            /**
             * Given a container d3 selection, select a child svg element of a given tag
             * and class if exists or append / insert one otherwise.  If multiple children
             * matches the tag and class name, returns only the first one.
             *
             * @param container
             * @param tagName tag name.
             * @param className (optional) Class name or a list of class names.
             * @param before (optional) reference DOM node for insertion.
             * @return selection of the element
             */
            function selectOrCreateChild(container, tagName, className, before) {
                var child = selectChild(container, tagName, className);
                if (!child.empty()) {
                    return child;
                }
                var newElement = document.createElementNS('http://www.w3.org/2000/svg', tagName);
                if (className instanceof Array) {
                    for (var i = 0; i < className.length; i++) {
                        newElement.classList.add(className[i]);
                    }
                }
                else {
                    newElement.classList.add(className);
                }
                if (before) {
                    container.node().insertBefore(newElement, before);
                }
                else {
                    container.node().appendChild(newElement);
                }
                return d3.select(newElement)
                    .datum(container.datum());
            }
            scene.selectOrCreateChild = selectOrCreateChild;
            ;
            /**
             * Given a container d3 selection, select a child element of a given tag and
             * class. If multiple children matches the tag and class name, returns only
             * the first one.
             *
             * @param container
             * @param tagName tag name.
             * @param className (optional) Class name or list of class names.
             * @return selection of the element, or an empty selection
             */
            function selectChild(container, tagName, className) {
                var children = container.node().childNodes;
                for (var i = 0; i < children.length; i++) {
                    var child = children[i];
                    if (child.tagName === tagName) {
                        if (className instanceof Array) {
                            var hasAllClasses = true;
                            for (var j = 0; j < className.length; j++) {
                                hasAllClasses =
                                    hasAllClasses && child.classList.contains(className[j]);
                            }
                            if (hasAllClasses) {
                                return d3.select(child);
                            }
                        }
                        else if ((!className || child.classList.contains(className))) {
                            return d3.select(child);
                        }
                    }
                }
                return d3.select(null);
            }
            scene.selectChild = selectChild;
            ;
            /**
             * Select or create a sceneGroup and build/update its nodes and edges.
             *
             * Structure Pattern:
             *
             * <g class='scene'>
             *   <g class='core'>
             *     <g class='edges'>
             *       ... stuff from tf.graph.scene.edges.build ...
             *     </g>
             *     <g class='nodes'>
             *       ... stuff from tf.graph.scene.nodes.build ...
             *     </g>
             *   </g>
             *   <g class='in-extract'>
             *     <g class='nodes'>
             *       ... stuff from tf.graph.scene.nodes.build ...
             *     </g>
             *   </g>
             *   <g class='out-extract'>
             *     <g class='nodes'>
             *       ... stuff from tf.graph.scene.nodes.build ...
             *     </g>
             *   </g>
             * </g>
             *
             * @param container D3 selection of the parent.
             * @param renderNode render node of a metanode or series node.
             * @param sceneElement <tf-graph-scene> polymer element.
             * @param sceneClass class attribute of the scene (default='scene').
             */
            function buildGroup(container, renderNode, sceneElement, sceneClass) {
                sceneClass = sceneClass || scene.Class.Scene.GROUP;
                var isNewSceneGroup = selectChild(container, 'g', sceneClass).empty();
                var sceneGroup = selectOrCreateChild(container, 'g', sceneClass);
                // core
                var coreGroup = selectOrCreateChild(sceneGroup, 'g', scene.Class.Scene.CORE);
                var coreNodes = _.reduce(renderNode.coreGraph.nodes(), function (nodes, name) {
                    var node = renderNode.coreGraph.node(name);
                    if (!node.excluded) {
                        nodes.push(node);
                    }
                    return nodes;
                }, []);
                if (renderNode.node.type === graph.NodeType.SERIES) {
                    // For series, we want the first item on top, so reverse the array so
                    // the first item in the series becomes last item in the top, and thus
                    // is rendered on the top.
                    coreNodes.reverse();
                }
                // Create the layer of edges for this scene (paths).
                scene.edge.buildGroup(coreGroup, renderNode.coreGraph, sceneElement);
                // Create the layer of nodes for this scene (ellipses, rects etc).
                scene.node.buildGroup(coreGroup, coreNodes, sceneElement);
                // In-extract
                if (renderNode.isolatedInExtract.length > 0) {
                    var inExtractGroup = selectOrCreateChild(sceneGroup, 'g', scene.Class.Scene.INEXTRACT);
                    scene.node.buildGroup(inExtractGroup, renderNode.isolatedInExtract, sceneElement);
                }
                else {
                    selectChild(sceneGroup, 'g', scene.Class.Scene.INEXTRACT).remove();
                }
                // Out-extract
                if (renderNode.isolatedOutExtract.length > 0) {
                    var outExtractGroup = selectOrCreateChild(sceneGroup, 'g', scene.Class.Scene.OUTEXTRACT);
                    scene.node.buildGroup(outExtractGroup, renderNode.isolatedOutExtract, sceneElement);
                }
                else {
                    selectChild(sceneGroup, 'g', scene.Class.Scene.OUTEXTRACT).remove();
                }
                position(sceneGroup, renderNode);
                // Fade in the scene group if it didn't already exist.
                if (isNewSceneGroup) {
                    sceneGroup.attr('opacity', 0).transition().attr('opacity', 1);
                }
                return sceneGroup;
            }
            scene.buildGroup = buildGroup;
            ;
            /**
             * Given a scene's svg group, set  g.in-extract, g.coreGraph, g.out-extract svg
             * groups' position relative to the scene.
             *
             * @param sceneGroup
             * @param renderNode render node of a metanode or series node.
             */
            function position(sceneGroup, renderNode) {
                // Translate scenes down by the label height so that when showing graphs in
                // expanded metanodes, the graphs are below the labels.  Do not shift them
                // down for series nodes as series nodes don't have labels inside of their
                // bounding boxes.
                var yTranslate = renderNode.node.type === graph.NodeType.SERIES ?
                    0 : graph.layout.PARAMS.subscene.meta.labelHeight;
                // core
                translate(selectChild(sceneGroup, 'g', scene.Class.Scene.CORE), 0, yTranslate);
                // in-extract
                var hasInExtract = renderNode.isolatedInExtract.length > 0;
                var hasOutExtract = renderNode.isolatedOutExtract.length > 0;
                if (hasInExtract) {
                    var offset = graph.layout.PARAMS.subscene.meta.extractXOffset;
                    var inExtractX = renderNode.coreBox.width -
                        renderNode.inExtractBox.width / 2 - renderNode.outExtractBox.width -
                        (hasOutExtract ? offset : 0);
                    translate(selectChild(sceneGroup, 'g', scene.Class.Scene.INEXTRACT), inExtractX, yTranslate);
                }
                // out-extract
                if (hasOutExtract) {
                    var outExtractX = renderNode.coreBox.width -
                        renderNode.outExtractBox.width / 2;
                    translate(selectChild(sceneGroup, 'g', scene.Class.Scene.OUTEXTRACT), outExtractX, yTranslate);
                }
            }
            ;
            /** Adds a click listener to a group that fires a graph-select event */
            function addGraphClickListener(graphGroup, sceneElement) {
                d3.select(graphGroup).on('click', function () {
                    sceneElement.fire('graph-select');
                });
            }
            scene.addGraphClickListener = addGraphClickListener;
            ;
            /** Helper for adding transform: translate(x0, y0) */
            function translate(selection, x0, y0) {
                // If it is already placed on the screen, make it a transition.
                if (selection.attr('transform') != null) {
                    selection = selection.transition('position');
                }
                selection.attr('transform', 'translate(' + x0 + ',' + y0 + ')');
            }
            scene.translate = translate;
            ;
            /**
             * Helper for setting position of a svg rect
             * @param rect rect to set position of.
             * @param cx Center x.
             * @param cy Center x.
             * @param width Width to set.
             * @param height Height to set.
             */
            function positionRect(rect, cx, cy, width, height) {
                rect.transition().attr({
                    x: cx - width / 2,
                    y: cy - height / 2,
                    width: width,
                    height: height
                });
            }
            scene.positionRect = positionRect;
            ;
            /**
             * Helper for setting position of a svg expand/collapse button
             * @param button container group
             * @param renderNode the render node of the group node to position
             *        the button on.
             */
            function positionButton(button, renderNode) {
                var cx = graph.layout.computeCXPositionOfNodeShape(renderNode);
                // Position the button in the top-right corner of the group node,
                // with space given the draw the button inside of the corner.
                var width = renderNode.expanded ?
                    renderNode.width : renderNode.coreBox.width;
                var height = renderNode.expanded ?
                    renderNode.height : renderNode.coreBox.height;
                var x = cx + width / 2 - 6;
                var y = renderNode.y - height / 2 + 6;
                // For unexpanded series nodes, the button has special placement due
                // to the unique visuals of this group node.
                if (renderNode.node.type === graph.NodeType.SERIES && !renderNode.expanded) {
                    x += 10;
                    y -= 2;
                }
                var translateStr = 'translate(' + x + ',' + y + ')';
                button.selectAll('path').transition().attr('transform', translateStr);
                button.select('circle').transition().attr({ cx: x, cy: y, r: graph.layout.PARAMS.nodeSize.meta.expandButtonRadius });
            }
            scene.positionButton = positionButton;
            ;
            /**
             * Helper for setting position of a svg ellipse
             * @param ellipse ellipse to set position of.
             * @param cx Center x.
             * @param cy Center x.
             * @param width Width to set.
             * @param height Height to set.
             */
            function positionEllipse(ellipse, cx, cy, width, height) {
                ellipse.transition().attr({
                    cx: cx,
                    cy: cy,
                    rx: width / 2,
                    ry: height / 2
                });
            }
            scene.positionEllipse = positionEllipse;
            ;
            /**
             * @param {number} stat A stat for a health pill (such as mean or variance).
             * @param {boolean} shouldRoundOnesDigit Whether to round this number to the
             *     ones digit. Useful for say int, uint, and bool output types.
             * @return {string} A human-friendly string representation of that stat.
             */
            function humanizeHealthPillStat(stat, shouldRoundOnesDigit) {
                if (shouldRoundOnesDigit) {
                    return stat.toFixed(0);
                }
                if (Math.abs(stat) >= 1) {
                    return stat.toFixed(1);
                }
                return stat.toExponential(1);
            }
            scene.humanizeHealthPillStat = humanizeHealthPillStat;
            /**
             * Renders a health pill for an op atop a node.
             */
            function _addHealthPill(nodeGroupElement, healthPill, nodeInfo) {
                // Check if text already exists at location.
                d3.select(nodeGroupElement.parentNode).selectAll('.health-pill').remove();
                if (!nodeInfo || !healthPill) {
                    return;
                }
                var lastHealthPillData = healthPill.value;
                // For now, we only visualize the 6 values that summarize counts of tensor
                // elements of various categories: -Inf, negative, 0, positive, Inf, and NaN.
                var lastHealthPillOverview = lastHealthPillData.slice(2, 8);
                var totalCount = lastHealthPillData[1];
                var healthPillWidth = 60;
                var healthPillHeight = 10;
                if (nodeInfo.node.type === tf.graph.NodeType.OP) {
                    // Use a smaller health pill for op nodes (rendered as smaller ellipses).
                    healthPillWidth /= 2;
                    healthPillHeight /= 2;
                }
                var healthPillGroup = document.createElementNS(svgNamespace, 'g');
                healthPillGroup.classList.add('health-pill');
                // Define the gradient for the health pill.
                var healthPillDefs = document.createElementNS(svgNamespace, 'defs');
                healthPillGroup.appendChild(healthPillDefs);
                var healthPillGradient = document.createElementNS(svgNamespace, 'linearGradient');
                var healthPillGradientId = 'health-pill-gradient';
                healthPillGradient.setAttribute('id', healthPillGradientId);
                var titleOnHoverTextEntries = [];
                var cumulativeCount = 0;
                var previousOffset = '0%';
                for (var i = 0; i < lastHealthPillOverview.length; i++) {
                    if (!lastHealthPillOverview[i]) {
                        // Exclude empty categories.
                        continue;
                    }
                    cumulativeCount += lastHealthPillOverview[i];
                    // Create a color interval using 2 stop elements.
                    var stopElement0 = document.createElementNS(svgNamespace, 'stop');
                    stopElement0.setAttribute('offset', previousOffset);
                    stopElement0.setAttribute('stop-color', scene.healthPillEntries[i].background_color);
                    healthPillGradient.appendChild(stopElement0);
                    var stopElement1 = document.createElementNS(svgNamespace, 'stop');
                    var percent = (cumulativeCount * 100 / totalCount) + '%';
                    stopElement1.setAttribute('offset', percent);
                    stopElement1.setAttribute('stop-color', scene.healthPillEntries[i].background_color);
                    healthPillGradient.appendChild(stopElement1);
                    previousOffset = percent;
                    // Include this number in the title that appears on hover.
                    titleOnHoverTextEntries.push(scene.healthPillEntries[i].label + ': ' + lastHealthPillOverview[i]);
                }
                healthPillDefs.appendChild(healthPillGradient);
                // Create the rectangle for the health pill.
                var rect = document.createElementNS(svgNamespace, 'rect');
                rect.setAttribute('fill', 'url(#' + healthPillGradientId + ')');
                rect.setAttribute('width', String(healthPillWidth));
                rect.setAttribute('height', String(healthPillHeight));
                healthPillGroup.appendChild(rect);
                // Show a title with specific counts on hover.
                var titleSvg = document.createElementNS(svgNamespace, 'title');
                titleSvg.textContent = titleOnHoverTextEntries.join(', ');
                healthPillGroup.appendChild(titleSvg);
                // Center this health pill just right above the node for the op.
                var healthPillX = nodeInfo.x - healthPillWidth / 2;
                var healthPillY = nodeInfo.y - healthPillHeight - nodeInfo.height / 2 - 2;
                if (nodeInfo.labelOffset < 0) {
                    // The label is positioned above the node. Do not occlude the label.
                    healthPillY += nodeInfo.labelOffset;
                }
                if (lastHealthPillOverview[2] || lastHealthPillOverview[3] ||
                    lastHealthPillOverview[4]) {
                    // At least 1 "non-Inf and non-NaN" value exists (a -, 0, or + value). Show
                    // stats on tensor values.
                    // Determine if we should display the output range as integers.
                    var shouldRoundOnesDigit = false;
                    var node_1 = nodeInfo.node;
                    var attributes = node_1.attr;
                    if (attributes && attributes.length) {
                        // Find the attribute for output type if there is one.
                        for (var i = 0; i < attributes.length; i++) {
                            if (attributes[i].key === 'T') {
                                // Note whether the output type is an integer.
                                var outputType = attributes[i].value['type'];
                                shouldRoundOnesDigit =
                                    outputType && /^DT_(BOOL|INT|UINT)/.test(outputType);
                                break;
                            }
                        }
                    }
                    var statsSvg = document.createElementNS(svgNamespace, 'text');
                    var minString = humanizeHealthPillStat(lastHealthPillData[8], shouldRoundOnesDigit);
                    var maxString = humanizeHealthPillStat(lastHealthPillData[9], shouldRoundOnesDigit);
                    statsSvg.textContent = minString + ' ~ ' + maxString;
                    statsSvg.classList.add('health-pill-stats');
                    statsSvg.setAttribute('x', String(healthPillWidth / 2));
                    statsSvg.setAttribute('y', '-2');
                    healthPillGroup.appendChild(statsSvg);
                }
                healthPillGroup.setAttribute('transform', 'translate(' + healthPillX + ', ' + healthPillY + ')');
                Polymer.dom(nodeGroupElement.parentNode).appendChild(healthPillGroup);
            }
            /**
             * Adds health pills (which visualize tensor summaries) to a graph group.
             * @param svgRoot The root SVG element of the graph to add heath pills to.
             * @param nodeNamesToHealthPills An object mapping node name to health pill.
             * @param colors A list of colors to use.
             */
            function addHealthPills(svgRoot, nodeNamesToHealthPills, healthPillStepIndex) {
                if (!nodeNamesToHealthPills) {
                    // No health pill information available.
                    return;
                }
                var svgRootSelection = d3.select(svgRoot);
                svgRootSelection.selectAll('g.nodeshape')
                    .each(function (nodeInfo) {
                    // Only show health pill data for this node if it is available.
                    var healthPills = nodeNamesToHealthPills[nodeInfo.node.name];
                    var healthPill = healthPills ? healthPills[healthPillStepIndex] : null;
                    _addHealthPill(this, healthPill, nodeInfo);
                });
            }
            scene.addHealthPills = addHealthPills;
            ;
        })(scene = graph.scene || (graph.scene = {}));
    })(graph = tf.graph || (tf.graph = {}));
})(tf || (tf = {})); // close module
