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
            bool
        """

        attributes = other.objectify()

        if len(self.objectify()) != len(attributes):
            return False

        for k, _ in attributes.items():
            if getattr(self, k) != getattr(other, k):
                return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class TestGraphsonReader(unittest.TestCase):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "MOCK"

    def test_mock_deserializer(self):
        deserializer = MockDeserializer

        readerClass = JanusGraphSONReader()

        readerClass.register_deserializer(self.GRAPHSON_BASE_TYPE, deserializer)
        reader = readerClass.build()

        mockJSON = dict()
        mockJSON["@type"] = "janusgraph:MOCK"
        mockJSON["@value"] = {"a": 1}

        actualMockObj = reader.toObject(mockJSON)
        expectedMockObj = Mock(a=1)

        self.assertEqual(expectedMockObj, actualMockObj)
