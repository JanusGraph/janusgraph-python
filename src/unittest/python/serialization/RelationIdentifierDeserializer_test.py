# Name: Debasish Kanhar

import unittest
import json
from janusgraph_python.structure.io.GraphsonReader import JanusGraphSONReader
from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier


class TestRelationIdentifierDeserialization(unittest.TestCase):
    def setUp(self):
        self.relationID = "74q-9n4-b2t-cr4"
        self.reader = JanusGraphSONReader().build()
        pass

    def test_relationID_deserialization(self):
        relIDGson = "{\"@type\":\"janusgraph:RelationIdentifier\",\"@value\": {\"relationId\": \"" + self.relationID + "\"}}"

        relIDJSON = json.loads(relIDGson)

        expectedRelID = self.reader.toObject(relIDJSON)
        actualRelID = RelationIdentifier(self.relationID)

        self.assertEqual(expectedRelID, actualRelID)
