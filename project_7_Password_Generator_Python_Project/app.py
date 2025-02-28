import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']

print('Welcome to the PyPassword Generator!')

nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''
for i in range(1,nr_letters+1):
    charector = random.choice(letters)

    password += charector

for i in range(1,nr_symbols+1):
     charector += random.choice(symbols)

     password +=  charector

for i in range(1,nr_numbers+1):
    charector += random.choice(numbers)

    password +=  charector

print(password)