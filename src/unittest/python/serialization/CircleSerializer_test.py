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

from janusgraph_python.core.datatypes.Circle import Circle
from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter


class TestCircleSerialization(unittest.TestCase):

    def test_circle_serialization(self):
        latitude = 80
        longitude = 100
        radius = 5

        circle = Circle(latitude, longitude, radius)

        writer = JanusGraphSONWriter().build()

        graphSON = writer.writeObject(circle)

        expectedJSON = dict()
        expectedJSON["@type"] = "janusgraph:Geoshape"
        expectedJSON["@value"] = dict()
        expectedJSON["@value"]["geometry"] = dict()
        expectedJSON["@value"]["geometry"]["type"] = "Circle"
        expectedJSON["@value"]["geometry"]["coordinates"] = list()
        expectedJSON["@value"]["geometry"]["coordinates"].append({"@type": "g:Double", "@value": float(longitude)})
        expectedJSON["@value"]["geometry"]["coordinates"].append({"@type": "g:Double", "@value": float(latitude)})
        expectedJSON["@value"]["geometry"]["radius"] = dict()
        expectedJSON["@value"]["geometry"]["radius"]["@type"] = "g:Double"
        expectedJSON["@value"]["geometry"]["radius"]["@value"] = radius
        expectedJSON["@value"]["geometry"]["properties"] = {"radius_units": "km"}

        actualGson = json.loads(graphSON)

        self.assertEqual(actualGson, expectedJSON)
