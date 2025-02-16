import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 100
        self.treasure = 0

    def search(self):
        if self.energy > 20:
            self.energy -= 20
            event = random.choice(["treasure", "trap", "nothing"])
            
            if event == "treasure":
                found = random.randint(10, 50)
                self.treasure += found
                print(f"🎉 You found {found} gold coins! Your total treasure is now {self.treasure}.")
            elif event == "trap":
                damage = random.randint(10, 30)
                self.health -= damage
                print(f"💀 Oh no! You fell into a trap and lost {damage} health!")
            else:
                print("🔍 You searched but found nothing...")

        else:
            print("⚡ You're too tired! Rest before searching again.")

    def rest(self):
        self.energy = min(self.energy + 30, 100)
        self.health = min(self.health + 20, 100)
        print("😴 You rested and regained health and energy.")

    def status(self):
        print(f"\n🏴‍☠️ {self.name}'s Status 🏴‍☠️")
        print(f"❤️ Health: {self.health} | ⚡ Energy: {self.energy} | 💰 Treasure: {self.treasure}\n")

# Game loop
player_name = input("Enter your adventurer's name: ")
player = Player(player_name)

print(f"\n🌴 Welcome, {player_name}, to the Treasure Hunt Adventure! 🌴")
time.sleep(1)

while player.health > 0:
    player.status()
    print("Choose an action: (1) Search for Treasure 💰 (2) Rest 😴 (3) Quit 🚪")
    choice = input("Enter your choice: ")

    if choice == "1":
        player.search()
    elif choice == "2":
        player.rest()
    elif choice == "3":
        print(f"🏆 You leave the island with {player.treasure} gold coins. Well played, {player.name}!")
        break
    else:
        print("❌ Invalid choice! Try again.")

    time.sleep(1)  # Smooth gameplay

if player.health <= 0:
    print(f"💀 {player.name} collapsed from exhaustion. Game over!")
