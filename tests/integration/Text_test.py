# Copyright 2023 JanusGraph-Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pytest import mark, param
from janusgraph_python.process.traversal import Text

class _TextTests(object):
    # g is expected to be set once this class is inherited
    g = None

    @mark.parametrize(
        'search_text,expected_count',
        [
            param('loves', 2),
            param('shouldNotBeFound', 0),
        ]
    )
    def test_text_contains_given_search_text(self, search_text, expected_count):
        count = self.g.E().has('reason', Text.text_contains(search_text)).count().next()
        assert count == expected_count

    @mark.parametrize(
        'search_text,expected_count',
        [
            param('wave', 1),
            param('f', 2),
            param('shouldNotBeFound', 0),
        ]
    )
    def test_text_contains_prefix_given_search_text(self, search_text, expected_count):
        count = self.g.E().has('reason', Text.text_contains_prefix(search_text)).count().next()
        assert count == expected_count

    @mark.parametrize(
        'search_text,expected_count',
        [
            param('.*ave.*', 1),
            param('f.{3,4}', 2),
            param('shouldNotBeFound', 0),
        ]
    )
    def test_text_contains_regex_given_search_text(self, search_text, expected_count):
        count = self.g.E().has('reason', Text.text_contains_regex(search_text)).count().next()
        assert count == expected_count

    @mark.parametrize(
        'search_text,expected_count',
        [
            param('waxes', 1),
            param('shouldNotBeFound', 0),
        ]
    )
    def test_text_contains_fuzzy_given_search_text(self, search_text, expected_count):
        count = self.g.E().has('reason', Text.text_contains_fuzzy(search_text)).count().next()
        assert count == expected_count

    @mark.parametrize(
        'search_text,expected_count',
        [
            param('herc', 1),
            param('s', 3),
            param('shouldNotBeFound', 0),
        ]
    )
    def test_text_prefix_given_search_text(self, search_text, expected_count):
        count = self.g.V().has('name', Text.text_prefix(search_text)).count().next()
        assert count == expected_count

    @mark.parametrize(
        'search_text,expected_count',
        [
            param('.*rcule.*', 1),
            param('s.{2}', 2),
            param('shouldNotBeFound', 0),
        ]
    )
    def test_text_regex_given_search_text(self, search_text, expected_count):
        count = self.g.V().has('name', Text.text_regex(search_text)).count().next()
        assert count == expected_count

    @mark.parametrize(
        'search_text,expected_count',
        [
            param('herculex', 1),
            param('ska', 2),
            param('shouldNotBeFound', 0),
        ]
    )
    def test_text_fuzzy_given_search_text(self, search_text, expected_count):
        count = self.g.V().has('name', Text.text_fuzzy(search_text)).count().next()
        assert count == expected_count
        