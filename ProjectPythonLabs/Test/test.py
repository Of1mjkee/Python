# -*- coding: utf-8 -*-

import math

#def main():
#    inputList = [1,2,3,4,5,6,7,8]
#    lengthInputList = len(inputList) 
#    k = int(math.log(lengthInputList,2))
#    resultList = inputList[:]
#    for index in range(lengthInputList):
#        newIndex = getIndex(index, k)
#        print(newIndex)
#        resultList[newIndex] = inputList[index]
#    print(inputList)
#    print(resultList)        
    
def getIndex(index, k):
    strbit = bin(index)
    print(strbit)
    cleanbit = strbit[2:]
    print(cleanbit)
    length = len(cleanbit)
    if(k > length):
         cleanbit = "0"*(k-length) + cleanbit
    print(cleanbit)
    revstr = cleanbit[::-1]
    result = int(revstr,2)
    return result

a = getIndex(1, 3)
print(a)

#if __name__ == "__main__":
#    main()  



#inputList = [1,2,3,4,5,6,7,8]
#s = "".join()
#print(s)
#str = "abcd"
#print(str[2:])        
#    
#ind = getIndex(6)
#print(ind)


#strbit = "0b10"
#
#strbit = strbit[:2] + ("0"*2) + strbit[2:]
#print(strbit)

#s = "0b1010"
#s[2] = "10"
#print(s)


#s[:4] + '-' + s[4:]
#'3558-79ACB6'

#value = 2
#bit = bin(value)
#l = value.bit_length()
#print(bit)
#print(l)
#print(len(bit))




