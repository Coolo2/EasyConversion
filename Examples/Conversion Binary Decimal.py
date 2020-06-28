from EasyConversion import convert
#Imports



print(convert.binary.decimal(["10101", "1111", "11111111", "InvalidBinary"], return_type=str))

#Prints the list of binaries as decimal numbers, returning in a str list.
#Returns:
#    ['21', '15', '255', '0']



binary = convert.decimal.binary("21", return_type=bin)

#Converts the decimal (as a str, can be int) into binary, returning as a bin. 
#Returns:
#    0b10101
