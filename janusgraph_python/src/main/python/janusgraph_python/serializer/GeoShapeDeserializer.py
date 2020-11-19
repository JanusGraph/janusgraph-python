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

from ..core.datatypes import GeoShape


class GeoShapeDeserializer(object):
    """ DeSerialize any GeoShape objects returned from the Gremlin server. """
    VALUE_KEY = "@value"

    @classmethod
    def objectify(cls, graphsonObj, reader):
        """ The Deserializer method to de-serialize a GeoShape into corresponding Python GeoShape object.

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

                        else:
                            radius = radius

                        circle = cls.__deserialize_circle_from_coordinates(coordinates, radius)

                        return circle

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

            return point

    @classmethod
    def __deserialize_points_from_coordinates(cls, coordinates):
        """ Deserializes coordinates json into list of coordinates so that GeoShape Point object

        Args:
            coordinates (list): The co-ordinates to be used to generate a Point object

        Returns:
            Point
        """

        coordList = [float(coord) for coord in list(coordinates)]

        point = cls.__get_point_from_coordinates(coordList)

        return point

    @classmethod
    def __get_point_from_coordinates(cls, coordinates):
        """ Deserializes Point object from co-ordinates

        Args:
            coordinates (list):

        Returns:
            Point
        """

        latitude = coordinates[1]
        longitude = coordinates[0]

        point = GeoShape.Point(latitude, longitude)

        return point

    @classmethod
    def __deserialize_circle_from_coordinates(cls, coordinates, radius):
        """ Deserializes coordinates json into list of coordinates and radius, so that a Circle object can be created.

        Args:
            coordinates (list):

        Returns:
            Circle
        """

        coordList = [coord[cls.VALUE_KEY] for coord in list(coordinates)]
        radius = int(radius)

        circle = cls.__get_circle_from_coordinates(coordList, radius)

        return circle

    @classmethod
    def __get_circle_from_coordinates(cls, coordinates, radius):
        """ Create Circle object from Co-ordinates and radius.

        Args:
            coordinates (list):
            radius (int):

        Returns:
            Circle
        """

        latitude = coordinates[1]
        longitude = coordinates[0]

        circle = GeoShape.Circle(latitude, longitude, radius)

        return circle
