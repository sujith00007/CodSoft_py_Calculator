num1=float(input ("Enter Value 1: " ))
num2=float(input ("Enter Value 2: "))
operator=input ("Choose Operator: ")
if(operator=='+'):
    print("Addition: ",num1+num2)
elif(operator=='-'):
    print("Subtraction: ",num1-num2)
elif(operator=='*'):
    print("Multiplication: ",num1*num2)
elif(operator=='/'):
    if(num2 == 0):
        print("Can't Divide By Zero")
    else:
        print("Division: ",num1/num2)
else:
    print("Enter valid operator")