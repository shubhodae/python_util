# lambda example

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newlist = list(map(lambda x: x + 5, a))
print(newlist)

newlist = list(filter(lambda x: x % 2 == 0, a))
print(newlist)
