import ast
# This is a boolean parser. It handles the following expressions

# True and True X
# True or True X
# True and False X
# True or False X
# False and False X
# False or True X
# False and True X
# False or False X

userTyped = input('Enter a boolean experession.').strip()
words = userTyped.split(' ')

a = words[1]

t1 = ast.literal_eval(words[0].title())
t2 = ast.literal_eval(words[2].title())

if a ==('or'):
    print('or')
    if t1 or t2:
        print('True')
    else:
        print('False')
else:
    print('and')
    if t1 and t2:
        print('True')
    else:
        print('False')

    
#if t1 and t2:
#    print("true1")
#elif t1 or t2:
#    print("true2")
    
