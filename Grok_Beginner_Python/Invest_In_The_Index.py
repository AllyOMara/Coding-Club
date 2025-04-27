# Getting the phrase from the user's input
phrase = input("Secret phrase? ")

# Getting the 1st, 2nd, 2nd last, and last letters
first = phrase[0]
second = phrase[1]
second_last = phrase[-2]
last = phrase[-1]

# Printing the final message
print("The treasure is in the " + first + second + second_last + last + "!")
