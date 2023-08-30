#write a prgamm to calculate the bill of user purchases iteam?

bill = 0
while (True):
    a = input("Write the amount you want to add and Press q to know your bill: \n")
    
    if a.isnumeric():
        bill = bill + int(a)
        
    elif a=="q":
        print("Your total bill is", bill)
        
    else:
        print("Error!")    
        break