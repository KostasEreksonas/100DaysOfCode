#!/usr/bin/env python3

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
split = input("How many people to split the bill? ")

print(f"Each person should pay: ${float(bill)*float(percentage)/int(split)}")
