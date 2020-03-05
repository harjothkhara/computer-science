#!/usr/bin/python

import argparse


# def find_max_profit(prices):
#     current_min = prices[0]
#     for i in range(0, len(prices) - 1):
#         for j in range(0, len(prices) - 1):
#             if prices[j] < prices[j-1]:
#                 current_min = prices[j]
#             if prices[j] > prices[j-1]:
#                 current_max = prices[j]
#                 max_profit_so_far = current_max - current_min
#     return max_profit_so_far

# goal: max profit from a single buy and sell order
# - find max difference between the smallest and largest prices
# - max profit at each iteration ( buy price - sell price)

def find_max_profit(prices):
    profit = None
    # must first buy before selling
    # i will track buy orders
    for i in range(0, len(prices)):  # buy index
        # j will track sell orders
        for j in range(i+i, len(prices)):  # sell index
            # initialize buy and sell price
            buy_price = prices[i]
            sell_price = prices[j]
            # initialize our profit from the first iteration
            if profit == None:
                profit = sell_price - buy_price
            # checking at each subsequent iteration if the profit is greater than the last
            elif (sell_price - buy_price) > profit:
                profit = sell_price - buy_price
    return profit


if __name__ == '__main__':
            # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
