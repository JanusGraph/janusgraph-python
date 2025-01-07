# Copyright 2024 JanusGraph-Python Authors
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

from collections import OrderedDict
from gremlin_python.structure.io.graphsonV3d0 import _GraphSONTypeIO, EdgeDeserializer, GraphSONUtil, GraphSONReader, GraphSONWriter
from gremlin_python.structure.graph import Edge, Vertex
from janusgraph_python.process.traversal import _JanusGraphP, RelationIdentifier

class JanusGraphSONReader(GraphSONReader):
    def __init__(self):
        # register JanusGraph-specific RelationIdentifier deserializer
        deserializer_map = {
            'janusgraph:RelationIdentifier': JanusGraphRelationIdentifierIO
        }
        GraphSONReader.__init__(self, deserializer_map)

class JanusGraphSONWriter(GraphSONWriter):
    def __init__(self):
        # register JanusGraph-specific RelationIdentifier and text-predicate serializer
        serializer_map = [
            (RelationIdentifier, JanusGraphRelationIdentifierIO),
            (_JanusGraphP, JanusGraphPSerializer)
        ]
        GraphSONWriter.__init__(self, serializer_map)


class JanusGraphPSerializer(_GraphSONTypeIO):
    @classmethod
    def dictify(cls, p, writer):
        out = {"predicate": p.operator,
               "value": [writer.to_dict(p.value), writer.to_dict(p.other)] if p.other is not None else
               writer.to_dict(p.value)}
        return GraphSONUtil.typed_value("JanusGraphP", out, "janusgraph")

class JanusGraphRelationIdentifierIO(_GraphSONTypeIO):
    @classmethod
    def objectify(cls, l, reader):    
        return RelationIdentifier.from_string(l['relationId'])
    
    @classmethod
    def dictify(cls, relation_identifier, writer):
        out = { "relationId": relation_identifier.string_representation }
        return GraphSONUtil.typed_value("RelationIdentifier", out, "janusgraph")
