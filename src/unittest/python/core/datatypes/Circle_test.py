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


class TestCircle(unittest.TestCase):

    def test_invalid_circle(self):
        latitude = 95.9
        longitude = 181.2
        radius = 0

        with self.assertRaises(ValueError):
            GeoShape.Circle(latitude, longitude, radius)

    def test_circle_equality(self):
        latitude = 85.9
        longitude = 171.2
        r = 5

        cr1 = GeoShape.Circle(latitude, longitude, r)
        cr2 = GeoShape.Circle(latitude, longitude, r)

        lat1 = 80.1
        lon1 = 160.2
        r = 5

        cr3 = GeoShape.Circle(lat1, lon1, r)
        cr4 = None

        self.assertEqual(cr1, cr2)
        self.assertNotEqual(cr1, cr3)
        self.assertNotEqual(cr1, cr4)

    def test_coordinate_retrival(self):
        latitude = 85.9
        longitude = 171.2
        radius = 5

        cr1 = GeoShape.Circle(latitude, longitude, radius)

        self.assertEqual(latitude, cr1.getLatitude())
        self.assertEqual(longitude, cr1.getLongitude())
        self.assertEqual(radius, cr1.getRadius())
        self.assertEqual([latitude, longitude], cr1.getCoordinates())

    def test_shape(self):
        latitude = 85.9
        longitude = 171.2
        radius = 5

        cr1 = GeoShape.Circle(latitude, longitude, radius)

        self.assertEqual("CIRCLE", cr1.getShape())
