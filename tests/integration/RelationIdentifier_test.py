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

from pytest import mark, param
from janusgraph_python.process.traversal import RelationIdentifier

class _RelationIdentifierSerializer(object):
    # g is expected to be set once this class is inherited
    g = None

    @mark.parametrize(
        'vertex_id,edge_type',
        [
            param(1280, 'mother', id='long in and out vertex ID'),
            param('jupiter', 'lives', id='long in vertex ID, string out vertex ID'),
            param('jupiter', 'brother', id='string in and out vertex ID'),
            param(1024, 'father', id='string in vertex ID, long out vertex ID'),
        ]
    )
    def test_RelationIdentifier_as_edge_id(self, vertex_id, edge_type):
        edge_id = self.g.V(vertex_id).both_e(edge_type).id_().next()

        count = self.g.E(edge_id).count().next()
        assert count == 1

    @mark.parametrize(
        'vertex_id,edge_type',
        [
            param(1280, 'mother', id='long in and out vertex ID'),
            param('jupiter', 'lives', id='long in vertex ID, string out vertex ID'),
            param('jupiter', 'brother', id='string in and out vertex ID'),
            param(1024, 'father', id='string in vertex ID, long out vertex ID'),
        ]
    )
    def test_Edge(self, vertex_id, edge_type):
        edge = self.g.V(vertex_id).both_e(edge_type).next()

        count = self.g.E(edge).count().next()
        assert count == 1

class _RelationIdentifierDeserializer(object):
    # g is expected to be set once this class is inherited
    g = None

    @mark.parametrize(
        'vertex_id,edge_type',
        [
            param(1280, 'mother', id='long in and out vertex ID'),
            param('jupiter', 'lives', id='long in vertex ID, string out vertex ID'),
            param('jupiter', 'brother', id='string in and out vertex ID'),
            param(1024, 'father', id='string in vertex ID, long out vertex ID'),
        ]
    )
    def test_valid_RelationIdentifier(self, vertex_id, edge_type):
        relation_identifier = self.g.V(vertex_id).both_e(edge_type).id_().next()

        assert type(relation_identifier) is RelationIdentifier

    @mark.parametrize(
        'vertex_id,edge_type',
        [
            param(1280, 'mother', id='long in and out vertex ID'),
            param('jupiter', 'lives', id='long in vertex ID, string out vertex ID'),
            param('jupiter', 'brother', id='string in and out vertex ID'),
            param(1024, 'father', id='string in vertex ID, long out vertex ID'),
        ]
    )
    def test_Edge(self, vertex_id, edge_type):
        edge = self.g.V(vertex_id).both_e(edge_type).next()

        assert type(edge.id) is RelationIdentifier