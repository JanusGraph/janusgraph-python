# Name: Debasish Kanhar

import unittest
from subprocess import Popen, PIPE
from JanuaGraphContainer import JanusGraphContainer
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from gremlin_python.structure.graph import Graph
from janusgraph_python.core.attribute.Geo import Geo
from janusgraph_python.core.datatypes.GeoShape import GeoShape


class TestGeoAttributes(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

    def test_geo_contains(self):
        self.container.start()

        docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        docker_ip = docker_ip.strip().decode("utf-8")

        client = JanusGraphClient()
        client = client.connect(host=str(docker_ip), port="8182",
                                            traversal_source="gods_traversal").get_connection()

        g = Graph().traversal().withRemote(client)

        # First we will need to add a property so that GeoContains can be queried.
        place = GeoShape.Circle(50, 100, 100)
        tarturus = g.V().has("name", "tartarus").property("place", place).next()

        truth = {GeoShape.Circle(50, 100, 10): 1, GeoShape.Circle(50, 100, 500): 0}

        for k, v in truth.items():
            count = g.E().has("place", Geo.geoContains(k)).count().next()
            self.assertEqual(count, v)

        client.close()

        self.container.stop()

    def test_geo_within(self):
        self.container.start()

        docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        docker_ip = docker_ip.strip().decode("utf-8")

        client = JanusGraphClient()
        client = client.connect(host=str(docker_ip), port="8182",
                                traversal_source="gods_traversal").get_connection()

        g = Graph().traversal().withRemote(client)

        truth = {GeoShape.Circle(37.97, 23.72, 50): 2, GeoShape.Circle(37.97, 23.72, 5): 0}

        for k, v in truth.items():
            count = g.E().has("place", Geo.geoWithin(k)).count().next()
            self.assertEqual(count, v)

        client.close()

        self.container.stop()
