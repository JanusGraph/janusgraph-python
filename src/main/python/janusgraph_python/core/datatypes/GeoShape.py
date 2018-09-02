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
__credits__ = ["Florian Hockman", "Jason Plurad", "Dave Brown", "Marko Rodriguez"]
__license__ = "Apache-2.0"
__version__ = "0.0.1"
__email__ = ["d.kanhar@gmail.com", "dekanhar@in.ibm.com"]


from .Point import Point
from .Circle import Circle


class GeoShape(object):
    """
    This class is the super class for all GeoShapes.
    """

    @staticmethod
    def Point(longitude, latitude):
        """
        This is wrapper method to call the actual Geographical Point class.

        Args:
            longitude (float): The longitude of Point
            latitude (float): The latitude of Point

        Returns:
            Point
        """

        point = Point(longitude, latitude)

        return point

    @staticmethod
    def Circle(longitude, latitude, radiusInKM):
        """
            This is wrapper method to call the actual Geographical Circle class.
        Args:
            longitude (float): The longitude of Circle center
            latitude (float): The latitude of Circle center
            radiusInKM (int): The radius, in Kilometers of Circle

        Returns:
            Circle
        """

        circle = Circle(longitude, latitude, radiusInKM)

        return circle
