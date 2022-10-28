#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program asks for users desired calculation to perform.
# The program then asks for various length and perfors a calcualtion and prints the results.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

import math #imported the math library

def main(): #defined the main function
    
    print("\n\tArea and Volume Calculators")    #menu print statements
    print("============================================")
    print("A. Area of a Rectangle")
    print("B. Area of a Trapezoid")
    print("C. Volume of a Sphere")
    print("D. Volume of a Hexagonal Pyramid")
    print("E. Volume of an Octagonal Prism")
    print("============================================")
    
    choice = input("\nChoose one of the following option to calculate: ")   #store what the users choice was in a variable
    
    if(choice == "A" or choice == "a"): #choice a condition
        print("\nOption A. Area of A Rectangle")
        width = float(input("\nEnter the width of the rectangle: "))    #asks user for dimensions
        length = float(input("Enter the length of the rectangle: "))
        recArea = (width * length)  #calculation
        print(f"\nThe area of the rectangle is {recArea:.2f}")  #print area
        
    elif(choice == "B" or choice == "b"):   #choice b condition
        print("\nOption B. Area of a Trapezoid")
        shortBase = float(input("\nEnter the short base of the trapezoid: "))   #asks user for dimensions
        longBase = float(input("Enter the long base of the trapezoid: "))
        height = float(input("Enter the height of the trapezoid: "))
        trapArea = (((shortBase + longBase) / 2) * height)  #calculation
        print(f"\nThe area of the trapezoid is {trapArea:.2f}") #prints area
        
    elif(choice == "C" or choice == "c"):   #choice c condition
        print("\nOption C. Volume of a Sphere") 
        radius = float(input("\nEnter the radius of the sphere: ")) #asks user for dimensions
        sphVolume = (4/3 * math.pi * radius**3) #calculation
        print(f"\nThe volume of the sphere is {sphVolume:.2f}") #prints volume
        
    elif(choice == "D" or choice == "d"):   #choice d condition
        print("\nOption D. Volume of a Hexagonal Pyramid")
        hexBaseEdge = float(input("\nEnter the base edge of the hexagonal pyramid: "))  #asks user for dimensions
        hexPyramidHeight = float(input("Enter the height of the hexagonal pyramid: "))
        hexVolume = (math.sqrt(3) / 2 * hexBaseEdge ** 2 * hexPyramidHeight)    #calculation
        print(f"\nThe volume of the hexagonal pyramid is {hexVolume:.2f}")  #prints volume
        
    elif(choice == "E" or choice == "e"):   #choice e condition
        print("\nOption E. Volume of an Octagonal Prism")    
        octBaseEdge = float(input("\nEnter the base edge of the octagonal prism: "))    #asks user for dimensions
        octHeight = float(input("Enter the height of the octagonal prism: "))
        octVolume = (2 * (1 + math.sqrt(2)) * octBaseEdge ** 2 * octHeight) #calculation
        print(f"\nThe volume of the octagonal prism is {octVolume:.2f}")    #prints volume
        
    else:   #if no conditions were met theis else will run
        print("\nInvalid input!\nPlease enter you choice between A and E.")
    
main()  #calling the main function that starts the program

#end of the program