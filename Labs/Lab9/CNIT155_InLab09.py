#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This Python program takes the number of steps walked for 7 days and computes the miles walked 
# during the week. If the input is entered in an incorrect format, the program catches errors and outputs the 
# exception messages. Then it asks for input again until the user provides a valid input. Create a new .py file 
# and start writing code.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def StepsToMiles(lst):  #defined the step to miles function
    miles = [item / 2000 for item in lst]
    return miles    #returned the updated miles function

def Header():   #defined the header 
    print("\n*************************************************************")
    print("**********\t\t\t\t\t  ***********")
    print("**********\t  Step to Miles Calculator\t  ***********")
    print("**********\t\t\t\t\t  ***********")
    print("*************************************************************")
    print()
    
def Main(): #defined the main function
    stepsList = []  
    ctr = 1
    average = 0
    
    
    Header()    #called the header function


    while(len(stepsList) < 7):  #while loop to input the steps into the list until the length is 7
        try:    #check to see if there is an error when the user inputs values
            steps = int(input(f"Enter the number of steps for Day {ctr}: "))
            if(steps < 0):  #raises value error exception if it is a negitive number
                raise ValueError
            else:   # if positive it add the value to the list
                stepsList.append(steps)
                ctr = ctr + 1
        
        except ValueError:  #if there is a value error exception print this
            print()
            print("Exception: wrong value entered")
            print("Please enter an integer value in a correct format!\n")
    
    
    print("\n*** The number of miles you walked this week ***")     #loop to print the list in miles
    milesWalked = StepsToMiles(stepsList)
    for ctr in range(0, len(milesWalked)):
        print(f"Day {ctr + 1}: {milesWalked[ctr]:.2f} miles")
       
        
    total = sum(milesWalked)    #calculates total, average and prints the average
    average = total / len(milesWalked)  
    print(f"\nThe average of miles walked: {average:.2f}")
    print("\nEnd of the program")
    
            
Main()