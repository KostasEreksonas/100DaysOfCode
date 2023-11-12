#!/usr/bin/env python3

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
_sum = 0
if size == "S":
  _sum += 15
elif size == "M":
  _sum += 20
elif size == "L":
  _sum += 25
if add_pepperoni == "Y":
    if size == "S":
        _sum += 2
    else:
        _sum += 3
if extra_cheese == "Y":
  _sum += 1
print(f"Your final bill is: ${_sum}.")
