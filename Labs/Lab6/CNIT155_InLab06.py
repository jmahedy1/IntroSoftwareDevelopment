#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: In this program, the user will be prompted to enter three sides of a triangle and check if the given numbers 
# form a valid triangle. If they do not form a valid triangle,the user is prompted to input new numbers. If they do form a triangle, 
# the program then calculates the area. Afterwards, the smallest and largest side will be displayed. The program asks if the user 
# wants to compute again. The program will continue to loop until the user inputs enters N or n.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

import math #imported math

def PrintInfo():    #Personal info function
    
    print("*********************************")  #info print statements
    print("*\tJack Mahedy\t\t*")
    print("*\tjmahedy@purdue.edu\t*")
    print("*\tCNIT155 InLab06\t\t*")
    print("*********************************")    

def Validate(a, b, c):  #validating the triabgle function
    
    if(a + b > c and a + c > b and b + c > a):
        return True
    else:
        return False

def ComputeArea(a, b, c):   #computing the are finction
    
    s = (a + b + c) / 2     #half perimeter calculation
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))   #area calculation
    
    return area #returning the area
    
def FindMin(a, b, c):   #Finding the min function
    if(a <= b and a <= c):
        return a
    elif(b <= a and b <= c):
        return b
    else:
        return c
    
def FindMax(a, b, c):   #Finding the max function
    if(a >= b and a >= c):
        return a
    elif(b >= a and b >= c):
        return b
    else:
        return c    

def Main(): #defined the main function
    
    PrintInfo() #calling the personal info function
    
    while True:     #while loop to keep asking for the triangle sides if the triangle is invalid or if they user want to keep trying different triangles
        a = float(input("\nEnter the length of side A of a triangle: "))
        b = float(input("Enter the length of side B of a triangle: "))
        c = float(input("Enter the length of side C of a triangle: "))
        
        print("\nValidating a triangle...")
        
        if Validate(a, b, c) == True:   #if statement, calls the validate function, and checks if it is true 
            print("\nThis is a valid triangle")
            area = ComputeArea(a, b, c)
            print(f"The area of the triangle is {area:.2f}")
            
            min = FindMin(a, b, c)
            max = FindMax(a, b, c)
            
            print(f"The smallest side is {min:.2f} and the largest side is {max:.2f}")
        else:
            print("\nInputs cannot for a triangle. Please enter different numbers!")
            continue
        
        while True:     #while loop to ask the user if they want to compute again or not
            value = input("\nDo you want to compute again (Y/N): ")
            
            if(value == "N" or value =="n"):
                print("End of the program")
                return
            elif(value == "Y" or value == "y"):
                break
            else:
                print("Invalid Input")
                print("Press Y or N, Case-insensitive:")
    
Main()  #calling the main function that starts the program

#end of the program