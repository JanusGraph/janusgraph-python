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


class Point(object):
    """ The Class representation of JanusGraph GeoShape Point. """
    def __init__(self, latitude, longitude):
        """ Creates a GeoShape Point with given latitude & longitude.

        Args:
            latitude (float): The latitude of Point
            longitude (float): The longitude of Point
        """
        self.__latitude = float(latitude) * 1.0
        self.__longitude = float(longitude) * 1.0

        if not self.__are_coordinates_valid():
            raise ValueError("Invalid Coordinates passed. "
                             "Latitude needs to be b/w [-90, 90] and Longitude b/w [-180, 180]")
    @staticmethod
    def getShape():
        """ Returns the shape of Geometrical object

        Returns:
            str
        """

        return "POINT"

    def getLatitude(self):
        """ Get the latitude of Point

        Returns:
            float
        """
        return self.__latitude

    def getLongitude(self):
        """ Get the longitude of Point

        Returns:
            float
        """
        return self.__longitude

    def getCoordinates(self):
        """ Get the coordinates of Point

        Returns:
            list
        """
        return [self.__latitude, self.__longitude]

    def __are_coordinates_valid(self):
        """ Test for validity for Coordinates being passed.

        Returns:
            bool
        """

        return abs(self.getLatitude()) <= 90.0 and abs(self.getLongitude()) <= 180.0

    def __key(self):
        return tuple(self.getCoordinates())

    def __eq__(self, other):
        """
            Overrides the default class equality method.
            This checks if 2 Geometrical Point classes/objects are equal or not.
        Args:
            other (Point):

        Returns:
            bool
        """

        return isinstance(self, type(other)) and self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def __str__(self):
        return "POINT(lat: {}, lon: {})".format(self.getLatitude(), self.getLongitude())

    def __ne__(self, other):
        return not self.__eq__(other)
