# Copyright 2023 JanusGraph-Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pytest import mark, param, raises
from janusgraph_python.process.traversal import RelationIdentifier, _JanusGraphP, Text

class TestRelationIdentifier(object):

    def test_invalid_string_relation_id_to_string(self):
        relation_id = '4qp-360'

        with raises(ValueError) as exception_info:
            RelationIdentifier.from_string(relation_id)

        assert str(exception_info.value) == 'Not a valid relation identifier: 4qp-360'

    @mark.parametrize(
        'relation_id',
        [
            param('4qp-360-7x1-3aw', id='valid relation ID'),
            param('4qp-Sout_vertex_id-7x1-Sin_vertex_id', id='valid relation ID with string IDs')
        ]
    )
    def test_string_relation_id_to_string(self, relation_id):
        relation_identifier = RelationIdentifier.from_string(relation_id)

        assert relation_id == str(relation_identifier)

    @mark.parametrize(
        'relation_id_str,out_vertex_id,type_id,relation_id,in_vertex_id',
        [
            param(
                '4qp-360-7x1-3aw',
                4104,
                10261,
                6145,
                4280,
                id='valid relation ID'
            ),
            param(
                '4qp-Sout_vertex_id-7x1-Sin_vertex_id',
                'out_vertex_id',
                10261,
                6145,
                'in_vertex_id',
                id='valid relation ID with string IDs'
            )
        ]
    )
    def test_string_relation_id_to_ids(self, relation_id_str, out_vertex_id, type_id, relation_id, in_vertex_id):
        relation_identifier = RelationIdentifier.from_string(relation_id_str)

        assert out_vertex_id == relation_identifier.out_vertex_id
        assert type_id == relation_identifier.type_id
        assert relation_id == relation_identifier.relation_id
        assert in_vertex_id == relation_identifier.in_vertex_id

    @mark.parametrize(
        'out_vertex_id,type_id,relation_id,in_vertex_id,relation_id_str',
        [
            param(
                4104,
                10261,
                6145,
                4280,
                '4qp-360-7x1-3aw',
                id='valid relation id'
            ),
            param(
                4104,
                10261,
                6145,
                None,
                '4qp-360-7x1',
                id='valid relation id without in-vertex ID'
            ),
            param(
                'out_vertex_id',
                10261,
                6145,
                'in_vertex_id',
                '4qp-Sout_vertex_id-7x1-Sin_vertex_id',
                id='valid relation ID with string IDs'
            ),
            param(
                'out_vertex_id',
                10261,
                6145,
                None,
                '4qp-Sout_vertex_id-7x1',
                id='valid relation ID with string IDs without in-vertex ID'
            )
        ]
    )
    def test_relation_id_to_string(self, out_vertex_id, type_id, relation_id, in_vertex_id, relation_id_str,):
        relation_identifier = RelationIdentifier.from_ids(out_vertex_id, type_id, relation_id, in_vertex_id)

        assert relation_id_str == relation_identifier.string_representation
        assert relation_id_str == str(relation_identifier)

    @mark.parametrize(
        'relation_id',
        [
            param('4qp-360-7x1-3aw', id='valid relation ID'),
            param('4qp-Sout_vertex_id-7x1-Sin_vertex_id', id='valid relation ID with string IDs')
        ]
    )
    def test_relation_id_hash(self, relation_id):
        relation_identifier = RelationIdentifier.from_string(relation_id)

        assert hash(relation_id) == hash(relation_identifier)

    @mark.parametrize(
        'relation_id,other_relation_id,expected_result',
        [
            param('4qp-360-7x1-3aw', None, False, id='compare to None'),
            param('4qp-360-7x1-3aw', 'self', True, id='compare to self'),
            param('4qp-360-7x1-3aw', '4qp-360-7x1-3aw', True, id='compare to other equal'),
            param('4qp-360-7x1-3aw', '36j-6hk-2dx-3a0', False, id='compare to other non-equal'),
        ]
    )
    def test_relation_id_equals(self, relation_id, other_relation_id, expected_result):
        other_relation_identifier = None
        relation_identifier = RelationIdentifier.from_string(relation_id)

        if other_relation_id:
            if other_relation_id == 'self':
                other_relation_identifier = relation_identifier
            else:
                other_relation_identifier = RelationIdentifier.from_string(other_relation_id)

        result = (relation_identifier == other_relation_identifier)

        assert result == expected_result

class TestJanusGraphP(object):

    @mark.parametrize(
        'predicate1,predicate2,expected',
        [
            param(
                _JanusGraphP('textContains', 'John'),
                _JanusGraphP('textContains', 'John'),
                True,
                id='both operators and values are equal'
            ),
            param(
                _JanusGraphP('textContains', 'John'),
                _JanusGraphP('textContains', 'Juhn'),
                False,
                id='both operators are equals but values differ'
            ),
            param(
                _JanusGraphP('textContains', 'John'),
                _JanusGraphP('textFuzzy', 'John'),
                False,
                id='both values are equals but operators differ'
            ),
            param(
                _JanusGraphP('textContains', 'John'),
                _JanusGraphP('textFuzzy', 'Juhn'),
                False,
                id='both values and operators differ'
            )
        ]
    )
    def test_JanusGraphP_eq(self, predicate1, predicate2, expected):
        result = predicate1 == predicate2
        assert result == expected

    @mark.parametrize(
        'expression,expected',
        [
            param(
                _JanusGraphP('textContains', 'John').and_(_JanusGraphP('textFuzzy', 'John')),
                'and(textContains(John),textFuzzy(John))',
                id='order of operations with and'
            ),
            param(
                (
                    _JanusGraphP('textContains', 'John').
                    or_(_JanusGraphP('textFuzzy', 'John')).
                    and_(_JanusGraphP('textPrefix', 'John'))
                ),
                'and(or(textContains(John),textFuzzy(John)),textPrefix(John))',
                id='order of operations with and/or'
            ),
            param(
                (
                    _JanusGraphP('textContains', 'John').
                    or_(_JanusGraphP('textFuzzy', 'John')).
                    and_(
                        _JanusGraphP('textPrefix', 'John').
                        or_(_JanusGraphP('textRegex', '.*hn.*'))
                    )
                ),
                'and(or(textContains(John),textFuzzy(John)),or(textPrefix(John),textRegex(.*hn.*)))',
                id='order of operations with multiple and/or'
            )
        ]
    )
    def test_JanusGraphP(self, expression, expected):
        assert str(expression) == expected

class TestText(object):

    @mark.parametrize(
        'predicate,expected',
        [
            param(Text.text_contains('John'), 'textContains(John)', id='text_contains'),
            param(Text.text_contains_prefix('John'), 'textContainsPrefix(John)', id='text_contains_prefix'),
            param(Text.text_contains_fuzzy('Juhn'), 'textContainsFuzzy(Juhn)', id='text_contains_fuzzy'),
            param(Text.text_contains_regex('.*hn.*'), 'textContainsRegex(.*hn.*)', id='text_contains_regex'),
            param(Text.text_fuzzy('Juhn'), 'textFuzzy(Juhn)', id='text_fuzzy'),
            param(Text.text_prefix('John'), 'textPrefix(John)', id='text_prefix'),
            param(Text.text_regex('.*hn.*'), 'textRegex(.*hn.*)', id='text_regex'),
        ]
    )
    def test_Text(self, predicate, expected):
        assert str(predicate) == expected