#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: Thsi program has 4 user defined functions and a main function. These functions include finding the 
# factorial, odd sum, inverse sum, and characters in a string. The program will ask the user what process to run, ask for 
# the input, make the computation, and display the resutls. 

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def Factorial(num): #factorial user-defined function
    fact = 1
    for ctr in range(1, num + 1):   #for loop to count
        fact = fact * ctr   #calculation to find the factorial
    return fact

def SumOdds(num1, num2):    #sumOdds user-defined function
    ctr = 0
    total = 0
    for ctr in range(num1, num2 + 1, 2):    #for loop to count by 2
        print(ctr)  #prints the odd numbers
        total = total + ctr
    print(f"The sum of the odd numbers is {total}")
    return total

def SumInverse(num1, num2):     #sumInverse user-defined function
    ctr = 0
    total = 0
    for ctr in range(num1, num2 + 1):   #for loop to print the inverse numbers and find the sum
        print(f"1 / {ctr}")
        total = total + (1 / ctr)
    print(f"The sum of the inverse of the numbers between {num1} and {num2} is {total:.2f}")

def FindChar(string, letter):    #findChar user-defined function
    total = 0
    for ctr in string:
        if(ctr.lower().upper() == letter.lower().upper()):
            total = total + 1
    print(f"The character {letter} appeared {total} times")

def Main():     #main function
    
    option = 0
    
    while(option != 5):     #while loop to keep asking the user for input
        print("\n===============\tUser Defined Functions Menu\t===============")
        print("1. Compute n Factorial")
        print("2. Sum of all odd numbers from n1 to n2 (n1<=n2)")
        print("3. Sum of the inverse of the numbers between n1 and n2 (n1<=n2)")
        print("4. Find the number of Characters")
        print("5. Exit")
        print("===============================================================")
        
        option = int(input("\nChoose one of the options to perform: "))
        
        if(option == 1):    #if/ else if/ else statement to ask the user for and option and then to perform specific tasks
            print("\n1. Compute n Factorial")
            num = int(input("Please enter a natural number for n: "))
            fact = Factorial(num)   #factorial function called
            print(f"{num} != {fact}")
        
        elif(option == 2):
            print("\n2. Sum of all odd numbers from n1 to n2 (n1<=n2)")
            num1 = int(input("Please enter a natural number for n1: "))
            num2 = int(input("Please enter a natural number for n2: "))
            print(f"Displaying odd numbers from {num1} to {num2} (n1<=n2)")
            SumOdds(num1, num2)     #sumodds function called
            
        elif(option == 3):
            print("\n3. Sum of the inverse of the numbers between n1 and n2")
            num1 = int(input("Please enter a natural number for n1: "))
            num2 = int(input("Please enter a natural number for n2: "))
            print(f"Displaying the inverse of the numbers from {num1} to {num2} (n1<=n2)")
            SumInverse(num1, num2)      #sumInverse function called
            
        elif(option == 4):
            print("\n4. Find the Number of Characters")
            string = input("Please enter the string to work on: ")
            letter = input("Please enter a character that you want to count in the string entered above: ")
            FindChar(string, letter)    #findChar function called
            
        elif(option == 5):
            print("\nBye!")            
            
        else:
            print("\nInvalid Option!")
            print("Enter a number between 1 and 5.")            
    
Main()  #calling the main function that starts the program
    
#end of the program