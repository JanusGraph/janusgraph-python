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


from ..core.datatypes.GeoShape import Circle, Point
from ..core.datatypes import GeoShape


class GeoShapeDeserializer(object):
    """
    This class is used to De-serialize any GeoShape objects being returned from Gremlin Server.
    """
    VALUE_KEY = "@value"

    @classmethod
    def objectify(cls, graphsonObj, reader):
        """
            The De-serializer method to de-serialize a GeoShape into corresponding Python GeoShape object.

        Args:
            graphsonObj (dict): The serialized JSON returned from JanusGraph's gremlin-server.
            reader : The reader class to use for de-serializing the GeoShape object.

        Returns:
            GeoShape
        """

        if graphsonObj.get("geometry") is not None:
            # Its a Geometry object
            geometryData = graphsonObj["geometry"]
            geometryDataValue = geometryData[cls.VALUE_KEY]

            val = iter(geometryDataValue)
            geometryDataValue = dict(zip(val, val))

            if "coordinates" in geometryDataValue and isinstance(geometryDataValue["coordinates"][cls.VALUE_KEY], list):
                coordinates = geometryDataValue["coordinates"][cls.VALUE_KEY]
                shape = geometryDataValue["type"]
                radius = geometryDataValue["radius"][cls.VALUE_KEY]
                radiusUnits = geometryDataValue["properties"][cls.VALUE_KEY][1]

                if len(coordinates) >= 2:

                    if shape.lower() == "circle":
                        if radiusUnits:
                            if radiusUnits.lower() == "km":
                                radius = radius
                            elif radiusUnits.lower() == "m":
                                radius = 0.001 * radius
                            else:
                                raise NotImplementedError("Current JanusGraph python serializers can only \
                                                            understand Radius units in KM and Mts.")
                            pass
                        else:
                            radius = radius
                            pass

                        circle = cls.__deserialize_circle_from_coordinates(coordinates, radius)

                        return circle.toString()

                    else:
                        raise NotImplementedError("Currently implemented De-serialization \
                                                        for Geometry shapes CIRCLE and POINT.")

                else:
                    raise AttributeError("Invalid GeoShape parameters passed. Co-ordinates need to be > 2")
            else:
                raise ValueError("Invalid GeoShape passed.")
        else:
            # It is point
            coordinates = graphsonObj["coordinates"]
            point = cls.__deserialize_points_from_coordinates(coordinates)

            return point.toString()

    @classmethod
    def __deserialize_points_from_coordinates(cls, coordinates):
        """
            De-serializes coordinates json into list of coordinates so that GeoShape Point object

        Args:
            coordinates (list): The co-ordinates to be used to generate a Point object

        Returns:
            Point
        """

        coordList = list(coordinates)
        coordList = [float(x) for x in coordList]

        point = cls.__get_point_from_coordinates(coordList)

        return point

    @classmethod
    def __get_point_from_coordinates(cls, coordinates):
        """
            De-serializes Point object from co-ordinates

        Args:
            coordinates (list):

        Returns:
            Point
        """

        latitude = coordinates[0]
        longitude = coordinates[1]

        pt = GeoShape.Point(longitude, latitude)

        return pt

    @classmethod
    def __deserialize_circle_from_coordinates(cls, coordinates, radius):
        """
            De-serializes coordinates json into list of coordinates and radius, so that a Circle object can be created.

        Args:
            coordinates (list):

        Returns:
            Circle
        """

        coordList = list(coordinates)
        coordList = [x[cls.VALUE_KEY] for x in coordList]
        radius = int(radius)

        circle = cls.__get_circle_from_coordinates(coordList, radius)

        return circle

    @classmethod
    def __get_circle_from_coordinates(cls, coordinates, radius):
        """
            Create Circle object from Co-ordinates and radius.

        Args:
            coordinates (list):
            radius (int):

        Returns:
            Circle
        """

        latitude = coordinates[0]
        longitude = coordinates[1]

        cr = GeoShape.Circle(longitude, latitude, radius)

        return cr
