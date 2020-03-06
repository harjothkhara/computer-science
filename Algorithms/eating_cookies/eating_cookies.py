#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# with any amount of cookies in a jar what are the different paths that we can take
# how many options can we run if we go down a certain recursive path? make sure those options are included in your recursive cases. how many ways are there to reach your basecase(0 cookies)?


def eating_cookies(n, cache=None):
    # basecase
    if n == 0:
        return 1

    total_ways = 0
    # cases:
    # cookie monster can eat all 3 cookies all at once
    if n >= 3:
        total_ways += eating_cookies(n-3)
    # cookie monster can eat 2 cookies, then 1 cookie
    if n >= 2:
        total_ways += eating_cookies(n-2)
    # cookie monster can eat 1 cookie, then 2 cookies
    if n >= 1:
        total_ways += eating_cookies(n-1)

    return total_ways

# time complexity of 3^n (three recursive calls)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
