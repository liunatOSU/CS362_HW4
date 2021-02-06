def volume(length):
  if(isinstance(length, int) or isinstance(length, float)):
    if(not length > 0):
      print("Length of edge must be greater than 0")
      return None
    return length**3
  else:
    print("Invalid input")
    return None
