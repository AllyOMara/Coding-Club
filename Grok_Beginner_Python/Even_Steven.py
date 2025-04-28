# Count how many letters have an even Unicode value.
def even_count(word):
  count = 0
  for letter in word:
    unicode_num = str(ord(letter))
    if unicode_num[-1] in '24680':
      count = count + 1
  return count

# Gets the username via user input
username = input("Give me a name: ")

# Finds out whether the name is even or odd using even_count
first = even_count(username)
second = even_count('Steven')

# Finds the output based on whether the name is even or not
if first == second:
  print("Even Steven!")
else:
  print("That name is not as even as Steven.")
