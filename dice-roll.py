import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for roll in range(100):
    result = random.randint(1,6)
    if result == 1:
        print("You Rolled a 1")
        one += 1
    elif result == 2:
        print("You Rolled a 2")
        two += 1
    elif result == 3:
        print("You Rolled a 3")
        three += 1
    elif result == 4:
        print("You Rolled a 4")
        four += 1
    elif result == 5:
        print("You Rolled a 5")
        five += 1
    else:
        print("You Rolled a 5")
        six += 1

print(f"You rolled {roll} times and got {one} ones, {two} twos, {three} threes, {four} fours, {five} fives, and {six} sixes")