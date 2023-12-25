# Copyright 2023 JanusGraph-Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from janusgraph_python.structure.io.graphsonV3d0 import JanusGraphSONReader, JanusGraphSONWriter
from janusgraph_python.process.traversal import RelationIdentifier, _JanusGraphP

class TestJanusGraphSONReader(object):
    graphson_reader = JanusGraphSONReader()

    def test_RelationIdentifier(self):
        relation_id = "3k1-360-6c5-39c"
        expected_relation_identifier = RelationIdentifier.from_string(relation_id);

        graphSON = json.dumps({"@type":"janusgraph:RelationIdentifier","@value":{"relationId":relation_id}})

        relation_identifier = self.graphson_reader.read_object(graphSON)

        assert relation_identifier == expected_relation_identifier


class TestJanusGraphSONWriter(object):
    graphson_writer = JanusGraphSONWriter()

    def test_RelationIdentifier(self):
        relation_id = "4qp-360-7x1-3aw"
        expected = json.dumps({"@type":"janusgraph:RelationIdentifier","@value":{"relationId":relation_id}}, separators=(',', ':'))

        relation_identifier = RelationIdentifier.from_string(relation_id)
        output = self.graphson_writer.write_object(relation_identifier)
        
        assert expected == output

    def test_JanusGraphP(self):
        result_1 = {
            "@type": "janusgraph:JanusGraphP",
            "@value": { "predicate":"textContains", "value":"John" }
        }
        predicate_1 = _JanusGraphP("textContains", "John")
        assert result_1 == json.loads(self.graphson_writer.write_object(predicate_1))

        result_2 = {
            "@type": "g:P",
            "@value": {
                "predicate": "and",
                "value": [
                    {
                        "@type":"g:P",
                        "@value": {
                            "predicate":"or",
                            "value":[ 
                                {
                                    "@type":"janusgraph:JanusGraphP",
                                    "@value":{
                                        "predicate":"textContains",
                                        "value":"John"
                                    }
                                },
                                {
                                    "@type":"janusgraph:JanusGraphP",
                                    "@value": {
                                        "predicate":"textContainsPrefix",
                                        "value":"John"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "@type":"janusgraph:JanusGraphP",
                        "@value": {
                            "predicate":"textContainsFuzzy",
                            "value":"Juhn"
                        }
                    }
                ]
            }
        }
        predicate_2 = (
            _JanusGraphP("textContains", "John").
            or_(_JanusGraphP("textContainsPrefix", "John")).
            and_(_JanusGraphP("textContainsFuzzy", "Juhn"))
        )
        assert result_2 == json.loads(self.graphson_writer.write_object(predicate_2))


class TestJanusGraphSONReaderWriterSymmetricy(object):
    graphson_writer = JanusGraphSONWriter()
    graphson_reader = JanusGraphSONReader()

    def test_RelationIdentifier(self):
        relation_identifier = RelationIdentifier.from_string("4qp-360-7x1-3aw")
        
        graphSON = self.graphson_writer.write_object(relation_identifier)
        read_relation_identifier = self.graphson_reader.read_object(graphSON)

        assert relation_identifier == read_relation_identifier