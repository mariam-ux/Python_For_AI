fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
hasOrange = False
for fruit in fruits:
    if(fruit == 'orange'):
        print('found orange in the list')
        hasOrange = True
if(hasOrange == False): 
    print('sorry orange not found')