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

from janusgraph_python.structure.io.graphson.graphson_writer_builder import JanusGraphSONWriterBuilder
from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil


class X(object):
    def objectify(self):
        return {key: value for key, value in self.__dict__.items()
                if not key.startswith('__') and not callable(key)}


class MockSerializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "MOCK"
    GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)
    serializedJSON = None

    @classmethod
    def dictify(cls, obj, writer):
        """

        Args:
            obj (X):
            writer:

        Returns:

        """

        value = obj.objectify()
        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, value, cls.GRAPHSON_PREFIX)
        cls.serializedJSON = serializedJSON
        return serializedJSON

    def serialize(self, obj):
        value = obj.objectify()
        serializedJSON = GraphSONUtil.typedValue(self.GRAPHSON_BASE_TYPE, value, self.GRAPHSON_PREFIX)
        self.serializedJSON = serializedJSON
        return self

    def get_serialized_json(self):
        return self.serializedJSON


class TestGraphsonWriter(unittest.TestCase):

    def test_mock_serializer(self):
        mock_obj_type = X

        # Create Mock object's serializer
        serializer = MockSerializer

        writer_class = JanusGraphSONWriterBuilder()

        # Register the serializer and object. and build it.
        writer_class.register_serializer(mock_obj_type, serializer)
        writer = writer_class.build()

        # Test the updated writer build.
        mock_obj = X()
        # Serialize mock object into GSON
        mock_gson = writer.writeObject(mock_obj)

        # Retrieve actual serialization from MockSerializer
        mock_ser = MockSerializer().serialize(mock_obj)

        expected_json = json.loads(mock_gson)
        actual_json = mock_ser.get_serialized_json()

        self.assertEqual(expected_json, actual_json)
