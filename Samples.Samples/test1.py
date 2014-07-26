
class PriorityQueue:
    def __init__(self, *args):
        self.items = []
        return super().__init__(*args)
    def isEmpty(self):
        return self.items.count == 0
    def Insert(self, item):
        self.items.append(item)

    def Remove(self):
        max = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[max]:
                max = i
        maxItem = self.items[max]
        self.items[max:max+1] = []
        return maxItem

q = PriorityQueue()
q.Insert(5)
q.Insert(2)
q.Insert(3)
q.Insert(1)
while q.isEmpty(): print (q.Remove)

"""
if __name__ == '__main__':
    main()
"""
