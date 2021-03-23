from typing import List
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyOrders = []
        sellOrders = []

        def processBuyOrder(price, amount):
            while sellOrders and amount:
                sell_price, sell_amount = sellOrders[0]
                if sell_price > price:
                    break

                if sell_amount > amount:
                    sellOrders[0] = (sell_price, sell_amount - amount)
                    amount = 0
                else:
                    heapq.heappop(sellOrders)
                    amount -= sell_amount

            if amount:
                heapq.heappush(buyOrders, (-1 * price, amount))

        def processSellOrder(price, amount):
            while buyOrders and amount:
                buy_price, buy_amount = buyOrders[0]
                buy_price = -1 * buy_price
                if buy_price < price:
                    break

                if buy_amount > amount:
                    buyOrders[0] = (-1 * buy_price, buy_amount - amount)
                    amount = 0
                else:
                    heapq.heappop(buyOrders)
                    amount -= buy_amount

            if amount:
                heapq.heappush(sellOrders, (price, amount))

        for price, amount, isSell in orders:
            if isSell:
                processSellOrder(price, amount)
            else:
                processBuyOrder(price, amount)

        num_buyOrder = sum([order[1] for order in buyOrders])
        num_sellOrder = sum([order[1] for order in sellOrders])
        return int((num_buyOrder + num_sellOrder) % (1e9 + 7))


if __name__ == "__main__":
    test_cases = [
        ([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]], 6),
        ([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]], 999999984),
        ([[23, 17, 1], [18, 27, 0], [21, 26, 1], [8, 17, 0], [
         13, 22, 1], [22, 21, 1], [2, 24, 1], [5, 7, 0]], 69)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.getNumberOfBacklogOrders(t[0])
        if res != t[1]:
            sol.getNumberOfBacklogOrders(t[0])
