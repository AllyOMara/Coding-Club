# Defining the function to translate the emoji
def emoji_translate(emoji_code):
  if 128511 < emoji_code < 128519:
    return ':-)'
  elif 128543 < emoji_code < 128546:
    return '>:-('
  elif emoji_code == 128546:
    return ":'‑("
  elif 128538 < emoji_code < 128542:
    return ':‑P'
  else:
    return "Sorry, I don't know that emoji!"

# Asks for user input
emoji = input("Emoji? ")

# Converts the emoji into ord
emoji_code = ord(emoji)

# Translates it using the function defined above
final_emoji = emoji_translate(emoji_code)

# Prints the final product
print(final_emoji)
