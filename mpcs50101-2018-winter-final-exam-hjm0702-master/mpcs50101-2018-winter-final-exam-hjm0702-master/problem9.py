# Problem 9
#
#
# Write a function that removes duplicates from an unsorted
# linked list.   Your solution should use your own
# linked list implementation.

# Show an example of you function in action using the
# following list:
#
#   10, 12, 11, 11, 12, 11, 10
#
# After processing, the resulting list should become:
#   10, 12, 11

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

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def __getitem__(self,key):
        return self.head

    def __str__(self):
        final_list = []
        current = self.head
        count = 0
        while current != None:
            count = count +1
            final_list.append(str(current.getData( )))
            current = current.getNext()
        return str(final_list)

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
            if current.getData() >= item:
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


if __name__ == "__main__":
    testlist = [10, 12, 11, 11, 12, 11, 10]

    a = OrderedList()
    for i in testlist:
        if a.search(i) == "False":
            a.add(i)

    print a
