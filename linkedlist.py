class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        
    def __repr__(self) -> str:
        return "< Node : %s >" % self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head.nextNode
        result = []
        result.append("[Head: %s]" % self.head.data)
        while current:
            if current.nextNode is None:
                result.append("[Tail: %s]" % current.data)
            else:
                result.append("[%s]" % current.data)
            
            current = current.nextNode
        return "-> ".join(result)


    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.nextNode

        return count

    def prepend(self, data):
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode

    def push_back(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        current = self.head
        while current.nextNode:
            current = current.nextNode
        current.nextNode = newNode

    def insert(self, data, index):
        if index == 0:
            self.prepend(data)
        if index > 0:
            newNode = Node(data)
            current = self.head
            position = index
            while position > 1:
                current = current.nextNode
                position -= 1

            newNode.nextNode = current.nextNode
            current.nextNode = newNode

    def delete(self, key):
        # if self.head.data == key:
        #     self.head = self.head.nextNode
        #     return self.head
        #     # self.head.nextNode = None
        # current = self.head.nextNode
        # found = False
        # prev = self.head

        # while current and not found:
        #     if current.data == key:
        #         found = True
        #         prev.nextNode = current.nextNode
        #     else:
        #         prev = current
        #         current = current.nextNode

        # return current
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.nextNode

            elif current.data == key:
                found = True
                prev.nextNode = current.nextNode
            
            else:
                prev = current
                current = current.nextNode
            
        current.nextNode = None

        return current
    
    def removeWindex(self, index):
        if index == 0:
            current = self.head
            self.head = current.nextNode
            current.nextNode = None
            return current
        else:
            current = self.head.nextNode
            prev = self.head
            # 1 2 3 4
            while index > 1:
                prev = current
                current = current.nextNode
                index -= 1;

            prev.nextNode = current.nextNode
            current.nextNode = None
            return current

    def at(self, index):
        if index == 0:
            return self.head
        current = self.head.nextNode
        while index > 1 and current:
            current = current.nextNode
            index -= 1;

        return current


    def search(self, data):
        if self.head.data == data:
            return self.head
        current = self.head.nextNode
        while current:
            if current.data == data:
                return current
            current = current.nextNode

        return None


ll = LinkedList()
ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
ll.prepend(4)
ll.insert(7, 1)
ll.push_back(0)
ll.push_back(10)
n = ll.search(10)
print(n)
print(ll)
# print(ll.removeWindex(3))
# print(ll)
print(ll.at(3))
# print(ll)
