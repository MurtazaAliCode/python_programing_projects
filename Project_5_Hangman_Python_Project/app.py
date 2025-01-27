import random

print("\t\t======================={project of hangmen game}=========================\n")

word_list = ["apple","banana","orange","pinaaple"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
print("you have only 6 lives")

display = []
for i in range(len(chosen_word)):
    display += '_'

    print(display)

game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 5:
            print("""
            ______
            |   |
            |
            |
            |
            |___________""")
        elif lives == 4:
            print("""
            ______
            |   |
            |   0
            |
            |
            |___________""")
        elif lives == 3:
            print("""
            ______
            |   |
            |   0
            |   |
            |
            |___________""")  
        elif lives == 2:
            print("""
            ______
            |   |
            |   0
            |  /|\
            |   
            |___________""")        
        elif lives == 1:
            
             print("You lose")
             print("""
            ______
            |   |
            |   0
            |  /|\                       
            |  / \   
            |___________""")
            
        elif "_" not in display:
         game_over = True
         print("You win")    
        