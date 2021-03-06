#conditional logic
is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you are old enough to drive')  #indentation is important in python
elif is_licenced:  #else if statement
    print('you can drive now')
else:
    print('checkcheck')

#ternary operator (shortcut if else)

#condition_if_true if condition else condition_if_else

is_friend = True

can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

#short circuiting

is_Friend = True
is_User = True

print(is_Friend and is_User)

if is_Friend or is_User:
    print('best friends forever')

print(not (True))

is_magician = False
is_expert = True

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('''at least you're getting there''')
elif not is_magician:
    print('you need magic powers')

print(
    True is 1
)  #is checks whether value stored in same location == checks value is same with type conversion is checks exact similar to === in javascript

print('1' is '1')

for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

user = {'name': 'Golem', 'age': 5006, 'can_swim': False}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for item in my_list:
    sum += item

print(sum)

#range
print(range(100))

for number in range(0, 50):
    print(number)

for _ in range(0, 10):  #_ is typically used when don't care about value
    print(_)

for _ in range(0, 10, 2):
    print(_)

for _ in range(2):
    print(list(range(10)))

for i, char in enumerate('Hellooooo'):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i, char)
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work')

