# Finding the user's serve speed
serve_speed = int(input("Serve speed? "))

# Based on information as of 2025 the world record serve was 263
# Due to the information above, anything over 263 is a new record
# Anything between 230 and 263 is top 20
# Anything below that outputs "Keep working on that serve."
if serve_speed > 263:
  print("New ATP record!")
elif serve_speed >= 230:
  print("Top 20!")
else:
  print("Keep working on that serve.")
