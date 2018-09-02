# Name: Debasish Kanhar

import unittest

from janusgraph_python.core.datatypes.GeoShape import GeoShape


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.latitude = 85.9
        self.longitude = 171.2

        self.point = GeoShape.Point(self.longitude, self.latitude)

        pass

    """
    This method is used to unit test when Invalid coordinates are passed to Point class.
    """
    def test_invalid_point(self):
        latitude = 95.9
        longitude = 181.2

        with self.assertRaises(ValueError):
            GeoShape.Point(longitude, latitude)
        pass

    """
    This method is used to unit test when Valid coordinates are passed to Point class. 
    """
    def test_valid_point(self):

        pt = self.point

        point_representation = "POINT(lat: {}, lon: {})".format(self.latitude, self.longitude)

        assert point_representation == pt.toString()
        pass

    """
    This method is used to unit test equality and non equality of 2 Point classes defined by __eq__ and __ne__ methods. 
    """
    def test_point_equality(self):
        lat1 = 80.1
        lon1 = 160.2

        p1 = self.point
        p2 = self.point
        p3 = GeoShape.Point(lon1, lat1)

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        pass

    """
    This method is used to unit test, once Point objects are created, it can return valid and correct coordinates.
    """
    def test_coordinate_retrival(self):
        p1 = self.point

        self.assertEqual(self.latitude, p1.getLatitude())
        self.assertEqual(self.longitude, p1.getLongitude())
        self.assertEqual([self.latitude, self.longitude], p1.getCoordinates())
        pass

    """
    This method is used to unit test the Shape of Object being created.
    """
    def test_shape(self):

        p1 = self.point

        self.assertEqual("POINT", p1.getShape())
        pass
