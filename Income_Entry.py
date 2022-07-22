"""
Author: Mike Zhang

The program displays a menu as following:

Please enter the income for Monday: 150

Please enter the income for Tuesday: 53

Please enter the income for Wednesday: 0

Please enter the income for Thursday: 56

Please enter the income for Friday: 75
==================================================
Total income of the week is $334.00
Average daily income of the week is $66.80 

Highest income is $150.00
Monday
Lowest income is $0.00
Wednesday

The program allows entry of income for the five days and calculates outputs of total, average, highest and lowest.
"""
def Income_Entry():
    incomelist = [] # declare an income list with 1 item 0 because Sunday got no income
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    
    for each in weekdays:
        incomelist.append(float(input(f"Please enter the income for {each}: ")))
    
    print("="*50)
    totalIncome = sum(incomelist)
    print(f"Total income of the week is ${totalIncome:.2f}")
    print(f"Average daily income of the week is ${totalIncome/len(weekdays):.2f}","\n")
    
    maxIncome = max(incomelist)
    print(f"Highest income is ${maxIncome:.2f}")  
    for index in range(len(incomelist)):
        if(incomelist[index]) == maxIncome:
            print(weekdays[index])
      
    minIncome = min(incomelist)      
    print(f"Lowest income is ${minIncome:.2f}")    
    for index in range(len(weekdays)):
        if (incomelist[index]) == minIncome:
            print(weekdays[index])


if __name__ == "__main__":
    Income_Entry()
