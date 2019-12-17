Appendix B: The float Class
----------------------------

The `Python 3 Documentation
<http://docs.python.org/py3k>`_ site contains this and much more extensive documentation on the Python 3 language, including the `Library Reference 
<http://docs.python.org/py3k/library/index.html>`_ which contains this documentation. This appendix was generated from the Python help system by typing help(float) in the Python interpreter.

Help on class float in module builtins:

class float(object)
 |  float(x) -> floating point number
 |  
 |  Convert a string or number to a floating point number, if possible.
 |  
 |  Methods defined here:
 |  
 |  __abs__(...)
 |      x.__abs__() <==> abs(x)
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __bool__(...)
 |      x.__bool__() <==> x != 0
 |  
 |  __divmod__(...)
 |      x.__divmod__(y) <==> divmod(x, y)
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __float__(...)
 |      x.__float__() <==> float(x)
 |  
 |  __floordiv__(...)
 |      x.__floordiv__(y) <==> x//y
 |  
 |  __format__(...)
 |      float.__format__(format_spec) -> string
 |      
 |      Formats the float according to format_spec.
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __int__(...)
 |      x.__int__() <==> int(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(y) <==> x*y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __neg__(...)
 |      x.__neg__() <==> -x
 |  
 |  __pos__(...)
 |      x.__pos__() <==> +x
 |  
 |  __pow__(...)
 |      x.__pow__(y[, z]) <==> pow(x, y[, z])
 |  
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |  
 |  __rdivmod__(...)
 |      x.__rdivmod__(y) <==> divmod(y, x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rfloordiv__(...)
 |      x.__rfloordiv__(y) <==> y//x
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(y) <==> y*x
 |  
 |  __round__(...)
 |      Returns the Integral closest to x, rounding half toward even.
 |      When an argument is passed, works like built-in round(x, ndigits).
 |  
 |  __rpow__(...)
 |      y.__rpow__(x[, z]) <==> pow(x, y[, z])
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __rtruediv__(...)
 |      x.__rtruediv__(y) <==> y/x
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  __truediv__(...)
 |      x.__truediv__(y) <==> x/y
 |  
 |  __trunc__(...)
 |      Returns the Integral closest to x between 0 and x.
 |  
 |  as_integer_ratio(...)
 |      float.as_integer_ratio() -> (int, int)
 |      
 |      Returns a pair of integers, whose ratio is exactly equal to the original
 |      float and with a positive denominator.
 |      Raises OverflowError on infinities and a ValueError on NaNs.
 |      
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any float.
 |  
 |  hex(...)
 |      float.hex() -> string
 |      
 |      Return a hexadecimal representation of a floating-point number.
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |  
 |  is_integer(...)
 |      Returns True if the float is an integer.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __getformat__ = <built-in method __getformat__ of type object>
 |      float.__getformat__(typestr) -> string
 |      
 |      You probably don't want to use this function.  It exists mainly to be
 |      used in Python's test suite.
 |      
 |      typestr must be 'double' or 'float'.  This function returns whichever of
 |      'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
 |      format of floating point numbers used by the C type named by typestr.
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 |  
 |  __setformat__ = <built-in method __setformat__ of type object>
 |      float.__setformat__(typestr, fmt) -> None
 |      
 |      You probably don't want to use this function.  It exists mainly to be
 |      used in Python's test suite.
 |      
 |      typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
 |      'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
 |      one of the latter two if it appears to match the underlying C reality.
 |      
 |      Overrides the automatic determination of C-level floating point type.
 |      This affects how floats are converted to and from binary strings.
 |  
 |  fromhex = <built-in method fromhex of type object>
 |      float.fromhex(string) -> float
 |      
 |      Create a floating-point number from a hexadecimal string.
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -4.9406564584124654e-324
