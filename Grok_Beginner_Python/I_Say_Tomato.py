# Defining the check_temp function
def check_temp(temperature):
  # Checking temperature
  if temperature > 29:
    return('Too hot!')
  elif temperature < 21:
    return('Too cold!')
  else:
     return('OK')
# Testing
if __name__ == '__main__':
  print(check_temp(24)) # Should output OK
  print(check_temp(10)) # Should output Too cold

  # Add more testing here.
  print(check_temp(9)) # Should output Too cold
  print(check_temp(29)) # Should output OK
  print(check_temp(30)) # Should output Too hot
