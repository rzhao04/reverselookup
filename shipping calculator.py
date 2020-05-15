firstItem = 10.95
rate = 2.95
numOfItems = int
numOfItems = input ("the num of items: ")
if numOfItems == 1:
    print ("$", firstItem)
if numOfItems > 1:
    cost = (numOfItems - 1) * rate
    finalCost = firstItem + cost
    print (finalCost)