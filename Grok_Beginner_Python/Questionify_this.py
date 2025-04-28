# Replace the exclamation marks with question marks.
def questionify(text):
  questionified = text.replace('!', '?')
  return(questionified)

# Test prints
print(questionify('How did you do that!'))
print(questionify('Oh no!!! Why!'))
