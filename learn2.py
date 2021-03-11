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
