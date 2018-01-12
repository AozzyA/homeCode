familyName = input('What is your last name: ').strip()
#print ('The members of the ' + familyName + ' family:')

answer = input('do you have any family members? ')

family = answer == 'yes' or answer == 'y'family

print (family)
familyMembers = list()
while family:
    name = input('what is their name? ')
    familyMembers.append(name)
    family = input ("are there any more? ") == 'yes'
