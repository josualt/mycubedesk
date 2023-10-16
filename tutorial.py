# tutorial.py
"""
this is a 
multiline comment
in python
"""
print('welcome to python')

name = input('what is your name?')
print(f"hello {name}")

age = input('are you a minor?')

if age == 'no':
    print('ondo sartzek ;)')
elif age == 'yes':
    print('FBI OPEN UP!!')
elif int(age) < 18:
    print('you creep')
else:
    print('who the fuck are you')

# loops

count = 5
while count > 0:
    print(count)
    count = count-1

for i in range(5):
    print(i)

friends = ['Petxi', 'Xolomo', 'Patri']
for friend in friends:
    print(friend)

# functions


def greed(name):
    print(f"hello {name}")


greed('puta mierda')
# petxi
