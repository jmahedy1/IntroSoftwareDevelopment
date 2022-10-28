#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This Python program allows users to enter students’ GPAs and computes the
# average of entered GPAs. Create a new .py file and start writing code.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def Main(): #defined the main function
    
    students = int(input("\nHaw many students are there in your class?: "))
    studentName = []    #created emply strings
    studentGpa = []
    
    
    for ctr in range(0, students):  #loop to ask for the name and insert it into the list
        name = input(f"Input student #{ctr + 1} name: ")
        studentName.append(name)
        while True:     #while loop inside the for loop to loop the if conditions for the gpa
            gpa = float(input(f"Input student #{ctr + 1} GPA: "))
            if(gpa >= 0 and gpa <= 4):  #conditions for the GPA
                studentGpa.append(gpa)  #if true it will add the gpa to the gpa list
                break
            else:
                print("\nA GPA must be between 0 and 4.0 (both inclusive)!")    #if false it will print this
    
    
    print("=============== List ===============")   #header
    print("\tName\t\tGPA")
    print("     --------\t      ---------")
    for ctr in range(0, students):  #for loop to print the two lists at the counter interation
        print("      ", studentName[ctr], "\t\t", studentGpa[ctr])
    print("============================================")
    
    
    total = 0
    average = 0
    for ctr in range(len(studentGpa)):  #for loop to find the average 
        total = total + studentGpa[ctr]
        average = total / len(studentGpa)
    print(f"The average of the entered GPA's is: {average:.2f}")
    max1 = max(studentGpa)  #using the max function
    min1 = min(studentGpa)  #using the min function
    print(f"The maximum GPA is: {max1:.2f}")    #printing the max and min
    print(f"The minimum GPA is: {min1:.2f}")
    print("===========================================") 
    
Main()  #called the main