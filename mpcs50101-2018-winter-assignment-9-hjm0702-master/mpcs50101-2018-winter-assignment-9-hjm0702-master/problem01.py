map(lambda x: x ** 2, numbers)
'''O(n) since it will execute mathematical operations item by item in "numbers"'''

filter(lambda x: x % 2, numbers)
'''O(n) since it will validate an item one by one in "numbers"'''

reduce(lambda x,y: x + y, numbers)
'''O(n) since it will execute mathematical operations n-1 times when n is the number of items in "numbers"'''
