from EasyConversion import Morse_Dict 

MORSE_CODE_DICT = Morse_Dict.dict.Dict

class Dec:


    def Bin(decimal, return_type=bin):
        if type(decimal) is list:
            return_list = []
            for number in decimal:

                try:
                    binary = bin(int(number))
                    
                    try:
                        
                        if return_type == bin:
                            
                            return_list.append(binary)
                        else:
                            
                            return_list.append(return_type(str(binary)[2:]))
                    
                    except:
                    
                        raise TypeError('Invalid return type')
                        
                
                except:
                    try:
                        return_list.append(return_type(0))
                    except:
                        raise TypeError('Invalid return type')


            return return_list

        else:

            try:
                binary = bin(int(decimal))
                try:
                    if return_type == bin:
                                
                        return binary
                    else:
                        
                        return return_type(str(binary)[2:])
                
                except:
                    raise TypeError('Invalid return type')

            except Exception as e:
                print(e)
                raise Exception('Invalid decimal.')

    binary, Binary = Bin, Bin


    def Letter(input_number, repeat=False):
        if repeat == False or repeat in ['false', 'False', '0', 0]:
            if type(input_number) is list:
                return_list = []
                for number in input_number:
                    try:
                        number = int(number)
                    except:
                        number = None
                    done =0
                    counter = 0
                    for letter in "abcdefghijklmnopqrstuvwxyz":

                        counter = counter + 1
                        
                        if counter == number:
                            done = 1
                            return_list.append(letter)
                    if done != 1:
                        return_list.append(None)

                return return_list

            else:
                counter = 0
                try:
                    number = int(input_number)
                except:
                    raise Exception('Invalid decimal')
                for letter in "abcdefghijklmnopqrstuvwxyz":

                    counter = counter + 1


                    if counter == input_number:
                        return letter
        elif repeat == True or repeat in ['true', 'True', '1', 1]:
            if type(input_number) is list:
                return_list = []
                
                for number in input_number:
                    
                    try:
                        number = int(number)
                    except:
                        number = None

                    counter = 0
                    
                    complete = False
                    while complete == False:
                        
                        for letter in "abcdefghijklmnopqrstuvwxyz":

                            counter = counter + 1
                            
                            digit = False
                            if str(number).isalpha():
                                digit = True

                            if counter == number:
                                done = 1
                                return_list.append(letter)
                                complete = True
                        if digit == True:
                            return_list.append(None)
                            complete = True

                return return_list
            else:
                counter = 0
                try:
                    number = int(input_number)
                except:
                    raise Exception('Invalid decimal')

                complete = False
                while complete == False:
                    for letter in "abcdefghijklmnopqrstuvwxyz":

                        counter = counter + 1

                        if counter == number:
                            return letter
                            complete = True
        else:
            raise TypeError('Incorrect value for `repeat=`')
    
    letter, let, Let = Letter, Letter, Letter

decimal, dec, Decimal = Dec, Dec, Dec

class Bin:


    def Dec(binary, return_type=int):
        if type(binary) is list:
            return_list = []
            for number in binary:

                for non_binary in ['2', '3', '4', '5', '6', '7', '8', '9']:
                    if non_binary in number:

                        binary = 0



                try:
                    binary = int(str(number.replace('0b', '')))
                except:
                    binary = 0
                
                
                decimal = 0 #create decimal variable
                
                binary = list(str(binary)) #convert the binary into a list
                binary = binary[::-1]      #reverse the list
                
                power = 0   #make power variable
                
                
                for number in binary:
                    if number == '1':
                        
                        decimal += 2**power    
                    
                    power += 1 #increase the power variable by one  
                
                try:
                    return_list.append(return_type(decimal))
                
                except:
                    return_list.append(return_type("0"))


            return return_list

        else:

            for non_binary in ['2', '3', '4', '5', '6', '7', '8', '9']:
                if non_binary in binary:

                    raise TypeError('Invalid binary number')

            try:
                binary = int(str(binary).replace('0b', ''))
            except:
                raise TypeError('Invalid binary number')
            
            
            decimal = 0 #create decimal variable
            
            binary = list(str(binary)) #convert the binary into a list
            binary = binary[::-1]      #reverse the list
            
            power = 0   #make power variable
            
            
            for number in binary:
                if number == '1':
                    
                    decimal += 2**power    
                
                power += 1 #increase the power variable by one  
            
            try:
                return return_type(decimal)
            
            except:
                raise TypeError('Invalid return type')
    
    dec, decimal, Decimal = Dec, Dec, Dec

binary, Binary = Bin, Bin

class Ascii:

    def Letter(input_ascii):
        b = input_ascii
        if type(b) is str:
            if "," in b and ", " not in b:
                final = b.split(",")
            elif ", " in b:
                final = b.split(", ")
            elif " " in b and ',' not in b:
                final = b.split(" ")
            else:
                final = [b]
        if type(b) is list:
            final = []
            for item in b:
                try:
                    final.append(bin(item))
                except:
                    final.append(str(item))
        try:
            return ''.join([chr(int(x, 2)) for x in final])
        except:
            raise Exception('Invalid Ascii')
    
    letter, Let, let, string, Str, String = Letter, Letter, Letter, Letter, Letter, Letter, 

asc, Asc, asciibinary, AsciiBinary, Asciibinary = Ascii, Ascii, Ascii, Ascii, Ascii

class Letter:

    def Decimal(input_letter, return_type=int):
        if return_type not in [int, str]:
            raise TypeError('Invalid return type')
        
        
        if type(input_letter) is list or type(input_letter) is str and len(input_letter) > 1:
            return_list = []
            
            for letter in input_letter:
                
                if not letter.isalpha():
                    return_list.append(None)
                
                
                else:
                    counter = 0
                    
                    for alp in "abcdefghijklmnopqrstuvwxyz":
                        
                        
                        counter = counter + 1
                        if letter.lower() == alp:
                            
                            return_list.append(return_type(counter))
            
            
            return return_list
        
        
        elif type(input_letter) is str:
            
            if not input_letter.isalpha():
                raise Exception('Invalid letter')
            
            
            else:
                counter = 0

                for alp in "abcdefghijklmnopqrstuvwxyz":

                    counter = counter + 1

                    if input_letter.lower() == alp:

                        return return_type(counter)

    
    dec, Dec, decimal = Decimal, Decimal, Decimal

    def Ascii(input_string):
        s = input_string

        if type(s) is not list:

            b = []
            for character in s:

                b.append(character)

        else:
            b = s

        return [bin(ord(x))[2:].zfill(8) for x in b]
    
    asc, Asc, asciibinary, AsciiBinary, Asciibinary = Ascii, Ascii, Ascii, Ascii, Ascii

    def morse(input_text): 
        cipher = '' 
        message = input_text.upper()
        for letter in message: 
            if letter != ' ': 
                try:
                    
                    cipher += MORSE_CODE_DICT[letter] + ' '
                
                except:
                    raise Exception('Found invalid characters')
            else: 
                cipher += ' '
    
        return cipher 
    
    Morse, morsecode, Morsecode, MorseCode = morse, morse, morse, morse


letter, string, String, Str, let, Let = Letter, Letter, Letter, Letter, Letter, Letter

class Detect:
            
    def asciistring(input, return_type=str):

        if return_type == list:
            if True in [c in input for c in "abcdefghijklmnopqrstuvwxyz!@#$%^&*()23456789[];'\,./<>?:|-_ABCDEFGHIJKLMNOPQRSTUVWXYZ="]:

                return Letter.asciibinary(input)
            
            else:
                return asciibinary.Letter(input)
        if return_type == str:

            if True in [c in input for c in "abcdefghijklmnopqrstuvwxyz!@#$%^&*()23456789[];'\,./<>?:|-_ABCDEFGHIJKLMNOPQRSTUVWXYZ="]:

                return ' '.join(Letter.asciibinary(input))
            
            else:
                return asciibinary.Letter(input)
    
    stringascii, StringAscii, Stringascii, Asciistring, AsciiString = asciistring, asciistring, asciistring, asciistring, asciistring

    def binarydecimal(input):

        if True in [c in str(input) for c in "23456789"]:
            return Decimal.Binary(input, return_type=str)
            
        else:
            return Binary.Decimal(str(input).replace("0b", ""))
    
    decimalbinary, Decimalbinary, DecimalBinary, Binarydecimal, BinaryDecimal = binarydecimal, binarydecimal, binarydecimal, binarydecimal, binarydecimal

    def morsestring(input):

        if True in [c in str(input) for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV1234567890!@#$%^&*()=+;'\[]:"]:
            return Letter.morse(input)
            
        else:
            return Morse.string(input)
    
    MorseString, Morsestring, Stringmorse, stringmorse, StringMorse = morsestring, morsestring, morsestring, morsestring, morsestring

detect = Detect

class Morse:

    def string(morse_code): 
  
        message = morse_code
        message += ' '
    
        decipher = '' 
        citext = '' 
        for letter in message: 
    

            if (letter not in [' ', '/', ' / ']):
    

                i = 0
    
                citext += letter 

            else: 
                i += 1
    

                if i == 2 : 
    

                    decipher += ' '
                else: 
                    
                    try:
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                        .values()).index(citext)] 
                        citext = '' 
                    except:
                        try:
                            decipher += list(Morse_Dict.dict.Dict2.keys())[list(Morse_Dict.dict.Dict2
                            .values()).index(citext)] 
                            citext = '' 
                        except:
                            pass
        if decipher == "":
            raise Exception("Invalid morse")
        return decipher 
    
    String, Str, letter, Letter = string, string, string, string

morse, morsecode, Morsecode, MorseCode = Morse, Morse, Morse, Morse
