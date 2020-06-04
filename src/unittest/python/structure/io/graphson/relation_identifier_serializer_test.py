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
import json
from janusgraph_python.core.datatypes.relation_identifier import RelationIdentifier
from janusgraph_python.structure.io.graphson.graphson_writer_builder import JanusGraphSONWriterBuilder


class TestRelationIdentifierSerializer(unittest.TestCase):

    def test_relation_id_serialization(self):
        relation_id = "74q-9n4-b2t-cr4"

        edge = RelationIdentifier(relation_id)
        writer = JanusGraphSONWriterBuilder().build()

        actual_json_str = writer.writeObject(edge)

        expected_json_str = json.dumps({
            "@type": "janusgraph:RelationIdentifier",
            "@value": {"relationId": relation_id}
        }, separators=(',', ':'))

        self.assertEqual(actual_json_str, expected_json_str)
