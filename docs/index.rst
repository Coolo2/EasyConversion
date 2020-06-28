.. include:: .special.rst
##################
Easy Conversion
##################

| EasyConversion is a library for easily converting in python. It is mostly made for testing, but can be used.
| It is very early so don't expect much from it


******************
Starting
******************
:red: `this part is red?`
**Installation:**

``pip install EasyConversion``

Or download it from the `PyPi page <https://pypi.org/project/EasyConversion/>`_

**Importing:**

    Importing main conversion:
          ``from EasyConversion import convert``

    Importing Documentation in python:
          ``from EasyConversion import docs``



####################################
EasyConversion.convert.
####################################
    
    Section for converting. There will be input, output, aliases and usage Documented.  

Decimal to binary:
^^^^^^^^^^^^^^^^^^^^^^^^



**Usage**::

   DecToBin(decimal : [str, int, list], return_type=bin)


**Arguments:**

    | ``decimal`` the decimal number to input. Type: ``str, int, list``
    | Optional: ``return_type`` the output type. Options: ``bin, str, int`` Defaults to bin
    
    
**Output:**

    | Output can be in a bin, str, int, or [list](if input type is list)
    | Output type defaults to bin
    | Output type can be changed with argument ``return_type=[str, int, bin]``
    | If input type is list, it returns all sections converted in the same order
    | List form returns '0' in error.


**Aliases:**

    * dectobin
    * decimaltobinary
    * DecimalToBinary


Binary to Decimal:
^^^^^^^^^^^^^^^^^^^^^^^^



**Usage**::

   BinToDec(binary : [bin, int, str, list], return_type=int)


**Arguments:**

    | ``binary`` the binary number to input. Type: ``str, int, bin, list``
    | Optional: ``return_type`` the output type. Options: ``str, int`` Defaults to int
    
    
**Output:**

    | Output can be in a str, int, or [list](if input type is list)
    | Output type defaults to int
    | Output type can be changed with argument ``return_type=[str, int]``
    | If input type is list, it returns all sections converted in the same order
    | List form returns '0' in error.


**Aliases:**

    * bintodec
    * binarytodecimal
    * BinaryToDecimal

`PyPi page <https://pypi.org/project/EasyConversion/>`_ | `GitHub page <https://github.com/Coolo22/EasyConversion/>`_
