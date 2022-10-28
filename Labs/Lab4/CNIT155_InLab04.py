#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program prompts the user to select a loop option. Depending on what choice the user has picked
# the program will then perform various computations. Once the user is finished with all of the computation he can exit the program.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defined the main function
    
    option = 0  #defining option variable
    
    while(option != 6): #loops menu with computation options
        print("\n\t\t\tWhile Loops Lab")    #menu print statements
        print("==================================================================")
        print("1. Print all natural numbers between 1 and N")
        print("2. Add up all natural numbers between 1 and N")
        print("3. Add up all even natural numbers between 1 and N")
        print("4. Compute the sum of the square numbers between 1 and N")
        print("5. Compute the sum and average of the cube numbers between 1 and N")
        print("6. Exit")
        print("==================================================================")
    
        option = int(input("\nChose one of the following options to perform: "))   #store what the users choice was in a variable
    
        if(option == 1):
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Displaying natural numbers from 1 to {n}")
            counter = 1
            while(counter <= n):    #loops to add the counter
                print(counter)
                counter = counter + 1
        
        elif(option == 2):
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Display natural numbers from 1 to {n}")
            counter = 1
            total = 0
            while(counter <= n):    #loop to increment the counter
                print(counter)  #print the range of numbers
                total = total + counter
                counter = counter + 1
            print(f"The sum of numbers from 1 to {n} is {total}")   
        
        elif(option == 3):
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Display natural numbers from 1 to {n}")
            counter = 2
            total = 0
            while(counter <= n):
                print(counter)
                total = total + counter
                counter = counter + 2   #to find the even numbers
            print(f"The sum of the even numbers from 1 to {n} is {total}")  #print the sum
            
        elif(option == 4):
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Display natural numbers from 1 to {n}")
            counter = 1
            total = 0
            while(counter <= n):    #loop to increment the counter
                square = counter ** 2   # calculate the squares
                print(square)
                total = total + square
                counter = counter + 1
            print(f"The sum of the square numbers from 1 to {n} is {total}") #print sum           
            
        elif(option == 5):
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Display natural numbers from 1 to {n}")     #prints the range
            counter = 1 #defines counter and total
            total = 0
            while(counter <= n):    #loop to add the counter up
                cube = counter ** 3 #calculate cubes of numbers
                print(cube)
                total = total + cube    
                counter = counter + 1
            print(f"The sum of cubes from 1 to {n} is {total}")
            average = total / n # avg calculation
            print(f"The average of cubes of numbers from 1 to {n} is {average:.2f}")    #prints avg and range
            
        elif(option == 6):  #allows the user to exit the loop
            print("Good Bye!")
            
        else:   #if no conditions were met the else will run
            print("\nInvalid input!\nEnter a number between 1 and 6.")
    
main()  #calling the main function that starts the program

#end of the program