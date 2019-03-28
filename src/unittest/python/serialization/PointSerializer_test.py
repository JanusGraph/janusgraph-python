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

from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter


class TestPointSerialization(unittest.TestCase):

    def test_point_serialization(self):
        latitude = 80
        longitude = 100

        point = Point(latitude, longitude)

        writer = JanusGraphSONWriter().build()

        graphSON = writer.writeObject(point)

        expectedJSON = dict()
        expectedJSON["@type"] = "janusgraph:Geoshape"
        expectedJSON["@value"] = dict()
        expectedJSON["@value"]["type"] = "Point"
        expectedJSON["@value"]["coordinates"] = list()
        expectedJSON["@value"]["coordinates"].append({"@type": "g:Double", "@value": float(longitude)})
        expectedJSON["@value"]["coordinates"].append({"@type": "g:Double", "@value": float(latitude)})

        actualGson = json.loads(graphSON)

        self.assertEqual(actualGson, expectedJSON)
