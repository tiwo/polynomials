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



Copyright
=========

Copyright (c) 2012 by tiwo.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
