num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operation = input("enter the operation desired(add, subt, mult, div): ")
operation = operation.lower();
if(operation == "add"):
    print(num1 + num2)
elif(operation == "subt"):
    print(num1 - num2)
elif(operation == "mult"):
    print(num1 * num2)
elif(operation == "div"):
    print(num1 / num2)
else: print("invalide operation")

