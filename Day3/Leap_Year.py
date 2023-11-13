#!/usr/bin/env python3

# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"Leap year")
    else:
      print(f"Not leap year")
  else:
    print(f"Leap year")
else:
  print(f"Not leap year")
