
#class Convert():
    #def __init__(self):
        #pass

def DecToBin(decimal, return_type=bin):
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

        except:
            raise Exception('Invalid decimal.')

dectobin, decimaltobinary, DecimalToBinary = DecToBin, DecToBin, DecToBin




def BinToDec(binary, return_type=int):
    if type(binary) is list:
        return_list = []
        for number in binary:

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

bintodec, binarytodecimal, BinaryToDecimal = BinToDec, BinToDec, BinToDec



