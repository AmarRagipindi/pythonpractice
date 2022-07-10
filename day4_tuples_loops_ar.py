inputPrices = (10, 20, 5, 70, 90)

highestDifference = 0
diff = 0
length = len(inputPrices)

# find the difference in forward fashion and always store the highest difference
for index in range(length):
    for innerIndex in range(length):
        if innerIndex != len(inputPrices)-1:
            diff = inputPrices[index] - inputPrices[innerIndex+1]
            if diff > highestDifference:
                highestDifference = diff
print(highestDifference)

