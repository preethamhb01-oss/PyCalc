
print("WELCOME TO CALCUPY V2 ..")
class Calculator :
  
    
    
    def add(a, b , c=0):
        print(a+b+c)
        
        
    def subtract(a,b, c=0):
        print(a-b-c)

    def mult(a, b , c=1):
        print(a*b *c)
        
        
    def div (a,b):
        
        if b!=0:
            print(a/b)
            
        else:
            print("denominator is not equal to zero")
            
a = int(input("enter first term : "))
b = int(input("enter second term : "))


            
c = Calculator

c.add(a , b)
class PowerOperator :
    def power(p):
        print(f"{p} square is : {p**2}")
        
p = int(input ("Enter the number get its Square :  "))

d=PowerOperator
d.power(p)

class Modulo:
    def Modulus(x, y):
        print(f"MODULE : {x%y}")
        
x = int(input("Enter the first term : "))
y = int(input("Enter second term : "))

m=Modulo
m.Modulus(x, y) 



