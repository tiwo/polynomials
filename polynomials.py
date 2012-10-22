# Copyright (c) 2012 by tiwo.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
"""


    Examples::

        >>> p = Polynomial([1,2,3])

        >>> print p
        1+2x+3x^2
        >>> print -3*p
        -3-6x-9x^2

        >>> p == 1+2*x+3*x*x
        True

        >>> p(0), p(1), p(-1)  # evaluate at 0, 1, -1:
        (1, 6, 2)

        >>> print p(1+x)  # plug in 1+x for x, and evaluate:
        6+8x+3x^2

        >>> p == p(x)
        True

        >>> print (1+x)*(1-x)        
        1-x^2

"""

from __future__ import division

__all__ = ['Polynomial', 'x', 'lower_factorial']

def _coerce(something, to):

    if isinstance(something, to):
        return something

    if hasattr(something, '__iter__'):
        return to(something)

    return to([something])

class Polynomial(list):

    def __repr__(self):
        self.__cancel()
        return '%s([%s])' % (self.__class__.__name__,
                           ', '.join(repr(c) for c in self)
                          )

    def __cancel(self):
        try:
            while not self[-1]:
                self.pop()
        except IndexError:
            pass

    def __str__(self):
        """

        Examples:
            >>> Zero = 0*x
            >>> print Zero, 1+Zero,  Zero-1, 2+Zero, x, -x, 2*x, -3*x
            0 1 -1 2 x -x 2x -3x

        """
        self.__cancel()

        if not self:
            return '0'

        result = []
        for e, c in enumerate(self):
            if not c:
                continue

            if c == 1:
                if e == 0:
                    result.append('1')
                    continue
                elif result:
                    result.append('+')
                else:
                    pass

            elif c == -1:
                if e == 0:
                    result.append('-1')
                    continue
                else:
                    result.append('-')

            elif c > 0:
                if result:
                    result.append('+%s' % c)
                else:
                    result.append(str(c))
            else:
                assert c < 0
                result.append(str(c))

            if not e:
                continue
            elif e == 1:
                result.append('x')
            else:
                result.append('x^%s' % e)

        return ''.join(result)

    def degree(self):
        self.__cancel()
        if len(self) == 0:
            return float('-inf')
        return len(self) - 1

    def __nonzero__(self):
        self.__cancel()
        return 0 != len(self)

    def __eq__(self, other):
        return not (self - other)

    def __call__(self, x):
        self.__cancel()
        horner = lambda Previous, Next: Previous * x + Next
        return reduce(horner, reversed(self), 0) 

    def __neg__(self):
        return self.__class__(-c for c in self)

    def __getitem__(self, index):
        if index > len(self):
            return 0
        try:
            return list.__getitem__(self, index)
        except IndexError:
            return 0

    def __add__(self, other):
        other = _coerce(other, self.__class__)
    
        resulting_length = max(len(self), len(other))
        return Polynomial(self[i] + other[i]
            for i in range(resulting_length))

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        other = _coerce(other, self.__class__)      

        resulting_coeffs = [0] * (len(self) + len(other))
        for i, my_c in enumerate(self):
            for j, her_c in enumerate(other):
                resulting_coeffs[i+j] += my_c*her_c
        return Polynomial(resulting_coeffs)

    def __rmul__(self, other):
        return self*other

    def __pow__(self, e):
        """

        Example::
            >>> print (1 + x)**4
            1+4x+6x^2+4x^3+x^4
        """

        result = 1
        for k in range(e):
            result *= self
        return result

    def __sub__(self, other):
        return self + (-other)
        
    def __rsub__(self, other):
        return -(self - other)

    def derivative(self):
        resulting_coeffs = []
        for e, c in enumerate(self):
            resulting_coeffs.append(e*c)
        return self.__class__(resulting_coeffs[1:])

    def delta(self):
        return self(x+1) - self
            
        
x = Polynomial([0, 1])


def lower_factorial(n):
    """

        Examples::

            >>> print lower_factorial(1)
            x
            >>> print lower_factorial(2)
            -x+x^2
            >>> lower_factorial(4) == x*(x-1)*(x-2)*(x-3)
            True

            >>> lower_factorial(5).delta() == 5 * lower_factorial(4)
            True
    """
    result = 1
    for i in range(n):
        result *= x - i
    return result


if __name__ == '__main__':
    import sys
    import doctest
    sys.exit(min(255, doctest.testmod()[0]))
