# Chris de Leon - CSC590
import functools

# list creator
def createList(rangeBegin, rangeEnd):
    rangeBegin = int(rangeBegin)
    rangeEnd = int(rangeEnd)
    givenList = []
    # to ensure rangeEnd value is included in the list, we must add 1 to it
    for i in range(rangeBegin, rangeEnd + 1):
        givenList.append(i);
    return givenList

# map function to find squares and cubes of even and odd nums respectively
def myFunction(item):
    if item % 2 == 0:
        return item * item
    if item % 2 != 0:
        return item * item * item

# applies map function to the givenList
mappedList = map(myFunction, (createList(0, 11)))

# converts mappedList to list for readability
# print(list(mappedList))

# reduce to locate largest number in list
print(functools.reduce(lambda a, b: a if a > b else b, mappedList))

