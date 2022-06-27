"""
Author: Mike Zhang

The program generates a table for interest rate, years and beginning amount entered.

Input
Amount: 15000
Years: 4
Interest rate: 2.5

Output:
Year        Deposit     Interest    Balance   
Begin      15,000.00  
1                        375.00    15,375.00  
2                        384.38    15,759.38  
3                        393.98    16,153.36  
4                        403.83    16,557.19 
"""

def Interest_Table():
    balance = float(input("Please enter starting amount: "))
    yrs = int(input("Enter Amount of Years: "))
    interestRate = float(input("Interest Rate: "))
    
    print(f"{'Year':<10s}{'Deposit':^12s}{'Interest':^12s}{'Balance':^12s}")
    print(f"{'Begin':<10s}{balance:^12,.2f}")
    
    for countYear in range(yrs):
        interest = balance * interestRate/100
        balance += interest
        print(f"{countYear+1:<10d}{'':12s}{interest:^12,.2f}{balance:^12,.2f}")
        
if __name__ == "__main__":
    Interest_Table()