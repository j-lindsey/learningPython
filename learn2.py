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
