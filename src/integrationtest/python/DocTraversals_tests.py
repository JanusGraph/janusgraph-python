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
from JanusGraphContainer import JanusGraphContainer
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from gremlin_python.structure.graph import Graph


class TestDocTraversals(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

        self.client = JanusGraphClient().connect(host=self.container.get_host_ip(), port="8182",
                                traversal_source="gods_traversal").get_connection()

        self.container.start()
        self.g = Graph().traversal().withRemote(self.client)

    def tearDown(self) -> None:
        self.client.close()
        self.container.stop()

    def test_gremlin_getting_started(self):

        herculesAge = self.g.V().has("name", "hercules").values("age").next()

        self.assertEqual(herculesAge, 30)

    def test_receiving_edges(self):

        edges = self.g.V().has("name", "hercules").outE("battled").toList()

        self.assertEqual(len(edges), 3)

    def test_geo_point_received(self):

        firstBattlePlace = self.g.V().has("name", "hercules").outE("battled").order().by("time").values("place").next()

        self.assertEqual(firstBattlePlace.getLatitude(), 38.1)
        self.assertEqual(firstBattlePlace.getLongitude(), 23.7)
