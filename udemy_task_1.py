import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option no: 1
print(random.choice(friends))

# option no: 2
random_index = random.randint(0, 4)
print(friends[random_index])


