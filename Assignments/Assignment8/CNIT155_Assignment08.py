#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: There are 3 pre-defined lists that store 6 different item names, IDs, and prices for products 
# sold in a store. 4 user-defined functions were made to perform certain tasks. Once debugging starts, the program 
# will display a) the products information, b) updated information, c) the averages of prices (before and after the 
# adjustment), and d) products <=$100.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def Discount(lst):  #defined the discount function
    update = [ctr * .7 for ctr in lst]
    return update   #returned update

def PrintInfo(lst1, lst2, lst3):    #defined the printinfo function
    for ctr in range(0, 6):
        print("\t", lst1[ctr], lst2[ctr], f"{lst3[ctr]:.2f}", sep = "\t")
    print()
        
def Search(lst1, lst2, lst3):   #defined the search function
    for ctr in range(0, 6):
        if(lst3[ctr] <= 100):
            print("\t", lst1[ctr], lst2[ctr], f"{lst3[ctr]:.2f}", sep = "\t")

def Average(lst):   #Defined the average function
    average = 0
    total = 0
    for ctr in range(len(lst)):
        total = total + lst[ctr]
    average = total / len(lst)
    return average  #retuned average

def Header():   #defined the header function
    print("\n*************************************************************")
    print("**********\t\t\t\t\t  ***********")
    print("**********\t\tAssignment 08\t\t  ***********")
    print("**********\t\t\t\t\t  ***********")
    print("*************************************************************")
    print()

def Main(): #defined the main function
    names = ["Book", "Tea", "Soda", "Shoes", "Mug", "Tv"]   #defined and initilized the lists
    ids = [100, 101, 102, 103, 104, 105]
    prices = [130.00, 153.00, 221.00, 117.00, 55.00, 200.00]
    
    Header()    #called the header function
    
    print("\t\tName\tID\tPrice")
    print("=============================================================")
    PrintInfo(names, ids, prices)   #called the printinfo function
    print("*************************************************************")
    
    print("\n====================\tAverages\t=====================")
    average = Average(prices)   #called the average function
    print(f"The average of prices before the discount is ${average:.2f}")
    
    print("\n*************************************************************")
    print("The prices have been adjusted!")
    
    discount = Discount(prices) #called the discount function
    print("\n\t\tName\tID\tPrice")
    print("=============================================================")    
    for ctr in range(0, 6):
        print("\t", names[ctr], ids[ctr], f"{discount[ctr]:.2f}", sep = "\t")
    print("*************************************************************")
    
    print("\n====================\tAverages\t=====================")
    discountAverage = Average(discount)     #called the average function
    print(f"The average of the prices after the discount is ${discountAverage:.2f}")
    
    print("\n===============\tProducts under <= $100\t=================")
    print("\t\tName\tID\tPrice")
    print("=============================================================")    
    Search(names, ids, discount)    #called the search function
    
Main()  #called the main function

#end of program