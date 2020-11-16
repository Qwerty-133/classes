import numbers
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: float = 0
    y: float = 0
    _format_string = '({}, {})'

    def angle(self):
        return math.atan2(*self)

    def __iter__(self):
        yield self.x
        yield self.y

    def __mul__(self, other):
        if not isinstance(other, numbers.Number):
            return NotImplemented
        return Vector(*(coord * other for coord in self))

    def __rmul__(self, other):
        return other * self

    def __abs__(self):
        return math.hypot(*self)

    def __neg__(self):
        return Vector(*(-coord for coord in self))

    def __pos__(self):
        return Vector(*self)

    def __bool__(self):
        return bool(abs(self))

    def __str__(self):
        return self._format_string.format(*self)

    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            format_string = '<{}, {}>'
            coords = (abs(self), self.angle())
            format_spec = format_spec[:-1]
        else:
            format_string = self._format_string
            coords = tuple(self)

        return format_string.format(
            *(format(coord, format_spec) for coord in coords)
        )

    def __complex__(self):
        return complex(*self)
