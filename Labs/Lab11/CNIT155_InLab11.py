#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This program reads from a given text file (books.txt) and writes the results to a new text file (books_analysis.txt). 
# The sample text file (books.txt) contains 20 titles of books. This program reads the titles from the sample file, performs string manipulations 
# with them, and writes the results to books_analysis.txt. Exception handling is also used to prevent the program from crashing. 

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def Main(): #defined the main function
    try:    #try block to catch errors and created file objects
        inputFile = open("books.txt", "r")
        outputFile = open("books_analysis.txt", "w")
        bookList = inputFile.readlines()
        
        print("\nPrinting the contents of the file...\n")   #printing to terminal 
        print(bookList)
    
        header1 = "========== Analysis Results =========="
        outputFile.write(header1)
    
        bookAmount = f"\n\n1. The number of books in the file: {len(bookList)}"
        outputFile.write(bookAmount)
        
        header2 = "\n\n2. Titles of Books which have more than 2 words:\n\n"    #split the list elemets to check if the length is greater than 2
        outputFile.write(header2)
        for item in bookList:
            splitItem = item.split(" ")
            if(len(splitItem) > 2):
                outputFile.write(item)
                
        header3 = "\n\n3. Organized Book Titles:\n\n"   #loop through the list and capitalize the first letter
        outputFile.write(header3)
        for item in bookList:
            titleItem = item.title()
            outputFile.write(titleItem)
        
        inputFile.close()   #close the files
        outputFile.close()
        
    except FileNotFoundError:   #except block to check if the file is present
        print("The program failed to open the file. Make sure of the followings:")
        print("\tThe file to read is located in the same folder where this program is!")
        print("\tThe file's name is spelled correctly!")        
    
Main()  #called main

#end of the program