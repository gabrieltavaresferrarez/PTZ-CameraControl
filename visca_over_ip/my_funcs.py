def dec2bin(int_num:int, numBits = 0):

    bool_negative = int_num < 0

    if bool_negative:
        int_rangeValid = 2**(numBits-1)
        if int_num >= int_rangeValid or int_num <= -int_rangeValid:
            raise ValueError('Valor não cabe no número de bits')
    else:
        int_rangeValid = 2**(numBits)
        if int_num >= int_rangeValid:
            raise ValueError('Valor não cabe no número de bits')

    
    int_numBits = numBits
    int_num = abs(int_num)

    string_binary = '{:b}'.format(int_num)
    if int_numBits > 0:
        string_binary = '0'*(int_numBits - len(string_binary)) + string_binary
    
    if bool_negative:
        #complemento de 2
        #varre todos os numeros da direita pra esquerda até achar bit 1. Ai pula esse bit e inverte todos os bits dali pra frente
        bool_flipBits =  False
        for i in range(len(string_binary)-1, -1, -1):
            if bool_flipBits:
                if string_binary[i] == '0':
                    string_binary = string_binary[:i] + '1' + string_binary[i + 1:]
                else:
                    string_binary = string_binary[:i] + '0' + string_binary[i + 1:]
            if string_binary[i] == '1' and not(bool_flipBits):
                bool_flipBits = True
                
    return string_binary

def get_hex(strb_bin4):
    if strb_bin4 == '0000':
        return '0'
    if strb_bin4 == '0001':
        return '1'
    if strb_bin4 == '0010':
        return '2'
    if strb_bin4 == '0011':
        return '3'
    if strb_bin4 == '0100':
        return '4'
    if strb_bin4 == '0101':
        return '5'
    if strb_bin4 == '0110':
        return '6'
    if strb_bin4 == '0111':
        return '7'
    if strb_bin4 == '1000':
        return '8'
    if strb_bin4 == '1001':
        return '9'
    if strb_bin4 == '1010':
        return 'a'
    if strb_bin4 == '1011':
        return 'b'
    if strb_bin4 == '1100':
        return 'c'
    if strb_bin4 == '1101':
        return 'd'
    if strb_bin4 == '1110':
        return 'e'
    if strb_bin4 == '1111':
        return 'f'

def bin2hex(string_binNum:str):
    int_lenBinNum = len(string_binNum)
    int_zerosToAdd = 4 - (int_lenBinNum % 4)
    if int_zerosToAdd == 4:
        int_zerosToAdd = 0
    
    string_binNum = '0'*int_zerosToAdd + string_binNum
    
    int_lenBinNum = len(string_binNum)
    string_hexNum = ''
    for i in range(0, int_lenBinNum, 4):
        string_hexNum = string_hexNum + get_hex(string_binNum[i:i+4]) 
    return string_hexNum

def visca_hex_format(string_hexNum):
    string_out = ''
    for i in range(len(string_hexNum)):
        string_out = string_out + '0' + string_hexNum[i]
    return string_out