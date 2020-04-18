import numpy as np
from typing import Iterable

def expected_type(t : type, expected : Iterable[type]) -> TypeError:
    """
    A wrapper for generating type errors based on 
    """
    expected_string = ' '
    for i, cls in enumerate(expected):
        expected_string += ' ' + cls.__name__
        if i > 0 && i < len(expected) -1:
            expected_string += ','
        elif i == len(expected) - 1 and len(expected) > 1:
            expected_string += ' or'
    return TypeError(f'Expected {expected_string}, got instead {t.__name__!r}')

class RGBAColor:

    def __init__(self, color_int : int) -> None:
        self._int = color_int & 0xffffffff

    @property
    def red(self):
        """
        The red part of the RGBA color.
        """
        return (self._int & 0xff0000) >> 16

    @red.setter
    def red(self, val : int | float) -> :
        """
        Sets the red part of the RGBA color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            val = val & 0xff
            self._int &= not 0xff0000
            self._int |= val << 16
        elif type(val) == float:
            self.red = int(val * 255)
        else:
            raise expected_type(type(val), (int, float))

    @property
    def green(self):
        """
        The green part of the RGBA color.
        """
        return (self._int & 0xff00) >> 8

    @green.setter
    def green(self, val):
        """
        Sets the green value of the color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            val &= 0xff
            self._int &= not 0xff00
            self._int |= val << 8
        elif type(val) == float:
            self.green = int(val * 255)

        else:
            raise expected_type(type(val), (int, float))

    @property
    def blue(self):
        """
        The blue part of the color.
        """
        return self._int & 0xff

    @blue.setter
    def blue(self, val):
        """
        Sets the blue value of the color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            self._int &= not 0xff
            self._int |= (val & 0xff)
        elif type(val) == float:
            self.blue = int(val * 255)
        else:
            raise expected_type(type(val), (int, float))

    @property
    def alpha(self):
        """
        Alpha value of the RGBA color.
        """
        return (self._int & 0xff000000) >> 24
    @alpha.setter
    def alpha(self, val):
        """
        Sets the Alpha value of the RGBA color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            self._int &= not 0xff000000
            self._int |= (val & 0xff) << 24
        elif type(val) == float:
            self.alpha = int(val * 255)

        







