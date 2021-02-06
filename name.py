def name(first, last):
  if(isinstance(first, str) and isinstance(last, str)):
    if(not first or not last):
      print("Please enter a full name")
      return None
    return first + " " + last
  else:
    print("Invalid input")
    return None