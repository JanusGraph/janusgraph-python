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

from pytest import fixture

from integration.RelationIdentifier_test import _RelationIdentifierSerializer, _RelationIdentifierDeserializer
from integration.Text_test import _TextTests

class TestGraphSONRelationIdentifierSerializer(_RelationIdentifierSerializer):
    @fixture(autouse=True)
    def _graph_connection_graphson(self, graph_connection_graphson):
        # setting up 'g' variable so parent class's methods can use it
        self.g = graph_connection_graphson

class TestGraphSONRelationIdentifierDeserializer(_RelationIdentifierDeserializer):
    @fixture(autouse=True)
    def _graph_connection_graphson(self, graph_connection_graphson):
        # setting up 'g' variable so parent class's methods can use it
        self.g = graph_connection_graphson

class TestGraphSONText(_TextTests):
    @fixture(autouse=True)
    def _graph_connection_graphson(self, graph_connection_graphson):
        # setting up 'g' variable so parent class's methods can use it
        self.g = graph_connection_graphson