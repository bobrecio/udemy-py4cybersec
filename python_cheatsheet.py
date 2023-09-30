#import 

# variables
stringExample = "Hello there!"
numberExample = 12
isTrue = True

print("helllo world")
print(stringExample)

stringInput = input("Enter an integer") # all inputs are string type // ex=5
integerInput = int(input("Enter an integer")) # have to convert to int // ex=5

x = stringInput + 3 # ERROR
x = int(stringInput) + 3 # CORRECT RESULT // result 8

listExample = [1, 2, 3,"one", "two", "three"] 
# listExample[index] = value; index starts at 0

#if(then)-elif-else
if stringInput >= 5 and numberExample == 12 and isTrue != False:
    print(f('The value of x is {x}'))
elif isTrue == False:
    print(f('The value of isTrue is {isTrue}'))
else:
    print(stringInput, numberExample)
    
#while-loop
while y != 20:
    y = int(input(f'Enter a value for y >> '))

#for-loop
newListOfNumbers = [] #initialize a list
for number in range(1,21) 
# range starts at the first number and stops before the second number
    print(f('number is {number}')) # loops 1..20
    newListOfNumbers.append(number) 
    # adds the numbers in the range as items to the list
    
for item in listExample:
    print(f(This itme is {item})) # iterates through the list and assigns each to 'item'
    
# dictionary - {key:value}
person = {
    'name':'Bob',
    'job':'sysadmin',
    'age': 50,
    'isEmployed': True,
    'hobbies':['fishing','eating','Linux','cooking','tv']
}

print(person) # shows all values
print(person['name']) # shows the value of the name key
person['likesFishing'] = True # appends this key-value pair
print(person['hobbies'][2]) # shows the 2nd index of the hobbies list // 'Linux'

# FUNCTIONS 
def add(num1, num2):
    result = num1 + num2
    return result

print(add(1,2)) # functions must be define before they are called

