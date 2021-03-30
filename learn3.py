#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

for item in picture:
    for value in item:
        if value == 0:
            print(' ', end='')
        if value == 1:
            print('*', end='')
    print('')  #need a new line after every row

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)


def say_hello():
    print('hello')


say_hello()


def say_hello1(name, emoji):
    print(f'hellooo {name} {emoji}')


say_hello1('Andrei', 'smiley')
