# Name: Debasish Kanhar

import unittest
from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter
try:
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
except ImportError:
    from gremlin_python.structure.io.graphson import GraphSONUtil
import json


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

    def setUp(self):
        self.writerClass = JanusGraphSONWriter()
        self.writer = None
        pass

    def test_mock_serializer(self):
        # Create Mock Object
        mockObj = X
        # Create Mock object's serializer
        serializer = MockSerializer

        # Register the serializer and object. and build it.
        self.writerClass.register_serializer(mockObj, serializer)
        self.writer = self.writerClass.build()

        # Test the updated writer build.
        mockObj = X()
        # Serialize mock object into GSON
        mockGSON = self.writer.writeObject(mockObj)

        # Retrive actual serialization from MockSerializer
        mockSer = MockSerializer().serialize(mockObj)

        expectedJSON = json.loads(mockGSON)
        actualJSON = mockSer.get_serialized_json()

        self.assertEqual(expectedJSON, actualJSON)
