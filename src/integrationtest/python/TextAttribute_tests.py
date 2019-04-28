# Name: Debasish Kanhar

import unittest
from subprocess import Popen, PIPE
from JanuaGraphContainer import JanusGraphContainer
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from gremlin_python.structure.graph import Graph
from janusgraph_python.core.attribute.Text import Text


class TestTextAttributes(unittest.TestCase):
    def setUp(self):
        self.container = JanusGraphContainer()

        docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
        docker_ip = docker_ip.strip().decode("utf-8")

        self.client = JanusGraphClient()
        self.client = self.client.connect(host=str(docker_ip), port="8182",
                                          traversal_source="gods_traversal").get_connection()

        self.container.start()
        self.g = Graph().traversal().withRemote(self.client)

    def tearDown(self) -> None:
        self.client.close()
        self.container.stop()

    def test_text_fuzzy(self):

        truth = {"luves fresh breezs": 1, "shouldNotBeFound": 0}

        for k, v in truth.items():
            count = self.g.E().has("reason", Text.textFuzzy(k)).count().next()
            self.assertEqual(count, v)

    def test_text_prefix(self):

        truth = {"s": 3, "shouldNotBeFound": 0}

        for k, v in truth.items():
            count = self.g.V().has("name", Text.textPrefix(k)).count().next()
            self.assertEqual(count, v)

    def test_text_regex(self):

        truth = {"s.{2}": 2, "shouldNotBeFound": 0}

        for k, v in truth.items():
            count = self.g.V().has("name", Text.textRegex(k)).count().next()
            self.assertEqual(count, v)

    def test_text_contains_regex(self):

        truth = {"f.{3,4}": 2, "shouldNotBeFound": 0}

        for k, v in truth.items():
            count = self.g.E().has("reason", Text.textContainsRegex(k)).count().next()
            self.assertEqual(count, v)

    def test_text_contains_fuzzy(self):

        truth = {"waxes": 1, "shouldNotBeFound": 0}

        for k, v in truth.items():
            count = self.g.E().has("reason", Text.textContainsFuzzy(k)).count().next()

            self.assertEqual(count, v)

    def test_text_contains_prefix(self):

        truth = {"wave": 1, "shouldNotBeFound": 0}

        for k, v in truth.items():
            count = self.g.E().has("reason", Text.textContainsPrefix(k)).count().next()

            self.assertEqual(count, v)

    def test_text_contains(self):

        truth = {"loves": 2, "shouldNotBeFound": 0}

        for k, v in truth.items():
            count = self.g.E().has("reason", Text.textContains(k)).count().next()

            self.assertEqual(count, v)
