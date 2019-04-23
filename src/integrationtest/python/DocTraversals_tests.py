# Name: Debasish Kanhar

import unittest
from subprocess import Popen, PIPE
from JanuaGraphContainer import JanusGraphContainer
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from gremlin_python.structure.graph import Graph


class TestDocTraversals(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

    def test_gremlin_getting_started(self):
        self.container.start()

        docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        docker_ip = docker_ip.strip().decode("utf-8")

        client = JanusGraphClient()
        client = client.connect(host=str(docker_ip), port="8182",
                                traversal_source="gods_traversal").get_connection()

        g = Graph().traversal().withRemote(client)

        herculesAge = g.V().has("name", "hercules").values("age").next()

        self.assertEqual(herculesAge, 30)

        self.container.stop()

    def test_receiving_edges(self):
        self.container.start()

        docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        docker_ip = docker_ip.strip().decode("utf-8")

        client = JanusGraphClient()
        client = client.connect(host=str(docker_ip), port="8182",
                                traversal_source="gods_traversal").get_connection()

        g = Graph().traversal().withRemote(client)

        edges = g.V().has("name", "hercules").outE("battled").toList()

        self.assertEqual(len(edges), 3)

        self.container.stop()

    def test_geo_point_received(self):
        self.container.start()

        docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        docker_ip = docker_ip.strip().decode("utf-8")

        client = JanusGraphClient()
        client = client.connect(host=str(docker_ip), port="8182",
                                traversal_source="gods_traversal").get_connection()

        g = Graph().traversal().withRemote(client)

        firstBattlePlace = g.V().has("name", "hercules").outE("battled").order().by("time").values("place").next()

        self.assertEqual(firstBattlePlace.getLatitude(), 38.1)
        self.assertEqual(firstBattlePlace.getLongitude(), 23.7)

        self.container.stop()
