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


class Circle(object):

    """ The Class representation of JanusGraph GeoShape Circle."""

    def __init__(self, latitude, longitude, radiusInKM):
        """
            Creates a GeoShape Circle with given latitude, longitude and radius in KMs.

        Args:
            latitude (float): The latitude of circle's center.
            longitude (float): The longitude of circle's center
            radiusInKM (int): The radius of circle in KM.
        """

        self.__latitude = float(latitude) * 1.0
        self.__longitude = float(longitude) * 1.0
        self.__radius = radiusInKM

        if not self.__are_coordinates_valid():
            raise ValueError("Invalid Coordinates/Radius passed. "
                             "Latitude needs to be b/w [-90, 90] and Longitude b/w [-180, 180] and Radius > 0")

    @staticmethod
    def getShape():
        """ Return the Shape of Geometrical shape

        Returns:
            str
        """
        return "CIRCLE"

    def getLatitude(self):
        """ Get latitude of Circle center.

        Returns:
            float
        """
        return self.__latitude

    def getLongitude(self):
        """ Get longitude of circle center.

        Returns:
            float
        """
        return self.__longitude

    def getCoordinates(self):
        """ Get the coordinates of circle center

        Returns:
            list
        """
        return [self.__latitude, self.__longitude]

    def getRadius(self):
        """ Get the radius of circle

        Returns:
            int
        """
        return self.__radius

    def __are_coordinates_valid(self):
        """ Check for validity of coordinates passed to object in creation time.

        Returns:
            bool
        """

        return abs(self.getLatitude()) <= 90.0 and abs(self.getLongitude()) <= 180.0 and self.getRadius() > 0

    def __key(self):
        return tuple([self.getLatitude(), self.getLongitude(), self.getRadius()])

    def __eq__(self, other):
        """ Overrides default class equality method.

        Args:
            other (Circle): The other object to compare against.

        Returns:
            bool
        """

        return isinstance(self, type(other)) and self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "CIRCLE(lat: {}, lon: {}, r: {})".format(self.getLatitude(), self.getLongitude(), self.getRadius())
