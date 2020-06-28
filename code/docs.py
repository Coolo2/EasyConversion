from EasyConversion import textformat

colour = textformat.color



class BinToDec_Declare():
    BinToDec = f"""
{colour.BOLD}CONVERT BINARY TO DECIMAL{colour.END}
{colour.UNDERLINE}Usage:{colour.END}
    Convert.BinToDec(binary, return_type=str)
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
    bintodec, BinaryToDecimal, binarytodecimal"""




class DecToBin_Declare():
    DecToBin = f"""
{colour.BOLD} **CONVERT DECIMAL TO BINARY** {colour.END}
{colour.UNDERLINE}Usage:{colour.END}
    Convert.DecToBin(decimal, return_type=str)
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
    dectobin, DecimalToBinary, decimaltobinary"""
    
    
    

dectobin, decimaltobinary, DecimalToBinary = DecToBin_Declare.DecToBin, DecToBin_Declare.DecToBin, DecToBin_Declare.DecToBin
bintodec, binarytodecimal, BinaryToDecimal = BinToDec_Declare.BinToDec,BinToDec_Declare.BinToDec, BinToDec_Declare.BinToDec