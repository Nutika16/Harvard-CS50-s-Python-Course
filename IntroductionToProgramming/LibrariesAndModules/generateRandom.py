import random 

# random.choice() function is commonly used to perform a random selection.
coin = random.choice(["heads" , "tails"])
print(coin)

# random.randint(a, b) returns a random integer between a and b.
num = random.randint(1,10)
print(num)

# random.shuffle(x) function is used for shuffling
cards = ["jack" , "queen" , "king"]
random.shuffle(cards)
for card in cards:
    print(card)