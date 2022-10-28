#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program makes a GUI which display a book title, 
# number of "A" and "a", and the number of words in the title. 

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
#imported other python files
from graphics import *
from button import *

def main():

    # Create a window with 600 * 450 dimension.
    Window = GraphWin("Assignment 10", 500, 400)
    
    # Create a title for this program
    title = Text(Point(220,25), "Manipulating String in Python")
    title.setSize(20) #set the title's font size to 20
    title.setStyle("bold") #make the title bold
    title.setTextColor("Purple") #make the title purple!
    title.draw(Window) #now draw it on the window!
    
    #Create a label
    label1 = Text(Point(90,60), "Enter a title of a book:")
    label1.setSize(15)
    label1.setStyle("bold")
    label1.draw(Window)
    
    #Create an input textbox for strings that will be entered by the user
    inputBox = Entry(Point(280,60), 20)
    inputBox.setSize(15)
    inputBox.setFill("white")
    inputBox.draw(Window)
    
    #Create a display box to print the results
    display = Rectangle(Point(70, 100), Point(380, 350))
    display.draw(Window)
    
    #Create a button to receive the user's input
    btn = Button(Window, Point(410, 60), 50, 30, "Enter")
    btn.activate() #Activate Enter button
    
    #Create a button for exit
    quit = Button(Window, Point(410, 100), 50, 30, "Exit")
    quit.activate() #Activate Exit button
    
    rst1 = Text(Point(200,110), "")
    rst1.setSize(15)
    rst1.draw(Window)
    
    rst2 = Text(Point(200, 130), "")
    rst2.setSize(15)
    rst2.draw(Window)
    
    rst3 = Text(Point(210, 150), "")
    rst3.setSize(15)
    rst3.draw(Window)
    
    while True:
        p = Window.getMouse()
        if btn.clicked(p): #When the Enter button is clicked
        
            #GUI design part is done!
            #Now get the string entered by the user and store it the variable, string!
            string=inputBox.getText()
            
            #Find how many a or As are in the entered string.
            count = 0
            for letter in string: #for loop check each letter in the string
                if("A" in letter or "a" in letter): #if the letter is in the string 
                    count += 1 #increment the counter
                
            #Make first letter of each word uppercase using .title()
            updatedString = string.title()
            
            #Find how many words in the entered string using .split()
            words = string.split(" ") #split entered string into list
            wordCount = len(words) #count number of words in list
            
            #Print the results as Desired Outputs in the display textbox
            rst1.setText(f"The title is: {updatedString}") #sets text to output box
            
            rst2.setText(f"There is/are {count} A/a(s).")
            
            rst3.setText(f"The number of words in the string is/are: {wordCount}")
        
        elif quit.clicked(p): #When the Exit button is clicked, it closes the window.
            return
    
main()