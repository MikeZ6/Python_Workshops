"""
Author: Mike Zhang

This program returns input numeric numbers from 0-99 to english. Refer to the 'spell_0to99' function
"""

#%%
def spell_0To9(number):
    Key = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 
       7:"Seven", 8:"Eight", 9:"Nine"}
    
    number = int(number)
    if number <0:
        return f"function does not know how to spell {number}", False
    elif number > 9:
        return f"function does not know how to spell {number}", False
    else:
        return f"{number} is {Key[number]}", True

if __name__ =="__main__":
    for  i in range (-2,14):
        word,isOK = spell_0To9(i)
        if isOK:
            print(f"{word}")
        else:
            print(f"function does not know how to spell {i}")

#%%
def spell_10To19(number):
    Key = {10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 
           16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
    
    number = int(number)
    if number <10:
        return f"function does not know how to spell {number}", False
    elif number > 19:
        return  f"function does not know how to spell {number}", False
    else:
        return f"{number} is {Key[number]}", True

if __name__ =="__main__":
    for  i in range (-2,20):
        word,isOK = spell_10To19(i)
        if isOK:
            print(f"{word}")
        else:
            print(f"function does not know how to spell {i}")

#%%
def spell_10Mult(number):
    Key = {0:"Zero", 10:"Ten", 20:"Twenty", 30:"Thirty", 40:"Fourty", 50:"Fifty", 
           60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety", 100: "One Hundred"}
    
    number = int(number)
    if number % 10 != 0:
        return f"function does not know how to spell {number}", False
    elif number > 100:
        return f"function does not know how to spell {number}", False
    else:
        return f"{number} is {Key[number]}", True
    
if __name__ =="__main__":
    for  i in range (-2,100):
        word,isOK = spell_10Mult(i)
        if isOK:
            print(f"{word}")
        else:
            print(f"function does not know how to spell {i}")

#%%
def spell_0to99(number):
    DigitKey = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 
       7:"Seven", 8:"Eight", 9:"Nine"}
    TensKey = {10:"Ten", 20:"Twenty", 30:"Thirty", 40:"Fourty", 50:"Fifty", 
           60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety", 100: "One Hundred"}
    if number <0:
        return f"function does not know how to spell {number}", False
    elif 0<= number < 10:
        return spell_0To9(number)
    elif number <20:
        return spell_10To19(number)
    elif number % 10 == 0:
        return spell_10Mult(number)
    elif number > 100:
        return f"function does not know how to spell {number}", False
    else:
        singleDigit = number%10
        TensDigit = (number//10)*10
        return f"{number} is {TensKey[TensDigit]} {DigitKey[singleDigit]}", True
        

if __name__ =="__main__":
    for  i in range (-2,100):
        word,isOK = spell_0to99(i)
        if isOK:
            print(f"{word}")
        else:
            print(f"function does not know how to spell {i}")

