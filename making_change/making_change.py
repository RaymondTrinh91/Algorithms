#!/usr/bin/python

import sys

def making_change(amount, denominations):
  print(denominations[-1])
  if amount == 0:
    return 1
  elif amount < 0 or not denominations:
    return 0
  else:
    return sum(making_change(change, denominations[:-1]) for change in range(amount, -1, -denominations[-1]))


print(making_change(300, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")