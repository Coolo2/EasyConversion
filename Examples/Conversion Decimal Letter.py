from EasyConversion import convert
#Import

print(convert.decimal.letter(["1", "2", "7", "50", "notnumber10"]))
#Convert a decimal list into letters. No repeats, anything needing a repeat will output None
#Outputs:
#   ['a', 'b', 'g', None, None]

print(convert.decimal.letter(["50", "89", "3", "1", "notnumber11"], repeat=True))
#Convert a decimal list into letters. Repeat activated, so anything needing a repeat will output the letter after repeats.
#Outputs:
#   ['x', 'k', 'c', 'a', None]
