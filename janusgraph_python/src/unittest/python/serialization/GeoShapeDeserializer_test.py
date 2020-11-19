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
from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.core.datatypes.Circle import Circle


class TestGeoShapeDeserializer(unittest.TestCase):

    def test_point_deserialization(self):
        latitude = 80.0
        longitude = 100.0

        reader = JanusGraphSONReader().build()

        pointJSON = dict()
        pointJSON["@type"] = "janusgraph:Geoshape"
        pointJSON["@value"] = {"coordinates": [longitude, latitude]}

        expectedPoint = reader.toObject(pointJSON)

        actualPoint = Point(latitude, longitude)

        self.assertEqual(expectedPoint, actualPoint.__str__())

    def test_circle_deserialization(self):
        latitude = 80.0
        longitude = 100.0
        radius = 5

        reader = JanusGraphSONReader().build()

        circleJSON = dict()
        circleJSON["@type"] = "janusgraph:Geoshape"
        circleJSON["@value"] = dict()
        circleJSON["@value"]["geometry"] = dict()
        circleJSON["@value"]["geometry"]["@type"] = "g:Map"
        circleJSON["@value"]["geometry"]["@value"] = list()
        circleJSON["@value"]["geometry"]["@value"].append("type")
        circleJSON["@value"]["geometry"]["@value"].append("Circle")
        circleJSON["@value"]["geometry"]["@value"].append("coordinates")
        coordinates = dict()
        coordinates["@type"] = "g:List"
        coordinates["@value"] = list()
        coordinates["@value"].append({"@type": "g:Double", "@value": longitude})
        coordinates["@value"].append({"@type": "g:Int32", "@value": latitude})
        circleJSON["@value"]["geometry"]["@value"].append(coordinates)
        circleJSON["@value"]["geometry"]["@value"].append("radius")
        circleJSON["@value"]["geometry"]["@value"].append({"@type": "g:Double", "@value": radius})
        circleJSON["@value"]["geometry"]["@value"].append("properties")
        circleJSON["@value"]["geometry"]["@value"].append({"@type": "g:Map", "@value": ["radius_units", "km"]})

        expectedCircle = reader.toObject(circleJSON)

        actualCircle = Circle(latitude, longitude, radius)

        self.assertEqual(expectedCircle, actualCircle.__str__())
