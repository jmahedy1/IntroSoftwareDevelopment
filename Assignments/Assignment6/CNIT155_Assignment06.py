#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program asks the user what computation they would like to perform. The user selects what to perform, 
# enters their input, the program performs the computation, and the program displays the output.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defined the main function
    
    option = 0  #defined option variable
    
    while(option != 5): #while loop do keep the asking the user until they exit the program
    
        print("\n\tNested For Loops Lab")   #menu displaying the options
        print("=================================")
        print("1. A Multiplication table")
        print("2. N for N times with commas")
        print("3. The Table of Stars")
        print("4. The inverted Triangle")
        print("5. Exit")
        print("=================================")
    
        option = int(input("Choose one of the options to perform: "))   #store user input into the option variable
        
        if(option == 1):    #option 1 condition, computation, and output
            n = int(input("Enter a number for N: "))    #asks the user for input
            print(f"Displaying {n} x {n} of A Multiplication Table")
            for row in range(1, n + 1):
                for coll in range(1, n + 1):    #nested for loop to print the multiplication table
                    print(row * coll, end = " ")
                print()
                
        elif(option == 2):  #option 2 condition, computation, and output
            n = int(input("How many lines do you want to print?: "))    #asks the user for input
            for row in range(1, n + 1):
                for coll in range(row):
                    print(row, end = " ")
                    if((coll + 1) < row):   #if statement to enter the commas between the numbers
                        print(",", end = "")
                    else:
                        print("", end = "")
                print()   
                
        elif(option == 3):  #option 3 condition, computation, and output
            n = int(input("How many rows do you want to print the stars: "))    #asks the user for input
            print(f"Displaying {n} row(s) of Table of Stars")
            for row in range(1, n + 1):
                for coll in range(1, (n - row) + 1):
                    print(" ", end = " ")
                for coll in range(1, row + 1):
                    print("*", end = " ")
                print()
                
        elif(option == 4):  #option 4 condition, computation, and output
            n = int(input("Enter the size of the triangle of stars to print: "))    #asks the user for input
            print(f"Displaying {n} row(s) of stars of the Triangle")
            for row in range(n):
                for coll in range(row):
                    print(" ", end = "")
                for coll in range(2 * (n - row) - 1):
                    print("*", end = "")
                print()
                
        elif(option == 5):  #option 5 to exit out of the while loop
            print("Good bye!")
            
        else:   #if non of the conditions are met, it will ask the user to select 1-5
            print("Invalid Option!\nPlease choose an option between 1 and 5")
    
main()  #calling the main function that starts the program

#end of the program