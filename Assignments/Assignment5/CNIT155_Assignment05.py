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
    
    option = ""  #defining option variable
    
    while(option != "F"): #loops menu with computation options
        print("\n\t\t\tWhile Loops Practice")    #menu print statements
        print("==================================================================")
        print("A. Sum of odd natural numbers from 1 to N")
        print("B. Sum of squares of odd natural numbers from 1 to N")
        print("C. Sum of cubes of even natural numbers form 1 to N")
        print("D. Find the factorial of N")
        print("E. Print the multiplication of N")
        print("F. Exit")
        print("==================================================================")
    
        option = input("\nChose one of the following options to perform: ")   
    
        if(option == "A"): #if option a was chosen
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Displaying natural numbers from 1 to {n}")
            counter = 1 #defines variables
            total = 0
            while(counter < n):    #loops to add the counter
                print(counter)
                total += counter    #sum of incremented numbers
                counter += 2    #counter incremented
            print(f"\nThe sum of odd natural numbers from 1 to {n} is {total}")
        
        
        elif(option == "B"):   #if option b was chosen
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Displaying natural numbers from 1 to {n}")
            counter = 1
            total = 0
            while(counter <= n):    #loops to add the counter
                square = counter ** 2   #squared the numbers
                print(square)
                total += square     #added the squares
                counter += 2    #counter incremented
            print(f"\nThe sum of squares of odd natural numbers from 1 to {n} is {total}")            
            
            
        elif(option == "C"):   #if option c was chosen
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Displaying natural numbers from 1 to {n}")
            counter = 0
            total = 0
            while(counter < n):    #loops to add the counter
                counter += 2
                cube = counter ** 3 #cubed the even numbers
                print(cube)
                total += cube   #added up the even numbers
            print(f"\nThe sum of cubes of even natural numbers from 1 to {n} is {total}")            
            
            
        elif(option == "D"): #if option d was chosen
            n = int(input("Enter a natural number for N: "))    #stores n
            counter = 0
            fact = 1
            while(counter < n):    
                counter = counter + 1   #counter incremented
                fact = fact * counter
            print(f"\nThe factorial of {n} is {fact}")            
            
            
        elif(option == "E"):   #if option e was chosen 
            n = int(input("Enter a natural number for N: "))    #stores n
            print(f"Multiplication table of {n}")
            counter = 0
            fact = 1
            total = 1
            while(counter < 10):    
                counter = counter + 1   #incremented counter
                total = n * counter #calculation
                print(f"{n} x {counter} = {total}") #print multiplecation table format
            
            
        elif(option == "F"):  #allows the user to exit the loop
            print("Good Bye!")
            
            
        else:   #if no conditions were met the else will run
            print("\nInvalid input!\nChose an option between A and F")
    
main()  #calling the main function that starts the program

#end of the program