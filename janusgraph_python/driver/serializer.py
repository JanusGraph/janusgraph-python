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

from gremlin_python.driver.serializer import GraphSONSerializersV3d0, GraphBinarySerializersV1
from janusgraph_python.structure.io import graphsonV3d0, graphbinaryV1

class JanusGraphSONSerializersV3d0(GraphSONSerializersV3d0):
    """Message serializer for GraphSON 3.0 extended with JanusGraph-specific types"""
    def __init__(self):
        reader = graphsonV3d0.JanusGraphSONReader()
        writer = graphsonV3d0.JanusGraphSONWriter()
        super(GraphSONSerializersV3d0, self).__init__(reader, writer)

class JanusGraphBinarySerializersV1(GraphBinarySerializersV1):
    """Message serializer for GraphBinary 1.0 extended with JanusGraph-specific types"""
    def __init__(self):
        reader = graphbinaryV1.JanusGraphBinaryReader()
        writer = graphbinaryV1.JanusGraphBinaryWriter()
        super().__init__(reader, writer)