class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.start = Node(None)
    def add(self, data):
        newNode = Node(data)
        newNode.next = self.start
        self.start = newNode
    def access(self, index):
        curr = self.start
        ind = 0
        while(curr.data != None):
            if(ind == index):
                return curr.data
            ind += 1
            curr = curr.next
        return "Index out of bounds."
    def remove(self):
        if(self.start.data == None):
            print("Nothing left to remove")
        self.start = self.start.next
        

l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)

print(l1.access(0))
print(l1.access(1))
print(l1.access(2))
print(l1.access(3))

l1.remove()

print(l1.access(0))
print(l1.access(1))
print(l1.access(2))

l1.remove()
print(l1.access(0))
l1.remove()
print(l1.access(0))
l1.remove()

