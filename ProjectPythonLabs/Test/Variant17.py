# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 08:59:11 2014

@author: Ofim
"""

import numpy as np



def check(string):
    count = 0
    
    for i in string:
        if(i != "("):
            count -= 1
            if(count < 0):
                return False;
        else:
            count += 1
            
    if(count == 0):
        return True
    else:
        return False


def main():   
    string = input("Input string:")
    answer = check(string)
    if(answer):
        print("Строка сбалансирована!")
    else:
        print("Строка НЕ сбалансирована!")
    

if __name__ == "__main__":
    main()