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
from janusgraph_python.structure.io.GraphsonReader import JanusGraphSONReader
from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier


class TestRelationIdentifierDeserialization(unittest.TestCase):

    def test_relationID_deserialization(self):
        relationID = "74q-9n4-b2t-cr4"

        reader = JanusGraphSONReader().build()

        relIDJSON = dict()
        relIDJSON["@type"] = "janusgraph:RelationIdentifier"
        relIDJSON["@value"] = {"relationId": relationID}

        expectedRelID = reader.toObject(relIDJSON)
        actualRelID = RelationIdentifier(relationID)

        self.assertEqual(expectedRelID, actualRelID.__str__())
