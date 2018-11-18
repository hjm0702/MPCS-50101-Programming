class Deque:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def add_front(self, item):
        self.item.append(item)

    def add_rear(self, item):
        self.item.insert(0, item)

    def remove_front(self):
        return self.item.pop()

    def remove_rear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

# if __name__ == "__main__":
#     test = Deque()
#     print test.is_empty()
#     test.add_front("hi")
#     test.add_front(2)
#     test.add_rear(444)
#     print test
#     test.remove_front()
#     print test
#     test.remove_rear()
#     print test
#     test.size()
#     print test.is_empty()
