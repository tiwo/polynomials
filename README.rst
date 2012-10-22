Polynomials in Python
=====================

:Date: 2012-10-22
:Author: tiwo

This implements polynomials in Python.

Basic usage examples::

	>>> from polynomials import Polynomial, x

	>>> p = (x+1)**5
	>>> p
	Polynomial([1, 5, 10, 10, 5, 1])

Pretty printing (the representation will change in the future)::

	>>> print p
	1+5x+10x^2+10x^3+5x^4+x^5

