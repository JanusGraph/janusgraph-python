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
# limitations under the License.Kanhar

import unittest
from JanusGraphContainer import JanusGraphContainer
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from gremlin_python.structure.graph import Graph
from janusgraph_python.core.attribute.Geo import Geo
from janusgraph_python.core.datatypes.GeoShape import GeoShape


class TestGeoAttributes(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

        self.client = JanusGraphClient().connect(host=self.container.get_host_ip(), port="8182",
                                                 traversal_source="gods_traversal").get_connection()

        self.container.start()
        self.g = Graph().traversal().withRemote(self.client)

    def tearDown(self) -> None:
        self.client.close()
        self.container.stop()

    def test_geo_contains(self):

        # First we will need to add a property so that GeoContains can be queried.
        place = GeoShape.Circle(50, 100, 100)
        self.g.V().has("name", "tartarus").property("place", place).next()

        # Now that a place with name tartaraus is added into graph with coordinates (50,100) and radius 100,

        mock_data = {GeoShape.Circle(50, 100, 10): 1, GeoShape.Circle(50, 100, 500): 0}
        # Let us now query is any Geo shapes in Graph contains the following Geo objects:
        #   1: Geo circle of (50, 100) and radius 10 (Tartaraus just added above contains this object)
        #   2: Geo circle of (50, 100) and radius 500 (None)

        for k, v in mock_data.items():
            count = self.g.E().has("place", Geo.geoContains(k)).count().next()
            self.assertEqual(count, v)

    def test_geo_within(self):

        mock_data = {GeoShape.Circle(37.97, 23.72, 50): 2, GeoShape.Circle(37.97, 23.72, 5): 0}

        for k, v in mock_data.items():
            count = self.g.E().has("place", Geo.geoWithin(k)).count().next()
            self.assertEqual(count, v)
