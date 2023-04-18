#program to perform arithmetic operations
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("Enter '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division, '%' for division")
option=input("Enter which operation to perform:")
if option=='+':
    ans=a+b
    ans=str(ans)
    print("Addition of two numbers is "+ans)
elif option=='-':
    ans=a-b
    ans=str(ans)
    print("Subtraction of two numbers is "+ans)
elif option=='*':
    ans=a*b
    ans=str(ans)
    print("Multiplication of two numbers is "+ans)
elif option=='/':
    ans=a/b
    ans=str(ans)
    print("Division of two numbers is "+ans)
elif option=='%':
    ans=a%b
    ans=str(ans)
    print("Modulo or remainder of two numbers is "+ans)
