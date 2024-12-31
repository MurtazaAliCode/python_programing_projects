import random

print("\t\t=================={project of Number Guessing Game}==================\n")

def get_random_number():
    guss_teh_num = random.randint(1, 10)
    guss = 0
    while guss != guss_teh_num:
        guss = int(input("Guess the number: "))
        if guss < guss_teh_num:
            print("Too low")
        elif guss > guss_teh_num:
            print("Too high")

    print("congratulation You guessed the number correctly")
get_random_number()



