# Creates the team name from the user's input
Team = input("Team name? ")

# Prints each letter in the team name, preceded by "give me" using an f string
for letters in Team:
  print(f"Give me {letters}")

# Prints "go " and the team name using an f string
print(f"Go {Team}!")
