numbers = []#{'anthony't:[9, 10, 1], 'coleman':[26, 5], 'milan':[5, 10], 'jake':[8, 14]}
nameFirst = input('what is your first name? ').title()
favNumb = input('what are your favorite numbers? ')
print(nameFirst + '\'s favorite numbers are: ')
print('\t' + favNumb)

exit()
for name, favNumbers in numbers.items():  #Loop through the dictionary
    #print('\n')
    print(name + ' favorite numbers: ')
    #print('\t' + str(favNumbers))
    print('\t',end=' ')
    for an in favNumbers:
        print(an, end=' ')
#       for a in favNumbers:

   
########


print('JAKE' + str(numbers.get('anthony')))


name = "jake"
favNumbers = [9,10,11]

print (name)
for anthony in favNumbers:
    print(str(anthony))

