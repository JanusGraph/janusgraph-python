# Name: Debasish Kanhar

import unittest
import json

from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter


class TestCircleSerialization(unittest.TestCase):

    def setUp(self):
        self.latitude = 80
        self.longitude = 100

        self.point = Point(self.longitude, self.latitude)

        self.writer = JanusGraphSONWriter().build()
        pass

    def test_point_serialization(self):
        graphSON = self.writer.writeObject(self.point)

        expectedJSONStr = "{\"@type\":\"janusgraph:Geoshape\",\"@value\":{\"type\":\"Point\", \
                            \"coordinates\":[{\"@type\":\"g:Double\",\"@value\":" + str(self.latitude) + "},\
                            {\"@type\":\"g:Double\",\"@value\":" + str(self.longitude) + "}]}}"

        actualGson = json.loads(graphSON)

        expectedGson = json.loads(expectedJSONStr)

        self.assertEqual(actualGson, expectedGson)

        pass
