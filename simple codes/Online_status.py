# The aim of this challenge is, given a dictionary of people's online status,
# to count the number of people who are online. ;)


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

for i, g in statuses.items():
    if g == "offline":
        continue
    print(i, ':', g)