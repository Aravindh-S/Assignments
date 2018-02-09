Maxi = True


class heap:
    heap = [0]

    def insert(self, ip):
        self.heap.append(ip)
        if Maxi == False:
            self.min_the_heap(len(self.heap) - 1)
        else:
            self.max_the_heap(len(self.heap) - 1)
        # self.max_the_heap()

    def max_the_heap(self, index):
        parent = index // 2
        if index <= 1:
            return (self.heap)
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.max_the_heap(parent)
        else:
            self.max_the_heap(parent)

    def min_the_heap(self, index):
        parent = index // 2
        if index <= 1:
            return (self.heap)

        elif self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            self.min_the_heap(parent)
        else:
            self.min_the_heap(parent)

    def delmax(self):
        self.swap(1, (len(self.heap) - 1))
        self.heap.pop()
        self.PlaceDown()

    def delmin(self):
        self.swap(1, (len(self.heap) - 1))
        self.heap.pop()
        print(self.heap)
        self.PlaceDownMin()

    def PlaceDownMin(self, index=1):

        left = index * 2
        right = index * 2 + 1
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
            self.PlaceDownMin(smallest)

    def PlaceDown(self, index=1):

        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.PlaceDown(largest)

    def swap(self, ind, par):
        self.heap[ind], self.heap[par] = self.heap[par], self.heap[ind]


a = heap()
print("Min heap(0) or Max Heap(1)")
Maxi = input()
Choice = 0
while(Choice != 5):
    print("Enter Choice :       1.insert     2.Print heap  3.Delete min  4.Delete max     5.Break")
    Choice = int(input())
    if Choice == 1:
        li = input("Enter the element in the form of list:  ")
        for b in li:
            a.insert(b)
    elif Choice == 2:
        print(a.heap[1:])
    elif Choice == 3:

        if(Maxi == False):
            a.delmin()
            print(a.heap[1:])
        else:
            print("This is Max heap...Cannot delete Min")
    elif Choice == 4:
        a.delmax()
        if(Maxi == True):
            print(a.heap[1:])
        else:
            print("This is Min heap...Cannot delete Max")
    else:
        break
