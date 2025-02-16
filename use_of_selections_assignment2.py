import random

degrees = random.randint(1,400)

if degrees > 100:
    print("Temperature is above boiling point")
    
    if degrees > 320:
        print("Temperature above smoke point")
    
else:
    print("temperature is low")
    
    #When the degrees are over 320 it prints both boiling and smoking.
    
    
    