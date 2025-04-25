# Finding what the word is from the user
Radio_Word = input('Radio message: ')

# Personalised message
if Radio_Word == 'ROGER':
  print('Message received')
elif Radio_Word == 'WILCO':
  print('Understood and will comply')
elif Radio_Word == 'OVER AND OUT':
  print('Ending transmission')
else:
  print('Unknown radio message! MAYDAY MAYDAY!')
 
