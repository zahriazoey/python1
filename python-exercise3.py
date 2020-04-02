name = ''
season = ''
result = ' '

sen_tence = 'Please fill in the blanks below:'
madlib = "___(name)___'s favorite season is ___(season)___"

print(sen_tence)
print (madlib)

name = input('What is your name? ')
season = input('What is your favorite season? ')

result = f"{name}'s favorite season is {season}"

print(result)