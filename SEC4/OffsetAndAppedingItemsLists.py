Avengers = [
    "Steve Rogers",
    "Tony Stark",
    "Natasha Romanoff",
    "Bruce Banner",
    "Clint Barton",
    "Thor Odinson"
]

# Access item by index
print(Avengers[1])

# Replace an item in the list
Avengers[1] = "Tony Stank"
print(Avengers)

# Add an item at the end of the list
Avengers.append("Loki Laufeyson")
print(Avengers)

# Add multiple items (another list) at the end
Avengers.extend(["Maria Hill", "Nick Fury", "Agent Coulson"])
print(Avengers)

# Insert an item at a specific index
Avengers.insert(2, "Peter Parker")
print(Avengers)

# Remove a specific item by value
Avengers.remove("Bruce Banner")
print(Avengers)

# Remove and return the last item
Avengers.pop()
print(Avengers)

# Remove item at a specific index
Avengers.pop(2)
print(Avengers)

# Clear all items from the list
Avengers.clear()
print(Avengers)
Avengers = ["Steve", "Tony", "Natasha", "Thor", "Tony"]

# Count how many times an item appears
print(Avengers.count("Tony"))

# Find index of first occurrence
print(Avengers.index("Natasha"))

# Sort the list alphabetically
Avengers.sort()
print(Avengers)

# Reverse the list order
Avengers.reverse()
print(Avengers)

# Create a copy of the list
New_Avengers = Avengers.copy()
print(New_Avengers)
