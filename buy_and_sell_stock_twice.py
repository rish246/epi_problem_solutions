from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_profit, min_price = 0, float('inf')
    max_prices = [0, 0]
    price_cur_bracket = 0

    def insert_price(new_price):
        if max_prices[0] > max_prices[1]:
            max_prices[0], max_prices[1] = max_prices[1], max_prices[0]
        if max_prices[0] < new_price:
            max_prices[0] = new_price
        # print(max_prices)
    for price in prices:
        # print(max_prices)
        if price < min_price:
            insert_price(price_cur_bracket)
            min_price = price
            price_cur_bracket = 0
        else:
            price_cur_bracket = max(price_cur_bracket, price - min_price)
    # insert_price(price_cur_bracket)
    return sum(max_prices)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
    