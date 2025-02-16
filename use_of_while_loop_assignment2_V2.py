count = 0  
student_number = 991794823
while True:  
    num = int(input("Enter an integer (Enter student number to stop): "))  

    if num == student_number:  
        print("cutoff point")  
        break 
    if num % 11 == 0:  #checks for multiples of 11
        continue  

    print("You entered:", num)  
    count += 1
   
print("Total iterations:", count)
