#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # Initialize maxProfit variable
    maxProfit = float("-infinity")

    # Loop over entire list, setting the buyPrice
    for index, buyPrice in enumerate(prices):
        
        # Loop over the list of prices that come after the buyPrice and set the sellPrice eachtime.
        # Only need to look at the prices that come after the buyPrice since we must sell after buying.
        for sellPrice in prices[index+1:]:
            profit = sellPrice - buyPrice
            if profit > maxProfit:
                maxProfit = profit

    return maxProfit

            
# print(find_max_profit([100, 90, 80, 50, 20, 10]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))