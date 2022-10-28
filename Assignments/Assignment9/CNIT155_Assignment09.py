#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program reads and writes to text files. The program reads the values from the sample file, performs statistical 
# analysis with them, and writes the results to another text file (output.txt). Exception handling is used in the code to
# prevent the program from crashing.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def Main():     #defined the main function
    
    try:    #try block to try the enclosed code
        readData = open("input.txt", "r")   #opened the text file and created an object for reading
        content = readData.readlines()
        
        outputData = open("output.txt", "w")
        
        lstNames = []   #empty lists
        lstScores = []
        temp = []
        
        for ctr in range(len(content)): #loop to split the content of the file and store in different lists
            temp = content[ctr].split(", ")
            lstNames.append(temp[0])
            lstScores.append(float(temp[1]))
        
        print("\nPrinting every content in the file...")
        print(lstNames)  
        print(lstScores)
        print("\nScores have been updated. Check the output file!")
        
        maxValue = max(lstScores)   #found max and min
        minValue = min(lstScores)
        
        outputData.write("The Maximum score is:"+str(maxValue)+"\n")    #max scores printed to the file
        for ctr in range(len(lstScores)):
            if(lstScores[ctr] == maxValue):
                maxOutput = (f"{lstNames[ctr]}, {lstScores[ctr]}\n")
                outputData.write(str(maxOutput))
                
        outputData.write("\nThe Minimum score is:"+str(minValue)+"\n")  #min scores printed to the file
        for ctr in range(len(lstScores)):
            if(lstScores[ctr] == minValue):
                minOutput = (f"{lstNames[ctr]}, {lstScores[ctr]}\n")
                outputData.write(str(minOutput))
        
        outputData.write("\nUpdated Score(s):\n")   #updated scores printing to the file
        for ctr in range(len(lstScores)):
            if(lstScores[ctr] == minValue):
                lstScores[ctr] = lstScores[ctr] + .5
                updatedMinValue = (f"{lstNames[ctr]}, {lstScores[ctr]}\n")
                outputData.write(updatedMinValue)  
        
        readData.close()    #closed
        outputData.close()
        
    except FileNotFoundError:   #except block if the file is not in the same folder
        print("The program failed to open the file. Make sure of the followings:")
        print("\tThe file to read is located in the same folder where this program is!")
        print("\tThe file's name is spelled correctly!")
Main()