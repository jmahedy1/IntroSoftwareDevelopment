#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program acts as a conversion tool. We use variables, 
# inputs, math calculation, and print.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defined the main function
    
    print("\t*************************************************") #Displays program header/title
    print("\t*\t      CNIT155 Assignment 02\t\t*")
    print("\t*\t\t\t\t\t\t*")
    print("\t*\t      Conversion Calculator\t\t*")
    print("\t*************************************************\n")
    
    username = input("Enter your full name: ") # stores name input in variable
    print("My name is", username)   #prints name variable 
    
    print("\n** 1st. Pounds to Kilograms conversion **")    #print convserion header
    pound = float(input("What is the weight in pounds to convert it to kilograms?: ")) #recieves input and stores variable
    kilo_1 = pound / 2.2046 #Pound to kilo conversion
    print(f"The weight entered in pounds is {pound:.2f}lb and it is {kilo_1:.2f}kg")  #prints variables
    
    print("\n** 2nd. Celsius to Fahrenheit conversion **")  #print conversion header
    celsius = float(input("Enter the Celsius temperature to convert it to Fahrenheit: ")) #recieves input and stores variable
    fahrenheit = (celsius * 9/5) + 32   #fahrenheit to celsius conversion
    print(f"The entered temperature is Fahrenheit is {celsius:.2f}C and it is {fahrenheit:.2f}F")   #prints variables
    
    print("\n** 3rd. Miles to Kilometers conversion **")    #print conversion header
    mile = float(input("Enter miles to convert it to kilometers: ")) #recieves input and stores variable
    kilo_2 = mile * 1.609344    #mile to kilometer conversion
    print(f"The entered distance in miles is {mile:.2f}mi and it is {kilo_2:.2f}km")    #displays results/variables
    
    print("\n** 4th. Feet and Inches to Centimeters conversion **") #print conversion header
    print("What is your height in feet and inches?")    #print question
    feet = float(input("Feet?: "))  #declare and store variables  
    inch = float(input("Inches?: "))    #declare and store variables 
    feet2 = feet * 12   #feet to inches conversion
    centimeter = (feet2 + inch) * 2.54  #inches to centimeter conversion
    print(f"The entered height is {feet:.0f} feet {inch:.0f} inch and it is {centimeter:.2f}cm")    #print results
    
main()  #calling the main function that prints the sentences

#end of the program