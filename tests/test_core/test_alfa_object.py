from aioalfacrm.core import AlfaObject
from aioalfacrm.fields import Integer


class TestClass(AlfaObject):
    field1 = Integer()
    field2 = Integer(alias='field2_alias')
    field3 = Integer(default=10)
    field4 = Integer()


def test_init_alfa_object():
    a = TestClass(
        field1=1,
        field2=2,
        field4=None,
    )
    assert a.values == {'field1': 1, 'field2': 2, 'field3': 10, 'field4': None}
    assert a.props_aliases == {'field1': 'field1', 'field2': 'field2_alias', 'field3': 'field3', 'field4': 'field4'}


def test_alfa_object_serialize():
    a = TestClass(
        field1=1,
        field2=2,
        field4=None
    )

    serialized_object = a.serialize()
    assert serialized_object == {'field1': 1, 'field2_alias': 2, 'field3': 10}
    assert (str(a) == str({'field1': 1, 'field2_alias': 2, 'field3': 10}))
    assert (repr(a) == str({'field1': 1, 'field2_alias': 2, 'field3': 10}))
