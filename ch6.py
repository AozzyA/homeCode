ages = {'anthony':10, 'mia':7, 'jake':43, 'alin':43}
ages["anthony"] = [1, 2, 3]

for name, age in ages.items():
    print(name.title() + " is " + str(age))

for name in ages.keys():
    print(name.title())

for age in set(ages.values()):
    print(age)

