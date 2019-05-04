# Name: Debasish Kanhar

import unittest
from subprocess import Popen, PIPE
from JanusGraphContainer import JanusGraphContainer
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from gremlin_python.structure.graph import Graph
from janusgraph_python.core.attribute.Geo import Geo
from janusgraph_python.core.datatypes.GeoShape import GeoShape


class TestGeoAttributes(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

        docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        docker_ip = docker_ip.strip().decode("utf-8")

        self.client = JanusGraphClient().connect(host=str(docker_ip), port="8182",
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

        mock_data = {GeoShape.Circle(50, 100, 10): 1, GeoShape.Circle(50, 100, 500): 0}

        for k, v in mock_data.items():
            count = self.g.E().has("place", Geo.geoContains(k)).count().next()
            self.assertEqual(count, v)

    def test_geo_within(self):

        mock_data = {GeoShape.Circle(37.97, 23.72, 50): 2, GeoShape.Circle(37.97, 23.72, 5): 0}

        for k, v in mock_data.items():
            count = self.g.E().has("place", Geo.geoWithin(k)).count().next()
            self.assertEqual(count, v)
