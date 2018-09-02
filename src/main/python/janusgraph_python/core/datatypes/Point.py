"""
Copyright 2018 Debasish Kanhar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Debasish Kanhar (https://github.com/debasishdebs)"
__credits__ = ["Florian Hockman", "Marko Rodriguez"]
__license__ = "Apache-2.0"
__version__ = "0.0.1"
__email__ = ["d.kanhar@gmail.com", "dekanhar@in.ibm.com"]


class Point(object):
    def __init__(self, longitude, latitude):
        """
            The actual class representing Geographical Point/Geometrical Point.
        Args:
            latitude (float): The latitude of Point
            longitude (float): The longitude of Point
        """
        self.latitude = float(latitude) * 1.0
        self.longitude = float(longitude) * 1.0

        status = self.__are_valid_coordinates()

        if status:
            pass
        else:
            raise ValueError("Invalid Coordinates passed. "
                             "Latitude needs to be b/w [-90, 90] and Longitude b/w [-180, 180]")
        pass

    def getShape(self):
        """
            Returns the shape of Geometrical object
        Returns:
            str
        """

        return "POINT"

    def getLatitude(self):
        """
            Get the latitude of Point
        Returns:
            float
        """
        return self.latitude

    def getLongitude(self):
        """
            Get the longitude of Point
        Returns:
            float
        """
        return self.longitude

    def getCoordinates(self):
        """
            Get the coordinates of Point
        Returns:
            list
        """
        return [self.latitude, self.longitude]

    def __are_valid_coordinates(self):
        """
            Test for validity for Coordinates being passed.
        Returns:
            bool
        """
        if (-90 <= self.getLatitude() <= 90) and (-180 <= self.getLongitude() <= 180):
            return True
        else:
            return False

    def __eq__(self, other):
        """
            Overrides the defauls class equality method.
            This checks if 2 Geometrical Point classes/objects are equal or not.
        Args:
            other (Point):

        Returns:
            bool
        """

        if type(other) is str:
            if other == self.toString():
                return True

        elif type(other) is Point:
            if (other.getLatitude()).__eq__(self.getLatitude()) and \
                    (other.getLongitude()).__eq__(self.getLongitude()):
                return True
            else:
                return False

        elif other is None:
            return False

        else:
            return False

        # if other is None:
        #     return False
        # else:
        #     if other.getShape() == self.getShape():
        #         pass
        #     else:
        #         return False
        #
        #     if (other.getLatitude()).__eq__(self.getLatitude()) and \
        #             (other.getLongitude()).__eq__(self.getLongitude()):
        #         return True
        #     else:
        #         return False

    def __str__(self):
        return self.toString()

    def __ne__(self, other):
        return not self.__eq__(other)

    def toString(self):
        """
            Returns the String representation of Geometrical Point
        Returns:
            str
        """
        point = "POINT(lat: {}, lon: {})".format(self.getLatitude(), self.getLongitude())
        return point
