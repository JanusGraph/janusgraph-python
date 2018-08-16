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

from .Point import Point
from .Circle import Circle


class GeoShape(object):
    """ This class is the wrapper class to declare JanusGraph Geoshapes. """

    @staticmethod
    def Point(latitude, longitude):
        """ This is wrapper method to call the actual Geographical Point class.

        Args:
            latitude (float): The latitude of Point
            longitude (float): The longitude of Point

        Returns:
            Point
        """

        return Point(latitude, longitude)

    @staticmethod
    def Circle(latitude, longitude, radiusInKM):
        """ This is wrapper method to call the actual Geographical Circle class.

        Args:
            latitude (float): The latitude of Circle center
            longitude (float): The longitude of Circle center
            radiusInKM (int): The radius, in Kilometers of Circle

        Returns:
            Circle
        """

        return Circle(latitude, longitude, radiusInKM)
