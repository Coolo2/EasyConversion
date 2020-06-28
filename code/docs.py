from EasyConversion import textformat

colour = textformat.color

class Dec:
    Bin = f"""
{colour.BOLD} **CONVERT DECIMAL TO BINARY** {colour.END}
{colour.UNDERLINE}Usage:{colour.END}
    convert.decimal.binary(decimal, return_type=str)
    {colour.UNDERLINE}Arguments:{colour.END}
        decimal = decimal number to input [int, str, list]
        return_type = int, str, bin
{colour.UNDERLINE}Input: {colour.END}
    Input can be in a str, int, or list
{colour.UNDERLINE}Output:{colour.END}
    Output can be in a str, int, or [list](if input type is list) 
    Output type defaults to bin
    Output type can be changed with argument return_type=[str, int, bin]
    If input type is list, it returns all sections converted in the same order
    List form returns '0' in error.
{colour.UNDERLINE}Aliases:{colour.END}
    dec.Bin, Decimal.Binary, Dec.Bin, Decimal.binary
{colour.BOLD}More advanced docs can be found at
https://easyconversion.readthedocs.io/
{colour.END}  
    """

    Letter = f"""
{colour.BOLD} **CONVERT DECIMAL TO LETTER** {colour.END}
Converts between decimal and letter (based on alphabet, not ascii)
{colour.UNDERLINE}Usage:{colour.END}
    convert.decimal.letter(decimal)
    {colour.UNDERLINE}Arguments:{colour.END}
        decimal = decimal number to input [int, str, list]
        return_type = str / str-list
{colour.UNDERLINE}Input: {colour.END}
    Input can be in a str, int, or list
{colour.UNDERLINE}Output:{colour.END}
    Output can be in a str or [list](if input type is list) 
    If input type is list, it returns all sections converted in the same order
    List form returns None in error.
{colour.UNDERLINE}Aliases:{colour.END}
    dec.letter, Decimal.Letter, Dec.Let, dec.let, Decimal.letter
{colour.BOLD}More advanced docs can be found at
https://easyconversion.readthedocs.io/
{colour.END}  
    """
    letter, let, Let = Letter, Letter, Letter
    bin, binary, Binary = Bin, Bin, Bin



decimal, dec, Decimal = Dec, Dec, Dec



class Bin():
    Dec = f"""
{colour.BOLD}CONVERT BINARY TO DECIMAL{colour.END}
{colour.UNDERLINE}Usage:{colour.END}
    convert.binary.decimal(binary, return_type=str)
    {colour.UNDERLINE}Arguments:{colour.END}
        binary = binary number to input [int, str, list, bin]
        return_type = int, str
{colour.UNDERLINE}Input: {colour.END}
    Input can be in a str, int, bin or list (of any of the previous)
{colour.UNDERLINE}Output:{colour.END}
    Output can be in a str, int, or [list](if input type is list) 
    Output type defaults to int
    Output type can be changed with argument return_type=[str, int, bin]
    If input type is list, it returns all sections converted in the same order
    List form returns '0' in error.
{colour.UNDERLINE}Aliases:{colour.END}
    Bin.Dec, Bin.dec, Binary.Decimal, Binary.decimal
{colour.BOLD}More advanced docs can be found at
https://easyconversion.readthedocs.io/
{colour.END}  
"""
    dec, decimal, Decimal = Dec, Dec, Dec

binary, Binary, bin = Bin, Bin, Bin

class Letter:
    Decimal = f"""
{colour.BOLD} **CONVERT LETTER TO DECIMAL** {colour.END}
Converts between letter and decimal (based on alphabet, not ascii)
{colour.UNDERLINE}Usage:{colour.END}
    convert.letter.decimal(letter, return_type=int)
    {colour.UNDERLINE}Arguments:{colour.END}
        letter = letter to input [str, list]
        return_type = str / int / str/int list
{colour.UNDERLINE}Input: {colour.END}
    Input can be in a str or list
{colour.UNDERLINE}Output:{colour.END}
    Output can be in a str, int or [list](if input type is list) 
    Output type can be determined with argument return_type=[type]
    If input type is list, it returns all sections converted in the same order
    List form returns None in error.
{colour.UNDERLINE}Aliases:{colour.END}
    letter.dec, Letter.Decimal, Let.Dec, let.dec, Letter.decimal
{colour.BOLD}More advanced docs can be found at
https://easyconversion.readthedocs.io/
{colour.END}  
    """

    dec, Dec, decimal = Decimal, Decimal, Decimal
                                
letter, let, Let = Letter, Letter, Letter
