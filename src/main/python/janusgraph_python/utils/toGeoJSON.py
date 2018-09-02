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


class toGeoJSON(object):
    """
        Convert a GeoShape into Geo JSON so that JanusGraph can read it.
    """

    TYPE_KEY = "@type"
    VALUE_KEY = "@value"
    DATA_TYPE = "g:Double"

    def __init__(self, geoshape):
        """
            Initialize the GeoShape converter. Currently implements conversion only for Point and Circle class.

        Args:
            geoshape: The GeoShape object to convert.
        """

        self.shape = geoshape
        self.shapeStr = self.shape.getShape()

        self.geoJSON = dict()

        self.GEOMETRY = "geometry"
        self.GEOMETRY_TYPE = self.shapeStr.capitalize()
        pass

    def convert(self):
        """
            Convert into Geo JSON
        Returns:
            dict
        """

        if self.GEOMETRY_TYPE.lower() == "point":
            self.geoJSON["type"] = self.GEOMETRY_TYPE
            self.geoJSON["coordinates"] = list()

            coordinates = self.shape.getCoordinates()

            coordinateJSON = self.__serialize_coordinates_to_geo_json(coordinates)
            self.geoJSON["coordinates"] = coordinateJSON

        else:
            geometryData = dict()

            geometryData["type"] = self.GEOMETRY_TYPE
            geometryData["coordinates"] = list()

            coordinates = self.shape.getCoordinates()

            coordinateJSON = self.__serialize_coordinates_to_geo_json(coordinates)
            geometryData["coordinates"] = coordinateJSON

            radius = self.shape.getRadius()
            geometryData["radius"] = self.__serialize_radius_to_geo_json(radius)

            geometryData["properties"] = dict()
            geometryData["properties"]["radius_units"] = "km"

            self.geoJSON["geometry"] = geometryData

        return self.geoJSON

    def __serialize_radius_to_geo_json(self, radius):
        radiusJSON = dict()
        radiusJSON[self.TYPE_KEY] = self.DATA_TYPE
        radiusJSON[self.VALUE_KEY] = radius
        return radiusJSON

    def __serialize_coordinates_to_geo_json(self, coordinates):
        coordinateJSON = list()

        for i in range(len(coordinates)):
            crdJSON = dict()
            crdJSON[self.TYPE_KEY] = self.DATA_TYPE
            crdJSON[self.VALUE_KEY] = coordinates[i]

            coordinateJSON.append(crdJSON)

        return coordinateJSON
