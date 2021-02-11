#!/usr/bin/python

import sys
#use itertools to to get random RPS
from itertools import product
def rock_paper_scissors(n):
  # Your code here

  #options for product
  options = ['rock', 'paper', 'scissors']

  #return list of random RPS based on ammount (n)
  return [list(sequence_of_moves) for sequence_of_moves in product(options, repeat=n)]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')