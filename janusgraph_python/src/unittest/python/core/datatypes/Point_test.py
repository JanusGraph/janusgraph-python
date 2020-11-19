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

from janusgraph_python.core.datatypes.GeoShape import GeoShape


class TestPoint(unittest.TestCase):

    def test_invalid_point(self):
        latitude = 95.9
        longitude = 181.2

        with self.assertRaises(ValueError):
            GeoShape.Point(latitude, longitude)

    def test_point_equality(self):
        lat1 = 80.1
        lon1 = 160.2

        latitude = 85.9
        longitude = 171.2

        p1 = GeoShape.Point(latitude, longitude)
        p2 = GeoShape.Point(latitude, longitude)
        p3 = GeoShape.Point(lat1, lon1)

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_coordinate_retrival(self):
        latitude = 85.9
        longitude = 171.2

        p1 = GeoShape.Point(latitude, longitude)

        self.assertEqual(latitude, p1.getLatitude())
        self.assertEqual(longitude, p1.getLongitude())
        self.assertEqual([latitude, longitude], p1.getCoordinates())

    def test_shape(self):
        latitude = 85.9
        longitude = 171.2

        p1 = GeoShape.Point(latitude, longitude)

        self.assertEqual("POINT", p1.getShape())
