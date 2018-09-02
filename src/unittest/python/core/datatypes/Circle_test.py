# Name: Debasish Kanhar

import unittest

from janusgraph_python.core.datatypes.GeoShape import GeoShape


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.latitude = 85.9
        self.longitude = 171.2
        self.radius = 5

        self.circle = GeoShape.Circle(self.longitude, self.latitude, self.radius)

        pass

    """
    This method is used to unit test when Invalid coordinates/radius are passed to Circle class.
    """
    def test_invalid_circle(self):
        latitude = 95.9
        longitude = 181.2
        radius = 0

        with self.assertRaises(ValueError):
            GeoShape.Circle(longitude, latitude, radius)
        pass

    """
    This method is used to unit test when Valid coordinates are passed to Circle class.
    """
    def test_valid_circle(self):

        cr = self.circle

        circle_representation = "CIRCLE(lat: {}, lon: {}, r: {})".format(self.latitude, self.longitude, self.radius)

        assert circle_representation == cr.toString()
        pass

    """
    This method is used to unit test equality and non equality of 2 Circle classes defined by __eq__ and __ne__ methods.
    """
    def test_circle_equality(self):
        lat1 = 80.1
        lon1 = 160.2
        r = 5

        cr1 = self.circle
        cr2 = self.circle
        cr3 = GeoShape.Circle(lon1, lat1, r)
        cr4 = None

        self.assertEqual(cr1, cr2)
        self.assertNotEqual(cr1, cr3)
        self.assertNotEqual(cr1, cr4)
        pass

    """
    This method is used to unit test, once Circle objects are created, it can return valid and correct coordinates.
    """
    def test_coordinate_retrival(self):
        cr1 = self.circle

        self.assertEqual(self.latitude, cr1.getLatitude())
        self.assertEqual(self.longitude, cr1.getLongitude())
        self.assertEqual(self.radius, cr1.getRadius())
        self.assertEqual([self.latitude, self.longitude], cr1.getCoordinates())
        pass

    """
    This method is used to unit test the Shape of Object being created.
    """
    def test_shape(self):

        cr1 = self.circle

        self.assertEqual("CIRCLE", cr1.getShape())
        pass
