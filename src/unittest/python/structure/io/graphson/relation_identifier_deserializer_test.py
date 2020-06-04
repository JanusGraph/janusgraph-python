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

import json
import unittest
from janusgraph_python.structure.io.graphson.graphson_reader_builder import JanusGraphSONReaderBuilder
from janusgraph_python.core.datatypes.relation_identifier import RelationIdentifier


class TestRelationIdentifierDeserialization(unittest.TestCase):

    def test_relationID_deserialization(self):
        relation_id = "74q-9n4-b2t-cr4"

        reader = JanusGraphSONReaderBuilder().build()

        rel_id_json_str = json.dumps({
            "@type": "janusgraph:RelationIdentifier",
            "@value": {"relationId": relation_id}
        }, separators=(",", ":"))

        actual_relation_id = reader.readObject(rel_id_json_str)
        expected_relation_id = RelationIdentifier(relation_id)

        self.assertEqual(actual_relation_id, expected_relation_id)
