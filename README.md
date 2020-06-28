# EasyConversion

The GitHub for the EasyConversion package. 

For in-detail documentation see the [readthedocs page](https://easyconversion.readthedocs.io/en/latest/).

## Installation:
```pip
pip install EasyConversion
```
## Basic example:
```python
from EasyConversion import convert
from EasyConversion import docs
#Imports


print(convert.binary.decimal(["10101", "1111", "11111111", "InvalidBinary"], return_type=str))
#Prints the list of binaries as decimal numbers, returning in a str list.
#Returns:
#    ['21', '15', '255', '0']

binary = convert.decimal.binary("21", return_type=bin)
#Converts the decimal (as a str, can be int) into binary, returning as a bin. 
#Returns:
#    0b10101


print(docs.Bin.Dec)
#Prints documentation for Binary To Decimal conversions"""
```

## Folders
* `Examples` library examples for information
* `Archive` archive of all previous version files, also available on the [PyPi page](https://pypi.org/project/EasyConversion/)
* `Code` all the code for the library. Updated every version release
* `docs` area for the documentation for the use of the [readthedocs page](https://easyconversion.readthedocs.io/en/latest/). (also visible on GitHub)

Also see the [PyPi page](https://pypi.org/project/EasyConversion/) for download files and other descriptions
