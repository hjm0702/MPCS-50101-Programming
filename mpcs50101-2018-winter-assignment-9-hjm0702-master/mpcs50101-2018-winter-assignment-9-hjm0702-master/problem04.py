import random

def product_of_odds(list):
    return reduce(lambda x, y: x*y, filter(lambda x: x % 2, map(lambda x : x*1, list)))

if __name__ == "__main__":
    randomlist = [random.randint(1,10) for i in range(10)]
    # print randomlist
    print product_of_odds(randomlist)
