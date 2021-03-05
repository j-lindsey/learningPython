name = input('What is your name? ')
print('hellooooo ' + name)
#Fundamental Data typesT
#int - integer
print(2 + 4)
print(type(2 + 4))
#float - float point
print(type(9.9 + 1.1))
print(2**3)  #2 to power of 3
print(3 // 4)  #rounds value to integer
print(5 % 4)  #remainder

#math functions
print(round(3.1))  #rounds number
print(abs(-20))  #returns absolute value
#operator precedence
print((5 + 4) * 10 / 2)  #guess 45
print(((5 + 4) * 10) / 2)  # guess 45
print((5 + 4) * (10 / 2))  #guess 45
print(5 + (4 * 10) / 2)  #guess 25
print(5 + 4 * 10 // 2)  # 25

print(bin(5))  #bin returns binary value
print(int('0b101', 2))

counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *= 2

#Before you click RUN, guess what the counter variable holds in memory!
print(counter)  # guess 6
#bool - true/false
#str - string

#formatted strings
name = "joelle"
age = 3
print(f'hi {name}, You are {age} years old')
print('hi {}, You are {} years old'.format(name, age))
print('hi {1}, You are {0} years old'.format(name, age))
print('hi {new_name}, You are {age} years old'.format(new_name='sally',
                                                      age=100))

num = '01234567'
print(num[::-1])  #can be used to reverse a string
quote = 'to be or not to be'

print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))  #finds index of first occurance of text
print(quote.replace('be', 'me'))  #does not change the original string
print(quote)

#type conversions
birth_year = input('what year were you born? ')
age = 2021 - int(birth_year)
print(f'your age is {age}')

username = input('What is your username? ')
password = input('Please enter your password ')
sec_password = '*' * len(password)

print(
    f'{username}, your password {sec_password} is {len(password)} letters long'
)

#list -
li = [1, 2, 3, 4, 5]
li2 = [1, 2, 'a', True]  # can have multiple variable types
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
print(
    amazon_cart[0:3])  #list slicing creates new list does not change original
print(amazon_cart)

# using this list:
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!
print(basket[1][1][0])

#list methods
#adding
basket1 = [1, 2, 3, 4, 5]
new_list = basket1.append(100)  #append changes list in place
new_list = basket1
print(basket1)
print(new_list)
basket1.insert(4, 100)  #modifies array in place
print(basket1)
basket1.extend([100, 101])
print(basket1)

#removing
basket1.pop()  #removes last item
print(basket1)
basket1.pop(0)  #removes item at 0 index
print(basket1)
basket1.remove(4)  #removes the number 4 in the list
print(basket1)
#basket1.clear()
print(basket1)  #removes all items in the new_list
print(basket1.index(2))

print(basket1.count(100))
basket1.sort()  #modifies existing array
print(basket1)
sorted(basket1)  #creates  new array

basket1.reverse()
print(basket1)
print(basket1[::-1])  #reverses list in new instance

print(list(range(1, 100)))
sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'jojo'])

print(new_sentence)

#list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)

#dictionary (hash table, objects)
dictionary = {'a': 1, 'b': 2}

print(dictionary['b'])

user = {'basket': [1, 2, 3], 'greet': 'hello'}
print(user.get('age'))
print(user.get('age',
               55))  #if age doesnt exist won't get erro when running code.

print('basket' in user)
print('basket' in user.keys())
print(user.items())

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.append(new_friend[0])
friends.sort()

print(friends)

#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
userprofile = {
    'age': 25,
    'username': 'joelle',
    'weapons': ['axe'],
    'is_active': True,
    'clan': '1'
}
#2 iterate and print all the keys in the above user.
print(userprofile.keys())
#3 Add a new weapon to your user
userprofile['weapons'].append('knife')
print(userprofile)
#4 Add a new key to include 'is_banned'. Set it to false
userprofile['is_banned'] = False  #can use user.update({'is_banned': False})
print(userprofile)
#5 Ban the user by setting the previous key to True
userprofile['is_banned'] = True
print(userprofile)
#6 create a new user2 my copying the previous user and update the age value and username value.
user2 = userprofile.copy()
print(user2)
user2['username'] = 'John'
user2['age'] = 50
print(user2)
print(userprofile)

#tuple are immutable
#benefit is can't be changed, good for communicating things that aren't modified
#faster than lists
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])
print(5 in my_tuple)

new_tuple = my_tuple[1:2]
print(new_tuple)
x, y, x, *other = (1, 2, 3, 4, 5)
print(my_tuple.count(2))
print(my_tuple.index(3))
print(len(my_tuple))

#set inordered collections of unique objects
my_set = {1, 2, 3, 4, 5, 5}
my_list = [1, 2, 3, 4, 5, 5]

my_set.add(100)
my_set.add(2)

print(my_set)
print(set(my_list))  # converts list to set of unique values

print(1 in my_set) #checks if 1 exists in my_set
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) #sets out the difference doesnt modify set
print(my_set.discard(5)) #modifies by removing value
print(my_set)

print(my_set.difference_update(your_set)) #modifies set
print(my_set)

print(my_set.intersection(your_set)) #intsection between two sets

print(my_set.isdisjoint(your_set)) #are they different sets

print(my_set.union(your_set)) #adds sets together without duplicates

my_set = {4,5}
print(my_set.issubset(your_set))

print(my_set.issuperset(your_set))
print(my_set.isupserset(my_set))





#Classes - customized types

#Specialized Data Types - packages and modules from libraries
