##################
Easy Conversion
##################

`PyPi page <https://pypi.org/project/EasyConversion/>`_ | `GitHub page <https://github.com/Coolo22/EasyConversion/>`_

|

| EasyConversion is a library for easily converting in python. It is mostly made for testing, but can be used.
| It is very early so don't expect much from it
| For code examples, please see `here <https://github.com/Coolo22/EasyConversion/tree/master/Examples>`_


******************
Setup
******************

**Installation:**

    ``pip install EasyConversion``

Or download it from the `PyPi page <https://pypi.org/project/EasyConversion/>`_

**Importing:**

    Importing main conversion:
          ``from EasyConversion import convert``

    Importing Documentation in python:
          ``from EasyConversion import docs``



####################################
``EasyConversion``.convert
####################################
    
    Section for converting. There will be input, output, aliases and usage Documented.  

| 

.. raw:: html

    <h2>Decimal To Binary</h2>

| 

**Usage**::

   .decimal.binary(decimal : [str, int, list], return_type=bin)


**Full example**::
   
   from EasyConversion import convert
   print(convert.decimal.binary("21", return_type=bin))
   

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

    * dec.Bin
    * Dec.Bin
    * Decimal.Binary

| 

.. raw:: html

    <h2>Binary to Decimal</h2>

| 



**Usage**::

    .binary.decimal(binary : [bin, int, str, list], return_type=int)

**Full example**::
   
   from EasyConversion import convert
   print(convert.binary.decimal("10101", return_type=str))
   
   
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

    * Bin.Dec
    * Bin.dec
    * Binary.Decimal

.. raw:: html

    <h2>Decimal to Letter</h2>

| 


**Usage**::

   .decimal.letter

**Full example**::
   
   from EasyConversion import convert
   print(convert.decimal.letter(["100", "3", "4", "not_number"]))
   print(convert.decimal.letter(["100", "3", "4", "not_number"], repeat=True))
   
**Output:**

    | The full example would output
    |     ``[None, 'c', 'd', None]``
    |     ``['v', 'c', 'd', None]``
    | Output is the input number in letters (based on aplhabet)
    | Output is in ``str``


**Aliases:**

    * Dec.letter
    * Dec.let
    * Decimal.Let
    * Decimal.Letter
    * decimal.Letter

| 

.. raw:: html

    <h2>Letter to Decimal</h2>

| 


**Usage**::

   .letter.decimal

**Full example**::
   
   from EasyConversion import convert
   print(convert.letter.decimal(["a", "b", "g", "100number"]))
   print(convert.letter.decimal("abcdefgh", return_type=str))
   
**Output:**

    | The full example would output
    |     ``[1, 2, 7, None]``
    |     ``['1', '2', '3', '4', '5', '6', '7', '8']``
    | Output is the input letter(s) in numbers (based on aplhabet)
    | Output is in ``int`` by default, or ``return_type=[option]``
    | Output is a list unless it's a single letter


**Aliases:**

    * Letter.dec
    * Let.dec
    * Letter.Dec
    * Letter.Decimal
    * letter.Decimal


####################################
``EasyConversion``.docs
####################################

Get the docs for a function, in the python script (less detailed, easier to find)


| 

.. raw:: html

    <h2>Documentation fetch format</h2>

| 


**Usage**::

   .[from].[to]

   Example:
   .letter.decimal

**Full example**::
   
   from EasyConversion import docs
   print(docs.decimal.letter)
   
**Output:**

    | Docs for the section in ``str``


**Aliases:**

    * See aliases for the section you want to see the documentation for
    
Aliases for .docs 
    * .docfetch
    * .fetch_docs
    * .documentation

| 

########################################
``EasyConversion``.info `(new in 0.4.0)`
########################################

.. raw:: html

    <h2><b>.version</b></h2>

Current version of the package with different Options:

    ``.name``
    Current version name/number 

    ``.release_date``
    Current version release date

| 
| 

####################################
Version history
####################################

| 
| 

******************************
**0.4.1** (current) : 28 June 2020
******************************

    * Fixed major bug causing letter conversions to freeze
    * Added PyPi description
    * Updated GitHub page

| 

********************************************
**0.4.0** : 28 June 2020
********************************************

    * Re-ordered sections to make converting easier to read
    * Fixed more aliases
    * Improved (this) documentation page
    * New convert option: letter (convert between number and letter)
    * Fixed bugs with binary with decimal errors
    * New file system, seperated sections convert and doc 
    * New section, info (get version info, release date etc)
    * General fixes and improvements all-round

| 

******************************
**0.3.1** : 28 June 2020
******************************

    * Fixed docs function
    * Fixed most aliases

| 

********************
**0.3** : 28 June 2020
********************

    * Changed the file system so imports are smaller and easier
    * Fixed inputting binary in type ``bin``

| 

******************************
**0.2** : 27 June 2020
******************************

    * Added in-built docs

| 

******************************
**0.1** : 27 June 2020
******************************

    * Initial release (``.Convert.BinToDec`` and ``.Convert.DecToBin``) [after **0.3** these do not work.]
