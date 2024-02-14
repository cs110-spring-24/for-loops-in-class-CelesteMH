import random

heads = 0
tails = 0

for flip in range(100):         #for flip in range(0,100,1):         or      for flip in range(1,100):
    result = random.randint(1,2)
    if (result == 1):
        print("Heads")
        heads += 1              # heads = heads + 1
    else:
        print("Tails")
        tails += 1              # tails = tails + 1

print(f"You had {heads} heads and {tails} tails")