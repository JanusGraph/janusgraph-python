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


try:
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
except ImportError:
    from gremlin_python.structure.io.graphson import GraphSONUtil

from ..core.datatypes.GeoShape import Point
from ..utils.toGeoJSON import toGeoJSON

import json


class PointSerializer(object):
    """
    Serialize a GeoShape Point object so that the same can be passed to Gremlin Server
    """

    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"

    @classmethod
    def dictify(cls, point, writer):
        """
        This is serializer method for Point class.

        Args:
            point (Point): The GeoShape Point class to serialize into.
            writer:

        Returns:
            json
        """

        geometryJSON = toGeoJSON(point).convert()

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, geometryJSON, cls.GRAPHSON_PREFIX)

        return serializedJSON
