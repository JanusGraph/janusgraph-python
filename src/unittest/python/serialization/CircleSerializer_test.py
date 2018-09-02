# Name: Debasish Kanhar

import unittest
import json

from janusgraph_python.core.datatypes.Circle import Circle
from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter


class TestCircleSerialization(unittest.TestCase):

    def setUp(self):
        self.latitude = 80
        self.longitude = 100
        self.radius = 5

        self.circle = Circle(self.longitude, self.latitude, self.radius)

        self.writer = JanusGraphSONWriter().build()
        pass

    def test_circle_serialization(self):
        graphSON = self.writer.writeObject(self.circle)

        expectedJSONStr = "{\"@type\":\"janusgraph:Geoshape\",\"@value\":{\"geometry\":{\"type\":\"Circle\", \
                            \"coordinates\":[{\"@type\":\"g:Double\",\"@value\":" + str(self.latitude) + "},\
                            {\"@type\":\"g:Double\",\"@value\":" + str(self.longitude) + "}], \"radius\":{\"@type\":\"g:Double\",\
                            \"@value\":" + str(self.radius) + "},\"properties\":{\"radius_units\":\"km\"}}}}"

        actualGson = json.loads(graphSON)
        expectedGson = json.loads(expectedJSONStr)

        self.assertEqual(actualGson, expectedGson)

        pass
