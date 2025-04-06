#concatination (same as javascript)
#we cant concatinate string with int
#use format function to do so
s1 = 'Artificial{}'#curly braces acts as a place holder for the numbers
s2= 1000
print(s1.format(s2))

#ex2
s3 = 'im {}% sure i can finish the lesson in less than {} days'
s4 = 100
s5 = 2.5
print(s3.format(s4,s5))

#another way is to convert the number to string
print(s1 + " " + str(s2))