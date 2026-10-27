class Calculator :
    
    
    def add(a, b):
        print(a+b)
        
        
    def subtract(a,b):
        print(a-b)

    def mult(a, b):
        print(a*b)
        
        
    def div (a,b):
        
        if b!=0:
            print(a/b)
            
        else:
            print("denominator is not equal to zero")
            
a = int(input("enter first term : "))
b = int(input("enter second term : "))
            
c = Calculator

c.add(a , b)
