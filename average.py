def average(lst):
  if(isinstance(lst, list)):
    if(not lst):
      print("List cannot be empty")
      return None
    if(all(isinstance(x, int) or isinstance(x, float) for x in lst)):
      return sum(lst) / len(lst)
    else:
      print("Elements must be integers or floats")
      return None
  else:
    print("Invalid input")
    return None
    