##################
Easy Conversion
##################

| EasyConversion is a library for easily converting in python. It is mostly made for testing, but can be used.
| It is very early so don't expect much from it


******************
Starting
******************

    Installation
    =============

    ``pip install EasyConversion``

    Importing:
    =============

        Importing main conversion:
              ``from EasyConversion import convert``

        Importing Documentation in python:
              ``from EasyConversion import docs``



***************************
EasyConversion.convert.
***************************
    
    For conversions    

Decimal to binary:
^^^^^^^^^^^^^^^^^^^^^^^^



Usage:
^^^^^^^^^^^^^^^^
    ``DecToBin(decimal : str, int, list, return_type=str)``



Arguments:
^^^^^^^^^^^^^^^^

    | ``decimal`` the decimal number to input. Type: ``str, int, list``
    | Optional: ``return_type`` the output type. Options: ``bin, str, int`` Defaults to bin

Output:
^^^^^^^^
    | Output can be in a str, int, or [list](if input type is list)
    | Output type defaults to bin
    | Output type can be changed with argument return_type=[str, int, bin]
    | If input type is list, it returns all sections converted in the same order
    | List form returns '0' in error.

Aliases:
^^^^^^^^
    * dectobin
    * decimaltobinary
    * DecimalToBinary
