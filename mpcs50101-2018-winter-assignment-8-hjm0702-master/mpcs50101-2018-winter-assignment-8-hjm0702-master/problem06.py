'''The code takes an extremely amount of time (literally a hour!!!!) when it handles the scrabble list txt file.
I intentionally made an adjustment on line 124~125, to make it shorter by finding a result from 1000 words.


For the question from the prompt, I assume a solution where I read in the words first and then sort the result after
uses a dictionary. Given my assumption is right, using a dictionary is less time consuming since it took n^2 time
when I create an ordered list.

'''

import time
import re

def allowed():
    '''find valid words given the text file'''
    f = open('scrabble_list.txt')
    refer = f.read().split()
    return refer

def calculation(word):
    '''calculate the scores of the validated words'''
    tile_score = {"a": 1, "c": 3,
    "b": 3, "e": 1,
    "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10}

    total = 0
    for char in word:
        total = total + tile_score[char.lower()]
    return total


class Node:
    def __init__(self, score):
        self.data = score
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData()[0] > item[0]:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def __str__(self):
        final_list = []
        current = self.head
        count = 0
        while current != None:
            count = count +1
            final_list.append(str(current.getData( )))
            current = current.getNext()
        return str(final_list)

    def __getitem__(self, key):
        final_list = []
        current = self.head
        count = 0
        while current != None:
            count = count +1
            final_list.append(str(current.getData( )))
            current = current.getNext()
        return final_list[key]

    def __len__(self):
        final_list = []
        current = self.head
        count = 0
        while current != None:
            count = count +1
            final_list.append(str(current.getData( )))
            current = current.getNext()
        return len(final_list)

if __name__ == "__main__":
    final_list = OrderedList()

    # for i in range(len(allowed())):
    for i in range(1000):
        n = allowed()[i]
        combi = []
        combi.append(calculation(n))
        combi.append(n)
        final_list.add(combi)

    print "=======Worst 10========"
    for i in final_list[0:9]:
        match = re.search(r'\'\w+\'', i)
        print match.group()

    print "=======Best 10========"
    best = []
    for i in final_list[-10:]:
        match = re.search(r'\'\w+\'', i)
        best.append(match.group())

    for i in range(len(best)):
        print best[9-i]
