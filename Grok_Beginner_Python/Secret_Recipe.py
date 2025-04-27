# Gets the idea of the pie from the user's input as a string
Pie_Idea = input("Pie idea: ")

# Loops for each letter in the collected string
for letter in Pie_Idea:
  # Converts the letter into numbers using ord() and prints it
  code = ord(letter)
  print(code)
