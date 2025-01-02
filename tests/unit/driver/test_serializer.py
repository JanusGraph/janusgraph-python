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

from janusgraph_python.driver.serializer import JanusGraphSONSerializersV3d0, JanusGraphBinarySerializersV1
from janusgraph_python.structure.io import graphsonV3d0, graphbinaryV1


def test_graphson_serializer_v3():
    graphson_serializer_v3 = JanusGraphSONSerializersV3d0()

    assert graphson_serializer_v3.version == b"application/vnd.gremlin-v3.0+json"
    assert isinstance(graphson_serializer_v3._graphson_reader, graphsonV3d0.JanusGraphSONReader)
    assert isinstance(graphson_serializer_v3.standard._writer, graphsonV3d0.JanusGraphSONWriter)
    assert isinstance(graphson_serializer_v3.traversal._writer, graphsonV3d0.JanusGraphSONWriter)

def test_graphbinary_serializer_v1():
    graphbinary_serializer_v1 = JanusGraphBinarySerializersV1()

    assert graphbinary_serializer_v1.version == b"application/vnd.graphbinary-v1.0"
    assert isinstance(graphbinary_serializer_v1._graphbinary_reader, graphbinaryV1.JanusGraphBinaryReader)
    assert isinstance(graphbinary_serializer_v1.standard._writer, graphbinaryV1.JanusGraphBinaryWriter)
    assert isinstance(graphbinary_serializer_v1.traversal._writer, graphbinaryV1.JanusGraphBinaryWriter)