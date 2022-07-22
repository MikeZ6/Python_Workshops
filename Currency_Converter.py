"""
Author: Mike Zhang

The program 
1) creates and records interest rates in a csv file
2) presents exchange rates 
3) calculates currencies exchanged from SGD based on amount and rate
"""

def Rates_CSV():
    import csv
    with open('currency.csv', mode='w', newline='') as csv_file:
        fieldnames = ['Currency','rate']
        writer=csv.DictWriter(csv_file, fieldnames = fieldnames)
       
        writer.writerow({'Currency':'USD', 'rate':0.73829})
        writer.writerow({'Currency':'MYR', 'rate':3.05657})
        writer.writerow({'Currency':'EUR', 'rate':0.66323})
        writer.writerow({'Currency':'BGP', 'rate':0.55172})
        writer.writerow({'Currency':'AUD', 'rate':1.07305})
    


def Exchange():
    sgToCur={}
    
    with open("currency.csv", "r") as file_pointer:
        for each in file_pointer:
            s = each.strip().split(",")
            sgToCur[s[0]] = float(s[1])
    
    menu = """
Welcome to Forex Calculator
The rates are as shown below:
"""
    
    print(menu)
    for Currency, rate in sgToCur.items():
        print(f"{'':20}{Currency}:{rate:5f}")
        
    while True:
        try:
            value = float(input("Enter SGD value to convert: "))
            break
        except:
            print("Invalid decimal number")
    
    Currency=input("Which currency you want? ").upper()
    while Currency not in sgToCur.keys():
        print("I don't support this currency, please try again")
        Currency=input("Which currency you want? ").upper()
           
    rate = sgToCur[Currency]
    print(f"{Currency} values = {value:.2f} * {rate} = ${value*rate:.2f}")
    


if __name__ == "__main__":
    Rates_CSV()
    Exchange()