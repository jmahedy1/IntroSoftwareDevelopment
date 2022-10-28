#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program recieves inputs from the user and converts them to float. Inputs are set to variables
# and get used to calculate the side are, bottom area, and volume. They are printed after.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

import math #imported the math library

def main(): #defined the main function
    
    depth1 = float(input("Enter a value for Depth1 (D1): "))    #ask user for D1 and D2 inputs
    depth2 = float(input("Enter a value for Depth2 (D2): "))
    
    if(depth1 < depth2):    #condition to see if D1 is less than D2
        width = float(input("Enter a value for Width (W): "))   #if D1 is less than D2 ask for width and length
        length = float(input("Enter a value for Length (L): "))
        print("\nCalculating...")
        
        sideArea = ((depth1 + depth2) * length / 2) #sideArea calculation
        
        d3 = (depth2 - depth1)  #D3 calculation
        hyp = (math.sqrt(math.pow(d3, 2) + math.pow(length, 2)))    #hyp calculation
        bottomArea = (hyp * width)  #bottom area cacluation using d3, hyp, and width
        
        volume = (sideArea * width) #volume calculation
        
        print(f"\nThe side area of the pool is: {sideArea:.2f}")    #prints the side area, bottom area, and volume of the pool
        print(f"The bottom area of the pool is: {bottomArea:.2f}")
        print(f"The volume of the pool is: {volume:.2f}")
    else:   #if d1 is greater than d2 print that the inputs are invalid
        print("Invalid input! D2 must be greater than D1!")
    
main()  #calling the main function that starts the program

#end of the program