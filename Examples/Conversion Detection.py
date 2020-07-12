from EasyConversion import convert
#Imports

print (convert.detect.asciistring("HELLO") )
#Detects if the input is ascii or text and converts it both ways
#Returns:
#   01001000 01000101 01001100 01001100 01001111

print (convert.detect.morsestring("···· · ·-·· ·-·· ---") )
#Detects if the input is ascii or text and converts it both ways
#Returns:
#   HELLO
