# Define the function triangle_area
def triangle_area(base, height):
  return(0.5 * int(base) * int(height))
  
# Testing
print(triangle_area(10, 6)) # Should output 30 or 30.0
print(triangle_area(5, 3)) # Should output 7.5
print(triangle_area(15,10)) # Should output 75 or 75.0
