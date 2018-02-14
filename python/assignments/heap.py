
"""
This progrom calculates the min heap and max
heap of a given data also performing operations like
(i) Insertion
(ii) Deletion of max from max heap
(iii) Deletion of min from min heap

"""
MAXI = True


class Heap:
    """
    This is the class that contains all the heap functions
    """

    heap = [0]

    def insert(self, inp):
        """
        takes in the input as single element and appends in heap
        """
        self.heap.append(inp)
        if MAXI is False:
            self.min_the_heap(len(self.heap) - 1)
        else:
            self.max_the_heap(len(self.heap) - 1)
        # self.max_the_heap()

    def max_the_heap(self, index):
        """
        This computes the max heap using recurssion
        """
        parent = index // 2
        if index <= 1:
            return self.heap
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.max_the_heap(parent)
        else:
            self.max_the_heap(parent)

    def min_the_heap(self, index):
        """
        This computes the max heap using recurssion
        """
        parent = index // 2
        if index <= 1:
            return self.heap

        elif self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            self.min_the_heap(parent)
        else:
            self.min_the_heap(parent)

    def delmax(self):
        """
        This deletes the max element from the max heap
        """
        self.swap(1, (len(self.heap) - 1))
        self.heap.pop()
        self.place_down()

    def delmin(self):
        """
        This deletes the min element from the min heap
        """
        self.swap(1, (len(self.heap) - 1))
        self.heap.pop()
        print(self.heap)
        self.place_down_min()

    def place_down_min(self, index=1):
        """
        This pushes down the top most element making sure that
        the heap stucture is maintained in case of min heap
        """
        left = index * 2
        right = index * 2 + 1
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
            self.place_down_min(smallest)

    def place_down(self, index=1):
        """
        This pushes down the top most element making sure that
        the heap stucture is maintained in case of max heap
        """
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.place_down(largest)

    def swap(self, ind, par):
        """
        swaps the given two argument
        """
        self.heap[ind], self.heap[par] = self.heap[par], self.heap[ind]

    def show_tree(self):
        """
        prints the tree
        """
        print(self.heap[1:])


if __name__ == '__main__':

    CLASS_VAR = Heap()
    # instatiating class variable

    print("Min heap(0) or Max Heap(1)")
    MAXI = input()
    CHOICE = 0

    while CHOICE != 5:
        print("Choice :'\t'1.insert'\t'2.Print heap'\t'3.Delete min'\t'4.Delete max'\t'5.Break")
        CHOICE = int(input())

        if CHOICE == 1:
            LIST_INPUT = input("Enter the element in the form of list:  ")
            for b in LIST_INPUT:
                CLASS_VAR.insert(b)

        elif CHOICE == 2:
            CLASS_VAR.show_tree()

        elif CHOICE == 3:
            if MAXI is False:
                CLASS_VAR.delmin()
                CLASS_VAR.show_tree()

            else:
                print("This is Max heap...Cannot delete Min")

        elif CHOICE == 4:
            CLASS_VAR.delmax()
            if MAXI is True:
                CLASS_VAR.show_tree()
            else:
                print("This is Min heap...Cannot delete Max")
        else:
            break
