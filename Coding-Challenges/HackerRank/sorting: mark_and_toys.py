# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&isFullScreen=true

# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.

# Complete the maximumToys function below.


def maximumToys(prices, k):
    budget = k
    toys = 0
    # sort array in ascending order so all the lower prices items are in the begining
    prices.sort()
    # start buying items at beg of arr until you cannot but anymore items
    for i in range(len(prices)):  # index prices array
        # if our budget is not below zero
        if budget >= 0:
            # go through each priced item in arr and subtract from budget k
            budget -= prices[i]
            # if our budget is above > 0 then buy, otherise don't
            if budget >= 0:
                toys += 1
    return toys
