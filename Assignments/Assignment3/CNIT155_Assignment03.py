#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program recieves coefficient inputs from the user 
# and puts them in quadratic equation form. The program also finds the 
# discriminant, roots, and smallest coefficient.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

import math #imported the math library

def main(): #defined the main function
    
    coefficient_a = float(input("Enter the coefficient a:"))    #recieve coefficient inputs from the user and store them as a float in variables
    coefficient_b = float(input("Enter the coefficient b:"))
    coefficient_c = float(input("Enter the coefficient c:"))
    
    print(f"\nQuadratic Equation is: {coefficient_a:.1f}*X^2 + {coefficient_b:.1f}*X + {coefficient_c} = 0")    #uses variables to print the quadratic equation
    
    discriminant = (coefficient_b ** 2) - (4 * coefficient_a * coefficient_c)   #calculation to find the discriminant
    print(f"\nThe Discriminant is: {discriminant:.2f}") #print statement to print the discriminant
    
    #if/else if chain to determine the amount of roots
    if (discriminant > 0):    #condition 1
        root_1 = ((-coefficient_b + math.sqrt(coefficient_b ** 2 - 4 * coefficient_a * coefficient_c)) / (2 * coefficient_a))   #calculation to find root 1
        root_2 = ((-coefficient_b - math.sqrt(coefficient_b ** 2 - 4 * coefficient_a * coefficient_c)) / (2 * coefficient_a))   #calculation to find root 2
        print(f"\nThe equation has two real roots: {root_1:.2f} and {root_2:.2f}")  #prints out the roots
    elif (discriminant == 0):   #condition 2
        root_3 = (-coefficient_b / (2 * coefficient_a)) #calcualtion to find the single root
        (print(f"\nThe equation has only one root: {root_3:.2f}"))  #prints the root
    else:   #condition 3
        print("\nThe equation has no real roots")   #prints if there are no roots
    
    #if/else if chain to find the smallest coefficent 
    if (coefficient_a < coefficient_b and coefficient_a < coefficient_c):   #condition 1
        print(f"\nThe smallest coefficient is: {coefficient_a:.2f}") #prints if coeficcient a is the smallest 
    elif(coefficient_b < coefficient_a and coefficient_b < coefficient_c):  #condition 2
        print(f"\nThe smallest coefficient is: {coefficient_b:.2f}")    #prints if coeficcient b is the smallest 
    else:   #Condition 3
        print(f"\nThe smallest coefficient is: {coefficient_c:.2f}")    #prints if coeficcient c is the smallest 
    
main()  #calling the main function that starts the program

#end of the program