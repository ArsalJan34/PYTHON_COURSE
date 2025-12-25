import random
Avengers = [
    "Steve Rogers",
    "Tony Stark",
    "Natasha Romanoff",
    "Bruce Banner",
    "Clint Barton",
    "Thor Odinson"
]
print(random.choice(Avengers))

random_index =random.randint(0,6)
print(Avengers[random_index])

