import random

print("\t\t=================={project of computer guss the Number}==================\n")

import random

def computer_guess_number(x):
    high = x
    low = 1
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  
        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Invalid input. Please enter 'H', 'L', or 'C'.")
    
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# Example usage
computer_guess_number(10)


