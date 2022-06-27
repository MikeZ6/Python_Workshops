"""
Author: Mike Zhang

The program displays a menu as following:

                        <<Welcome!>>
                A. Add an item
                D. Display all items
                T. Transact
                X. Exit the application

The program runs in a loop and responds to each input until the user enters “X” to exit.
"""
def Menu():
    while True:
        menu = """
                                <<Welcome!>>
                        A. Add an item
                        D. Display all items
                        T. Transact
                        X. Exit the application
        """
    
        print(menu)
        choice = input("Please choose one of the above options: ").upper()
        if choice == 'A':
            print("You are about to add an item")
        elif choice =='D':
            print("All items will show here")
        elif choice =='T':
            print("Please wait while we transact...")
        elif choice =='X':
            print("See you again")
            print("Good Bye!")
            break
        else :
            print("You have selected a wrong entry")
    

if __name__ == "__main__":
    Menu()