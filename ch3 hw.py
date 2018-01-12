# Ask the last name.
nameFirst = input('what is your first name? ').strip().title()
familyName = input('What is your last name? ').strip().title()

# Ask if there are any family members.
familyAsk = input('do you have any family members? ').lower().strip() in ['yes', 'y']
familyMembers = list()

# Asking if there are any more family members then asking their names.
# After that puting it in a list.
while familyAsk:
    name = input('what is their name? ').strip().title()
    familyMembers.append(name)
    familyAsk = input ("are there any more? ").lower().strip() in ['yes', 'y']

print('The members of the ' + familyName + ' family:')
print('\t' + nameFirst + ' ' + familyName)
for name in familyMembers:
    print('\t' + name + ' ' + familyName)

# What the code is supposed to do.


# ask the last name.
# ask for family members.
# print last name.
# print each full name.
