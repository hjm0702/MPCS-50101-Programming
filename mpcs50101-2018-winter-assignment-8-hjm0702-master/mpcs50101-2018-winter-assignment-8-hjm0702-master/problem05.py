class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext

temp = Node(93)
print temp.getData()
# print temp.getNext

# print Node()

class Unorderedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def lengh(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = Unorderedlist()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print mylist.search(0)


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def lengh(self):
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
            if current.getData() > item:
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

'''
class Fridge:
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print "Fridge open"

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print 'Food in'
        else:
            print 'Cannot do that'

    def close(self):
        self.isOpened = False
        print 'Fridge closed.'

    def getdata(self):
        return self.foods

class Food:
    pass

if __name__ == "__main__":
    food = Fridge()
    food.open()
    food.put("apple")
    food.put("potato")
    print food.getdata()

'''
