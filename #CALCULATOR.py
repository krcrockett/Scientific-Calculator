#CALCULATOR

#ADDITION

def addition ():
    print ("Addition")
    n = float(input("Enter the number:  "))
    t = 0 //Total number enter 
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate):  "))
    return [ans,t]

#SUBTRACTION

def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number:  "))
    t = 0 //Total number enter 
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate):  "))
    return [ans,t]

#MULTIPLICATION

def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number:  "))
    t = 0 //Total number enter 
    ans = 1 
    while n != 0:
        ans = ans * n 
        t+=1
        n = float(input("Enter another number (0 to calculate):  "))
    return [ans,t]

