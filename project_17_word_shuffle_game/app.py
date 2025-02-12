import random

def shuffle_word(word):
    return "".join(random.sample(word, len(word)))

def word_scramble_game():
    words = ["fruit", "computer", "game", "moon", "mobile"]
    original_word = random.choice(words)
    scrambled_word = shuffle_word(original_word)
    
    print("======{ Welcome to Word Scramble Game!}======")
    print("Unscramble this word: \n", scrambled_word)
    
    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ")
        if guess.lower() == original_word:
            print("Congratulations! You guessed it right.")
            return
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
    
    print(f"Sorry, you're out of attempts! The correct word was '{original_word}'.")

if __name__ == "__main__":
    word_scramble_game()
