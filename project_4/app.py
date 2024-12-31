print("\t\t============{project of rock paper sesior}===============\n")

import random

user_choise = int(input("enter your choise rock=1, paper=2,sesior=3"))
print(f"your choise is :{user_choise}")

if user_choise > 3:
    print("you did chose invalid num you fail")
else:
    computer_choise = random.randint(1,3)
    print("computer choise is:")
    print(computer_choise)
if computer_choise == user_choise:
    print("draw")
elif computer_choise ==1 and  user_choise == 2:
    print("you win")
elif user_choise == 1 and computer_choise == 2:
    print("computer win")

elif computer_choise == 3 and user_choise == 1:
    print("you win") 
elif computer_choise == 1 and user_choise == 3:
    print("computer win")             

