import numpy as np
from re import match
from typing import Iterable, SupportsFloat

def expected_type(t : type, expected : Iterable[type]) -> TypeError:
    """
    A wrapper for generating type errors.
    @param t: the wrong type got.
    @param expected: an iterable, preferably a tuple, of the expected types
    to display.
    """
    expected_string = ''
    for i, cls in enumerate(expected):
        if i == len(expected) - 1 and len(expected) > 1:
            expected_string += ' or'
        expected_string += ' ' + cls.__name__
        if i > 0 and i < len(expected) -1:
            expected_string += ','
    return TypeError(f'Expected{expected_string}, got instead {t.__name__!r}')

class RGBAColor:

    def __init__(self, color_int : int) -> None:
        self._int = color_int & 0xffffffff
    
    ### REPRESENTATION
    def __str__(self):
        return self.as_hex_color

    def __repr__(self):
        return f'<RGBA{self.to_rgba_tuple} {self.to_hex_color}>'

    ### CONSTRUCTORS
    @classmethod
    def from_hex_color(cls, hex_color):
        if not match(r'^#([0-9a-f]{6})$', hex_color):
            raise ValueError(f'Hex colors expected in the form: #RRGGBB')
        else:
            return cls(int(hex_color[1:], 16))

    @classmethod
    def from_array(cls, arr):
        if len(arr) not in  (3, 4):
            raise ValueError('Expected an array of length 3 or 4')
       obj = cls(0)
       obj.red = arr[0]
       obj.green = arr[1]
       obj.blue = arr[2]
       if len(arr) == 4:
           obj.alpha = arr[3]
       return obj
    ### PROPERTIES

    #### Other useful forms of the color

    @property
    def toarray(self):
        return np.array([ self.red, self.green, self.blue, self.alpha ])
    @property
    def toarray_noalpha(self):
        return self.toarray[:-1]

    @property
    def to_hex_color(self):
        return '#' + hex(self._int)[2:].rjust(6, '0')

    @property
    def to_rgba_tuple(self):
        return self.red, self.green, self.blue, self.alpha



    #### Available properties

    @property
    def red(self) -> int:
        """
        The red part of the RGBA color.
        """
        return (self._int & 0xff0000) >> 16

    @red.setter
    def red(self, val : SupportsFloat) -> None:
        """
        Sets the red part of the RGBA color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            val = val & 0xff
            self._int &= ~ 0xff0000
            self._int |= val << 16
        elif type(val) == float:
            self.red = int(val * 255)
        else:
            raise expected_type(type(val), (int, float))

    @property
    def green(self) -> int:
        """
        The green part of the RGBA color.
        """
        return (self._int & 0xff00) >> 8

    @green.setter
    def green(self, val : SupportsFloat) -> None:
        """
        Sets the green value of the color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            val &= 0xff
            self._int &= ~ 0xff00
            self._int |= val << 8
        elif type(val) == float:
            self.green = int(val * 255)

        else:
            raise expected_type(type(val), (int, float))

    @property
    def blue(self) -> int:
        """
        The blue part of the color.
        """
        return self._int & 0xff

    @blue.setter
    def blue(self, val : SupportsFloat) -> None:
        """
        Sets the blue value of the color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            self._int &= ~ 0xff
            self._int |= (val & 0xff)
        elif type(val) == float:
            self.blue = int(val * 255)
        else:
            raise expected_type(type(val), (int, float))

    @property
    def alpha(self) -> int:
        """
        Alpha value of the RGBA color.
        """
        return (self._int & 0xff000000) >> 24
    @alpha.setter
    def alpha(self, val : SupportsFloat) -> None:
        """
        Sets the Alpha value of the RGBA color.
        @param val: either an integer in the range
        0-255 (will be cut to the first byte) or a 
        float in the range 0.0-1.0.
        """
        if type(val) == int:
            self._int &= ~ 0xff000000
            self._int |= (val & 0xff) << 24
        elif type(val) == float:
            self.alpha = int(val * 255)

        







