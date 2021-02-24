name = input('What is your name? ')
print('hellooooo ' + name)
#Fundamental Data typesT
#int - integer
print(2+4)
print(type(2+4))
#float - float point
print(type(9.9+1.1))
print(2**3) #2 to power of 3
print(3//4) #rounds value to integer
print(5%4) #remainder


#math functions
print(round(3.1)) #rounds number
print(abs(-20)) #returns absolute value
#operator precedence
print((5 + 4) * 10 / 2) #guess 45
print(((5 + 4) * 10) / 2) # guess 45
print((5 + 4) * (10 / 2)) #guess 45
print(5 + (4 * 10) / 2) #guess 25
print(5 + 4 * 10 // 2) # 25

print(bin(5)) #bin returns binary value
print(int('0b101',2))


counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *=2

#Before you click RUN, guess what the counter variable holds in memory!
print(counter) # guess 6
#bool - true/false
#str - string

#formatted strings
name = "joelle"
age = 3
print(f'hi {name}, You are {age} years old' )
print('hi {}, You are {} years old'.format(name, age))
print('hi {1}, You are {0} years old'.format(name, age))
print('hi {new_name}, You are {age} years old'.format(new_name='sally', age=100))

num = '01234567'
print(num[::-1]) #can be used to reverse a string
#list - 
#tuple
#set
#dict

#Classes - customized types

#Specialized Data Types - packages and modules from libraries