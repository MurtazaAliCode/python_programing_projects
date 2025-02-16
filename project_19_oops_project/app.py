import time
import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.thirst = 50
        self.happiness = 50
        self.energy = 50
    
    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        print(f"{self.name} is eating... Hunger decreased!")
        self.animate("eating")
    
    def drink(self):
        self.thirst = max(0, self.thirst - 20)
        print(f"{self.name} is drinking... Thirst decreased!")
        self.animate("drinking")
    
    def play(self):
        if self.energy > 10:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 10
            print(f"{self.name} is playing! Happiness increased!")
            self.animate("playing")
        else:
            print(f"{self.name} is too tired to play!")
    
    def sleep(self):
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} is sleeping... Energy restored!")
        self.animate("sleeping")
    
    def status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/100")
        print(f"Thirst: {self.thirst}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100\n")
    
    def live(self):
        self.hunger = min(100, self.hunger + random.randint(5, 15))
        self.thirst = min(100, self.thirst + random.randint(5, 15))
        self.happiness = max(0, self.happiness - random.randint(5, 10))
        self.energy = max(0, self.energy - random.randint(5, 10))
    
    def animate(self, action):
        animations = {
            "eating": "(˘▽˘)っ🍎",
            "drinking": "(￣▽￣)ノ🥤",
            "playing": "(>‿◠)✌",
            "sleeping": "(-_-)zzz"
        }
        print(animations.get(action, "(・_・;)"))
        time.sleep(1)

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Dog"
    
    def bark(self):
        print(f"{self.name} barks: Woof! Woof!")

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Cat"
    
    def meow(self):
        print(f"{self.name} meows: Meow~")

def choose_pet():
    print("Choose a pet:")
    print("1. Dog")
    print("2. Cat")
    choice = input("Enter choice: ")
    name = input("Enter your pet's name: ")
    
    if choice == "1":
        return Dog(name)
    elif choice == "2":
        return Cat(name)
    else:
        print("Invalid choice, defaulting to Dog.")
        return Dog(name)

def main():
    pet = choose_pet()
    
    while True:
        pet.status()
        print("What would you like to do?")
        print("1. Feed")
        print("2. Give Water")
        print("3. Play")
        print("4. Let Sleep")
        print("5. Special Action")
        print("6. Quit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.drink()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            pet.sleep()
        elif choice == "5":
            if isinstance(pet, Dog):
                pet.bark()
            elif isinstance(pet, Cat):
                pet.meow()
        elif choice == "6":
            print("Goodbye! Take care of your pet!")
            break
        else:
            print("Invalid choice, try again.")
        
        pet.live()
        time.sleep(1)

if __name__ == "__main__":
    main()