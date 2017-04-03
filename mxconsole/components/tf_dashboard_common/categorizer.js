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
var Categorizer;
(function (Categorizer) {
    /**
     * This module contains methods that allow sorting tags into 'categories'.
     * A category contains a name and a list of tags.
     * The sorting strategy is defined by a 'CustomCategorization', which contains
     * 'categoryDefinitions' which are regex rules used to construct a category.
     * E.g. the regex rule 'xent' will create a category called 'xent' that
     * contains values whose tags match the regex.
     *
     * After custom categories are evaluated, the tags are sorted by a hardcoded
     * fallback categorizer, which may, for example, group tags into categories
     * based on their top namespace.
     */
    /* Canonical TensorFlow ops are namespaced using forward slashes.
     * This fallback categorizer categorizes by the top-level namespace.
     */
    Categorizer.topLevelNamespaceCategorizer = splitCategorizer(/\//);
    function fallbackCategorizer(s) {
        switch (s) {
            case 'TopLevelNamespaceCategorizer':
                return Categorizer.topLevelNamespaceCategorizer;
            default:
                throw new Error('Unrecognized categorization strategy: ' + s);
        }
    }
    Categorizer.fallbackCategorizer = fallbackCategorizer;
    /* An 'extractor' is a function that takes a tag name, and 'extracts' a
     * category name.
     * This function takes an extractor, and produces a categorizer.
     * Currently, it is just used for the fallbackCategorizer, but we may want to
     * refactor the general categorization logic to use the concept of extractors.
     */
    function extractorToCategorizer(extractor) {
        return function (tags) {
            if (tags.length === 0) {
                return [];
            }
            var sortedTags = tags.slice().sort(VZ.Sorting.compareTagNames);
            var categories = [];
            var currentCategory = {
                name: extractor(sortedTags[0]),
                tags: [],
            };
            sortedTags.forEach(function (t) {
                var topLevel = extractor(t);
                if (currentCategory.name !== topLevel) {
                    categories.push(currentCategory);
                    currentCategory = {
                        name: topLevel,
                        tags: [],
                    };
                }
                currentCategory.tags.push(t);
            });
            categories.push(currentCategory);
            return categories;
        };
    }
    function splitCategorizer(r) {
        var extractor = function (t) {
            return t.split(r)[0];
        };
        return extractorToCategorizer(extractor);
    }
    function defineCategory(ruledef) {
        var r = new RegExp(ruledef);
        var f = function (tag) {
            return r.test(tag);
        };
        return { name: ruledef, matches: f };
    }
    Categorizer.defineCategory = defineCategory;
    function _categorizer(rules, fallback) {
        return function (tags) {
            var remaining = d3.set(tags);
            var userSpecified = rules.map(function (def) {
                var tags = [];
                remaining.forEach(function (t) {
                    if (def.matches(t)) {
                        tags.push(t);
                    }
                });
                var cat = { name: def.name, tags: tags.sort(VZ.Sorting.compareTagNames) };
                return cat;
            });
            var defaultCategories = fallback(remaining.values());
            return userSpecified.concat(defaultCategories);
        };
    }
    Categorizer._categorizer = _categorizer;
    function categorizer(s) {
        var rules = s.categoryDefinitions.map(defineCategory);
        var fallback = fallbackCategorizer(s.fallbackCategorizer);
        return _categorizer(rules, fallback);
    }
    Categorizer.categorizer = categorizer;
    ;
})(Categorizer || (Categorizer = {}));
