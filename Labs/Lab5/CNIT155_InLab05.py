#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This Python program displays a menu with five options. Depending on the user’s choice, 
# the program takes the user’s input and performs various computations. The user can exit the program by selecting 5.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defined the main function
    
    option = 0  #set option as a int variable
    
    while(option != 5): #while loop to keep displaying the menu with options 
    
        print("\n\n\tFor Loops Lab")
        print("==============================================")
        print("1. Display and Add natural numbers from N to 1")
        print("2. The Multiplecation table of N")
        print("3. The Pyramid of Stars")
        print("4. The Pyramid of Numbers")
        print("5. Exit")
        print("==============================================")
    
        option = int(input("Choose one of the options to perform: ")) #set option variable as a input
        
        if(option == 1):    #if option 1 is selected
            total = 0
            n = int(input("Enter a natural number for N: "))
            print(f"Displaying natural numbers from {n} to 1")
            for i in range(n, 0, -1):   #for loop
                print(i)
                total = total + i
            print(f"The sum of natural numbers from {n} to 1: {total}")
        
        elif(option == 2):  #if option 2 is selected
            total = 0
            n = int(input("Enter a natural number for N: "))
            print(f"The miltiplecation table of {n}")
            for i in range(1, 11):  #for loop
                total = n * i
                print(f"{n} * {i} = {total}")
                
        elif(option == 3):      #if option 3 is selected
            n = int(input("Enter a number to define the number of the rows of *: "))
            for i in range(0, n + 1):   #Nested for loop
                for i in range(i):
                    print("*", end=" ")
                print()
        
        elif(option == 4):  #if option 4 is selected
            n = int(input("Enter a number to define the number of the rows of numbers: "))
            for i in range(n + 1, 1, -1):
                for i in range(1, i):   #Nested for loop
                    print(i, end=" ")
                print()
                
        elif(option == 5):  #if option 5 is selected
            print("Good Bye!")
    
        else:   #if no option conditions are met
            print("Invalid option!\nPlease choose an option between 1 and 5")
    
main()  #calling the main function that starts the program

#end of the program