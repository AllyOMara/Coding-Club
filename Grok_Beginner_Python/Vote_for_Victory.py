# Defines the user's age using input, makes it an integer using int
user_age = int(input("How old are you? "))

# Checks the user's age
if user_age < 18:
  print("You are not old enough yet.")
else:
  print("You have to vote!")
