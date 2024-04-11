items = [
    ("apple", 15),
    ("orange", 10),
    ("banana", 20)
]


# 1. List sort - Sort based on price using
# priceList = []
# fruitList = []

# for fruit, price in items:
#     priceList.append(price)
#     fruitList.append(fruit)


# Return price form

# def sortFunction(items):
#     return items[1]


# items.sort(key=sortFunction)
# print(items)


# 2. sorted function
# print(sorted(priceList))


# 3. Use Lambda function
# items.sort(key=lambda item: item[1])
# print(items)

# 4. Create a new list that contains only the price
# for price in items:
#     priceList.append(price[1])

# print(priceList)

# 5. Use map to return only price in ascending order
# x = map(lambda item: item[1], items)
# for item in items:
#     print(item)


# 6. Convert the map to list that contains only price
# prices = list(map(lambda item: item[1], items))
# print(prices)

# 7. Use filter to return only prices above 10
# filter(lambda item: item[1] >= 10, items)

# 8. Return the filtered item in a list
# x = list(filter(lambda item: item[1] >= 10, items))
# print(x)

# 9. Use list comprehension for the map expression above
# x = [item[1] for item in items]
# x.sort()
# print(x)

# 10.Use list comprehension for the filter expression above
# filtered = [item for item in items if item[1] >= 15]
# print(filtered)

# 11. Use zip function to combine two lists
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# x = list(zip("xyz", list1, list2))
# print(x)
