grade = int(input("enter a grade between 100 and 0: "))
if(grade > 100 or grade < 0): 
    print("unvalide grade")
elif(grade <= 100 and grade >= 90):
    print("your score is A")
elif(grade < 90 and grade >= 80):
    print("your score is B")
elif(grade < 80 and grade >= 70):
    print("your score is C")
elif(grade < 70 and grade >= 60):
    print("your score is D")
elif(grade < 60 and grade >= 0):
    print("your score is F")
else: print("please enter an integer")