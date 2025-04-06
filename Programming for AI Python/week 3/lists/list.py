num = [1, 2, 3, 4, 5]
num.append(6)
print(num)
num.remove(num[1])
print(num)
num.remove(3)
print(num)
num.remove(num[-1])#-1 refers to the last element inthe list
print(num)

#slicing
num2 = [1, 2, 3, 4, 5, 6, 7, 8]
slice1 = num2[2:5]#from index 2 to index 4 
print(slice1)
num2[2:5] = [20, 30 , 40]#a way to modify a slice of a list
print(num2)

#insert
num3 = [1, 2, 4, 5]
num3.insert(2, 3)#first arg refers to the position and the second for the value
print(num3)

#pop
num3.pop(3)#arg refers to the index
print(num3)

#sort
num4 = [4, 8, 6 ,1, 9, 3, 5, 2, 7]
num4.sort()
print(num4)

#reverse
num4.reverse()
print(num4)

#multiplication
zero = [0] * 5
print(zero)
num5 = [1, 2] * 3
print(num5)