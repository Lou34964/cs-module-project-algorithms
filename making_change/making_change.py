#!/usr/bin/python

import sys

def making_change(amount, denominations):

  # if ammount is less or equal to 1 then return 1
  if amount <= 1:
    return 1

  #silent else

  cache = [0] * (amount+1) # starting list of 0's
  cache[0] = 1 # set first value to 1

  # for each coin available 
  for coin in denominations:
    for higher_amount in range(coin, amount+1):
      # finding each way to make ammount with each denominations
      difference = higher_amount - coin
      ways = cache[difference]
      cache[higher_amount] += ways

  return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")