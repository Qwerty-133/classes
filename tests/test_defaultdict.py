import pytest
from .context import defaultdict_


def test_default_dict():
    with pytest.raises(TypeError, match='first argument'):
        defaultdict_([(1, 2), (3, 4)])

    assert str(defaultdict_() == repr(defaultdict_()) ==
               'defaultdict_(None, {})')

    assert defaultdict_(int, [(1, 2), (3, 4)], four=20, five=50) == {
        1: 2, 3: 4, 'four': 20, 'five': 50
    }

    b = defaultdict_(int, [(1, 2), (3, 4)])

    assert b[2] + 3 == 3

    b = defaultdict_()

    with pytest.raises(KeyError, match='2'):
        b[2] + 3

    b = defaultdict_(lambda: 1 + '', [(1, 2), (3, 4)])

    with pytest.raises(TypeError, match='unsupported operand'):
        b[2]
