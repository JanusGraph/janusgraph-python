# Name: Debasish Kanhar

import unittest
import json
from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier
from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter


class TestRelationIdentifierSerializer(unittest.TestCase):
    def setUp(self):
        self.relationID = "74q-9n4-b2t-cr4"
        self.edge = RelationIdentifier(self.relationID)
        self.writer = JanusGraphSONWriter().build()
        pass

    def test_relationID_serialization(self):
        graphSON = self.writer.writeObject(self.edge)

        expectedJSONStr = "{\"@type\":\"janusgraph:RelationIdentifier\",\"@value\": {\"relationId\": \"" + self.relationID + "\"}}"

        expectedJSON = json.loads(expectedJSONStr)
        actualJSON = json.loads(graphSON)

        self.assertEqual(expectedJSON, actualJSON)
        pass
