# Ask first name.
nameFirst = input('what is your first name: ').strip()
# Ask if you have a midle name.
midleAsk = input('do you have a midle name yes or no: ').strip()

# Seting nameMidle to nothing.
nameMidle = ''

# What happens if you type yes to do you have a midle name.
if midleAsk.lower() in ['y', 'yes']:
    # Asking what your midle name is.
    nameMidle = input ("what is your midle name: ").strip()

# Ask last name 
nameLast = input('what is your last name: ').strip()
# Printing hello.
# First name.
# Midle name and last name.
print ('Hello ' + nameFirst.title() + ' ' + nameMidle.title() + ' ' + nameLast.title())
# Ask if you have a nickname
nickName = input ('do you have a nickname yes or no: ').strip()

# What happens if you type yes to do you have a nickname.
if nickName.lower() in ['y', 'yes']:
    # Ask what is your nickname.
    name4 = input ("what is your nickname: ").strip()
    # Printing hi and your nickname.
    print ('hi '.title() + name4.title())
