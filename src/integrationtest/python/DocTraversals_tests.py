# Name: Debasish Kanhar

import unittest
from subprocess import Popen, PIPE
from JanusGraphContainer import JanusGraphContainer
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from gremlin_python.structure.graph import Graph


class TestDocTraversals(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

        # docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        # docker_ip = docker_ip.strip().decode("utf-8")
        #
        # print("IP is ", docker_ip)

        self.client = JanusGraphClient().connect(host=str("localhost"), port="8182",
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
