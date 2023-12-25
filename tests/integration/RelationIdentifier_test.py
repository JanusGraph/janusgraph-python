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

from janusgraph_python.process.traversal import RelationIdentifier

class _RelationIdentifierSerializer(object):
    # g is expected to be set once this class is inherited
    g = None

    def test_RelationIdentifier_as_edge_id(self):
        edge_id = self.g.E().id_().next()

        count = self.g.E(edge_id).count().next()
        assert count == 1

    def test_Edge(self):
        edge = self.g.E().next()

        count = self.g.E(edge).count().next()
        assert count == 1

class _RelationIdentifierDeserializer(object):
    # g is expected to be set once this class is inherited
    g = None

    def test_valid_RelationIdentifier(self):
        relation_identifier = self.g.V().has('demigod', 'name', 'hercules').out_e('father').id_().next()

        assert type(relation_identifier) is RelationIdentifier

    def test_Edge(self):
        edge = self.g.V().has('demigod', 'name', 'hercules').out_e('father').next()

        assert type(edge.id) is RelationIdentifier