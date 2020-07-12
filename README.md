# EasyConversion 0.4.5

The GitHub for the EasyConversion package. 

For in-detail documentation see the [readthedocs page](https://easyconversion.readthedocs.io/en/latest/).

## Installation:
```pip
pip install EasyConversion
```
## Basic example:
```python
from EasyConversion import convert
#Imports


print(convert.binary.decimal(["10101", "1111", "11111111", "InvalidBinary"], return_type=str))
#Converts the list of binaries into decimal
#Returns:
#   ['21', '15', '255', '0']

print (
    convert.detect.asciistring("HELLO") + "\n" +
    convert.detect.asciistring("1000001 1010101")
)
#Detects if the input is ascii or text and converts it both ways
#Returns:
#   01001000 01000101 01001100 01001100 01001111
#   AU
```

## Folders
* `Examples` library examples for information
* `Archive` archive of all previous version files, also available on the [PyPi page](https://pypi.org/project/EasyConversion/)
* `Code` all the code for the library. Updated every version release
* `docs` area for the documentation for the use of the [readthedocs page](https://easyconversion.readthedocs.io/en/latest/). (also visible on GitHub)

Also see the [PyPi page](https://pypi.org/project/EasyConversion/) for download files and other descriptions
