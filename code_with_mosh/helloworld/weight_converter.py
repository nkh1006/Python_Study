weight = int(input("Weight: "))
unit = input("(L)bs of (K)g: ")
if unit.upper == "L":
  converted = weight * 0.45
  print(f"You are {converted} kilos")
else:
  converted = weight / 0.45
  print(f"You are {converted} pounds")  
