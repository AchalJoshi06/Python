a=int(input("Enter the 1st Number:"))
b=int(input("Enter the 2st Number:"))

ch=input("Enter the Operation('+','-','*','/','%') :")
Sum=a+b
Sub=a-b
Mul=a*b
Div=a/b
per=a*(b/100)
if (ch =='+'):
    print(Sum)
elif (ch=='-'):
    print(Sub)
elif (ch=='*'):
    print(Mul)
elif (ch=='/'):
    if(b!=0):
        print(Div)
    else:
        print("Enter the valid values")
elif (ch=='%'):
    print(per)

else:
    print("Enter the valid operation!!")       
 