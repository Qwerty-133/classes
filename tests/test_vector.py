import math
from .context import Vector


def tests():
    assert Vector(90, 90).angle() / math.pi == 0.25
    assert Vector(-45, 45) * 2 == Vector(-90, 90)
    assert abs(Vector(3, 4)) == 5
    assert -Vector(20, 30) == Vector(-20, -30)
    assert bool(Vector(20, 30))
    assert not bool(Vector())
    assert repr(Vector(20, 30)) == 'Vector(x=20, y=30)'
    assert format(Vector(20, 30), '05') == '(00020, 00030)'
    assert format(Vector(12, 13), '.1fp') == '<17.7, 0.7>'
    assert complex(Vector(20, 30)) == 20 + 30j
