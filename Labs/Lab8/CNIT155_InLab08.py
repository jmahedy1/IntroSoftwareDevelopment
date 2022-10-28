#=================================================================
# Your Name & Lab Section: Jack Mahedy, Thursday 1:30pm
# Your Purdue Email: jmahedy@purdue.edu
# Program Description: This Python program allows users to enter prices in US dollars and converts them to
# Euros. The program computes the average of entered prices and finds prices under $50. Along with main() 
# functions, 4 user-defined functions are required to perform various tasks.

# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def UsdToEuro(lst):     #defined the USD to Euro conversion
    euro = []
    for i in lst:   #for loop to append the converted usd list values to the euro list
        euro.append(i * .85)
    return euro    #returned the euro list values


def PrintInfo(lst1, lst2):  #defined the printinto function
    for ctr in range(len(lst1)):    #loop to print the lists by the incremeted ctr variable
        print("\t", f"{lst1[ctr]:.2f}", "\t\t", f"{lst2[ctr]:.2f}")


def Average(lst1):  #defined the average function
    average = 0     #defined the variables
    total = 0
    for item in lst1:   #loop over the list to add up the total and find the average
        total = total + item
    average = total/len(lst1)
    return average      #return the average


def FindPrice(lst1, lst2):  #defined the findprice function
    for ctr in range(len(lst1)):    #for loop use incremeted value
        if(lst1[ctr] < 50):     #condition to check if the price is less than 50
            print("\t", f"${lst1[ctr]:.2f}", "\t", f"€{lst2[ctr]:.2f}")


def Main():     #defined the main
    usd = []
    euro = []
    numberOfPrices = 0
    
    
    while(True):    #loop to keep asking for values
        price = int(input("Enter a price in USD. Use -1 to stop data entry: "))
        if(price != -1):
            usd.append(price)
            numberOfPrices = numberOfPrices + 1
        else:
            break
    
    
    print(f"\nNumber of prices entered: {numberOfPrices}")
    
    
    euro = UsdToEuro(usd)   #called the conversion function
    print("\n\tUSD ($)\t\tEuro (€)")
    print("=======================================")
    PrintInfo(usd, euro)
    print("=======================================")
    
    
    print("\n===============Averages================")
    usdAvg = Average(usd)   #called the average function with usd
    euroAvg = Average(euro) #called the average function with euro
    print(f"The average of prices in USD is: ${usdAvg:.2f}")
    print(f"The average of prices in EURO is: €{euroAvg:.2f}")
    
    
    print("\n=======\tPrice(s) under $50 are\t======")
    print("\n\tUSD ($)\t\tEuro (€)")
    print("\t--------\t--------")
    FindPrice(usd, euro)    #called the find price function
    
    
Main()