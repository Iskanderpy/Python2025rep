count = 0  

while True:  
    num = int(input("Enter an integer (negative number to stop): "))  
    if num < 0:  
        break   
    print("You entered:", num)  
    count += 1  

print("Total iterations:", count)
