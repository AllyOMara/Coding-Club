# Getting user input for the variable message
message = input("Message: ")

# Getting the 1st, 6th, and 12th letter (remember that you start counting at 0)
first = message[0]
sixth = message[5]
twelfth = message[11]

# Printing the secret message
print(first + sixth + twelfth)
