# Name: Debasish Kanhar

import unittest
from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier


class TestRelationIdentifier(unittest.TestCase):
    def setUp(self):
        self.relationID = "74q-9n4-b2t-cr4"

        self.edgeID = RelationIdentifier(self.relationID)
        pass

    def test_relationID_equality(self):
        id1 = "74q-9n4-b2t-cr4"
        id2 = "74q-9n4-b2t-cr6"

        e1 = self.edgeID
        e2 = RelationIdentifier(id1)
        e3 = RelationIdentifier(id2)

        self.assertEqual(e1, e2)
        self.assertNotEqual(e1, e3)
        pass
