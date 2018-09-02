# Name: Debasish Kanhar

import unittest
import json
try:
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
except ImportError:
    from gremlin_python.structure.io.graphson import GraphSONUtil
from janusgraph_python.structure.io.GraphsonReader import JanusGraphSONReader


class MockDeserializer(object):
    def __init__(self):
        pass

    @classmethod
    def objectify(cls, graphsonObj, reader):
        obj = Mock(**graphsonObj)
        return obj


class Mock(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        pass

    def objectify(self):
        return {key: value for key, value in self.__dict__.items()
                if not key.startswith('__') and not callable(key)}

    def __str__(self):
        return str(self.objectify())

    def __eq__(self, other):
        """

        Args:
            other (Mock):

        Returns:

        """

        attributes = other.objectify()

        for k, v in attributes.items():
            if getattr(self, k) == getattr(other, k):
                pass
            else:
                return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class TestGraphsonReader(unittest.TestCase):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "MOCK"
    MOCK_GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)

    def setUp(self):
        self.readerClass = JanusGraphSONReader()
        self.reader = None

        pass

    def test_mock_deserializer(self):
        deserializer = MockDeserializer

        self.readerClass.register_deserializer(self.MOCK_GRAPHSON_TYPE, deserializer)
        self.reader = self.readerClass.build()

        mockGSON = "{\"@type\":\"janusgraph:MOCK\",\"@value\":{\"a\": 1}}"
        mockJSON = json.loads(mockGSON)

        expectedMockObj = self.reader.toObject(mockJSON)
        actualMockObj = Mock()

        self.assertEqual(expectedMockObj, actualMockObj)
