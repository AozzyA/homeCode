names = ['hi','bye','hey']
print (sorted(names,reverse = True))
print(names)
names[1] = 'hi'
print(names)
name = names.pop(1)
print(names)
print(name)
names.append(name)
print(names)

family = input('do you have any family members? ') == 'yes'
familyMembers = list()
while family:
    name = input('what is their name? ')
    familyMembers.append(name)
    family = input ("are there any more? ") == 'yes'

print(familyMembers)

for j in names:
    print()
