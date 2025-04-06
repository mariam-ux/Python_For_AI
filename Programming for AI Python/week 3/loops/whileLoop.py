correctPss = "secret123"
inputPss = input("enter your password: ")
while inputPss != correctPss:
    print("incorrect")
    inputPss = input("enter your password: ")
print("password accepted")