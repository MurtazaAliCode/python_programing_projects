import random

print("\t\t=================={project of computer guss the Number}==================\n")

def computer_guss_number(x):
    high = x
    low = 1
    feedback = ''
    # guess = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guss_number(10)