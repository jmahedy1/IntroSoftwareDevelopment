#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program asks for variables and then prints the variables and the data type
# The program also asks for the temp in farhenheight and converts it to celcius.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defined the main function
    
    print("\nThis is InLab02 for CNIT155 by Jack Mahedy\n") #prints the title
    
    students = int(input("Enter the number of students in CNIT155: ")) #Declars the variable, datatype, and gets the users input and sets it to the student variable
    print("The number of students in CNIT155 is", students) #Prints the input entered 
    print("The data type of the number of students is ", type(students)) #prints the variable datatype
    
    textbook = float(input("\nEnter the price of the textbook: ")) #recieves input, sets it to a variable with datatype float
    print(f"The price of the textbook is $ {textbook:.2f}") #Prints the input entered 
    print("The data type of the price is", type(textbook)) #prints the variable datatype
    
    fahrenheit = float(input("\nEnter today's temperaturein (\N{DEGREE SIGN}F): ")) ##recieves input, sets it to a variable with datatype float
    celsius = (fahrenheit - 32) * 5 / 9 #Cenverts Fahrenheit to celsius
    print(f"Today's temperature in Celsius is {celsius:.2f}\N{DEGREE SIGN}C") #Prints the conversion
    print("The data type of the tempurature is", type(fahrenheit)) #Prints the datatype
    
main()  #calling the main function that prints the sentences

#end of the program