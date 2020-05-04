# Copyright 2018 JanusGraph Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from janusgraph_container import JanusGraphContainer
from janusgraph_python.driver.janusgraph_remote_connection_builder import JanusGraphRemoteConnectionBuilder
from gremlin_python.structure.graph import Graph
from janusgraph_python.core.attribute.text import Text


class TestTextAttributes(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

        self.client = JanusGraphRemoteConnectionBuilder().connect(host=self.container.get_host_ip(), port=8182,
                                                 traversal_source="gods_traversal").get_connection()

        self.container.start()
        self.g = Graph().traversal().withRemote(self.client)

    def tearDown(self) -> None:
        self.client.close()
        self.container.stop()

    def test_text_fuzzy(self):

        mock_data = {"luves fresh breezs": 1, "shouldNotBeFound": 0}

        for k, v in mock_data.items():
            count = self.g.E().has("reason", Text.textFuzzy(k)).count().next()
            self.assertEqual(count, v)

    def test_text_prefix(self):

        mock_data = {"s": 3, "shouldNotBeFound": 0}

        for k, v in mock_data.items():
            count = self.g.V().has("name", Text.textPrefix(k)).count().next()
            self.assertEqual(count, v)

    def test_text_regex(self):

        mock_data = {"s.{2}": 2, "shouldNotBeFound": 0}

        for k, v in mock_data.items():
            count = self.g.V().has("name", Text.textRegex(k)).count().next()
            self.assertEqual(count, v)

    def test_text_contains_regex(self):
        mock_data = {"f.{3,4}": 2, "shouldNotBeFound": 0}

        for k, v in mock_data.items():
            count = self.g.E().has("reason", Text.textContainsRegex(k)).count().next()
            self.assertEqual(count, v)

    def test_text_contains_fuzzy(self):
        mock_data = {"waxes": 1, "shouldNotBeFound": 0}

        for k, v in mock_data.items():
            count = self.g.E().has("reason", Text.textContainsFuzzy(k)).count().next()

            self.assertEqual(count, v)

    def test_text_contains_prefix(self):
        mock_data = {"wave": 1, "shouldNotBeFound": 0}

        for k, v in mock_data.items():
            count = self.g.E().has("reason", Text.textContainsPrefix(k)).count().next()

            self.assertEqual(count, v)

    def test_text_contains(self):
        mock_data = {"loves": 2, "shouldNotBeFound": 0}

        for k, v in mock_data.items():
            count = self.g.E().has("reason", Text.textContains(k)).count().next()

            self.assertEqual(count, v)
