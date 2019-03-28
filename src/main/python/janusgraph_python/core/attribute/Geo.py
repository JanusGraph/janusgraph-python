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

from gremlin_python.process.traversal import P


class Geo(object):
    """
    This class implements all the JanusGraph-based Geo Predicates.
    """

    @staticmethod
    def geoContains(value):
        """ The method is used for JanusGraph geoContains predicate.

        GeoContains predicate holds true when one object is contained by another. The query returns the GeoShapes
        which contains the GeoShape being passed/queried.

        Args:
            value (GeoShape): The GeoShape to query for and return all results which are present inside this GeoShape

        Returns:
            bool: Returns true iff the GeoShape contains the value being queried
        """

        return P("geoContains", value)

    @staticmethod
    def geoWithin(value):
        """ The method is used for JanusGraph geoWithin predicate.

        GeoWithin predicate holds true when one object is within another. The query returns the GeoShapes which are
        present inside/within the GeoShape being passed/queried.

        Args:
            value (GeoShape): The GeoShape to query for and return all results within this this GeoShape if present.

        Returns:
            bool: Returns true iff the GeoShape is within the value being queried
        """

        return P("geoWithin", value)
