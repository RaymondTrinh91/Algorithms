#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  moves = ["rock", "paper", "scissors"]
  results = []

  def combine(n, temp_array):
    if n == 0:
      results.append(temp_array) 
    else:
      for element in moves:
        combine(n-1, temp_array + [element])

  combine(n, [])

  return results

rock_paper_scissors(2)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')