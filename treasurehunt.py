
# Treasure Hunt Kevin Vang

name = input("What is your name? ")

has_treasure = False
treasure_count = 0

print(f"Welcome to the treasure hunt, {name}!")
print("You are an explorer searching for treasures left by the gods.")
print("Your journey will be filled with challenges and mysteries.")
print("Good luck on your adventure!")

choice = input("Do you want to go left or right? ")

while choice != "left" and choice != "right":
    print("Please choose 'left' or 'right'.")
    choice = input("Do you want to go left or right? ")

if choice == "left":
    print("You head left into the dense forest.")
    print("You search the forest for treasure.")
    print("After walking for hours, you reach a dead end.")
    print("Unfortunately, you found nothing!")
    print("You turn around and decide to take the right path instead.")

    choice = "right"

if choice == "right":
    print("You head right towards the mountains.")
    print("As you climb the mountain, you notice a mysterious cave.")
    print("Inside the cave, you discover an ancient treasure chest!")

    action = input("Do you want to 'open' the chest or 'leave'? ")

    while action != "open" and action != "leave":
        print("Please choose 'open' or 'leave'.")
        action = input("Do you want to 'open' the chest or 'leave'? ")

    if action == "open":
        print("You carefully open the treasure chest.")
        print("Inside, you discover the legendary Millennium Puzzle!")

        has_treasure = True
        treasure_count = treasure_count + 1

        print(f"Treasures collected: {treasure_count}")

    elif action == "leave":
        print("You decide to leave the treasure chest behind.")
        print("You head home without finding out what was inside.")

if has_treasure == True:
    print(f"Congratulations, {name}!")
    print("You found the Millennium Puzzle and completed your treasure hunt!")
else:
    print(f"Your adventure has ended, {name}.")
    print("You did not collect the Millennium Puzzle.")