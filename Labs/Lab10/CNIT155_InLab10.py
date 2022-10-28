#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: We are using a text file and reading the contents, performing calculations, and writing to an output file.
# We use try and except to catch if the file is not in the same folder.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def Main():     #defined the main function 
    try:    #try block to catch errors
        inputFile = open("scores.txt", "r")
        outputFile = open("scores_stat.txt", "w")
        
        scores = inputFile.readlines()  #reading the lines
        scoresList = [float(item) for item in scores]    
        
        print("\nPrinting the contents of the file...")
        print(scoresList)
        
        maxValue = max(scoresList)  #performed the calculations
        minValue = min(scoresList)
        average = sum(scoresList) / len(scoresList)
        length = len(scoresList)
        
        maxValueText = (f"\nThe maximum scores is: {maxValue:.2f}")
        minValueText = (f"\nThe minimum scores is: {minValue:.2f}")
        averageText = (f"\nThe average of scores in the list is: {average:.2f}")
        lengthText = (f"\nThe number of scores in the list is: {length:.2f}")
            
        outputFile.write(lengthText)    #wrote to the file
        outputFile.write(averageText)
        outputFile.write(maxValueText)
        outputFile.write(minValueText)
            
        inputFile.close()   #closed the files
        outputFile.close()
        
    except FileNotFoundError:   #Except block to catch the errors
        print("The program failed to open the file. Make sure of the followings:")
        print("\tThe file to read is located in the same folder where this program is!")
        print("\tThe file's name is spelled correctly!")
Main()  #called the main function

#end of program