inputPrices = (10, 20, 5, 70, 90)

highestDifference = 0
diff = 0
length = len(inputPrices)
buy_day = 0
sell_day = 0

# find the difference in forward fashion and always store the highest difference
for index in range(length):
    for innerIndex in range(index+1, length):
        diff = inputPrices[innerIndex] - inputPrices[index]
        if diff > highestDifference:
            highestDifference = diff
            buy_day = index
            sell_day = innerIndex

print(f"Maximum Profit: {highestDifference}")
print(f"Buy on day {buy_day+1} at price {inputPrices[buy_day]}")
print(f"Sell on day {sell_day+1} at price {inputPrices[sell_day]}")

