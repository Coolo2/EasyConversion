from EasyConversion.convert import Convert as c
from EasyConversion.docs import Docs as d
"""Imports"""


print(c.BinToDec(["10101", "1111", "11111111", "InvalidBinary"], return_type=str))
"""
Prints the list of binaries as decimal numbers, returning in a str list.
Returns:
    ['21', '15', '255', '0']
"""

binary = c.DecimaltoBinary("21", return_type=bin)
"""
Converts the decimal (as a str, can be int) into binary, returning as a bin. 
Returns:
    0b10101
"""


print(d.bintodec)
"""Prints documentation for Binary To Decimal conversions"""
