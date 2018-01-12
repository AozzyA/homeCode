numbers = {'anthony':[9, 10, 1], 'coleman':[26, 5], 'milan':[5, 10], 'jake':[8, 14]}# a dictionary is used when one wants to get a vaule from a spesific key
#lists are used when one wants a ordird culectshun of vaules

for name, favNumbers in numbers.items():  
    #print('\n')
    print(name + ' favorite numbers: ')
    #print('\t' + str(favNumbers))
    print('',end='')
    for an in favNumbers:
        print(an, end=' ')
        for a in favNumbers:
            print()

abc = [1, 2, 3]
jake = abc[0:2]
print(abc)
print(jake)
xyz = ['hi', 'bye', 'hey']
xyz[0:1]

print(8888)
print(xyz[0:3])
