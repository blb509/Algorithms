#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_max_prof = prices[1] - prices[0]
    current_min_buy = prices[0]
    current_max_sell = prices[1]
    for x in range(0, len(prices) - 2):
        for y in range(1, len(prices) - 1):
            if prices[y] - prices[x] > current_max_prof:
                current_max_prof = prices[y] - prices[x]
                current_min_buy = prices[x]
                current_max_sell = prices[y]
    return current_max_prof


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

