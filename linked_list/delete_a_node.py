class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.length += 1
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node
            # self.head = temp
            self.length += 1

    def delete_node(self, position):
        print(position)
        if self.head and position >= 0:
            if position == 0:
                self.head = self.head.next
            else:
                count = 0
                temp = self.head
                prev = None
                while temp:
                    if count == position:
                        break
                    count += 1
                    prev = temp
                    temp = temp.next
                if not temp:
                    print("No position found in a linked list")
                    return
                prev.next = temp.next
        else:
            print("LL is empty")

    def length_of_ll_recursive(self, node):
        if not node:
            return 0
        else:
            return 1 + self.length_of_ll_recursive(node.next)

    def print_linked(self):
        temp = self.head
        while temp:
            print(str(temp.data) + '->', end=' '),
            temp = temp.next
        print('None')
        print('linked list is of length ' + repr(self.length))


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.print_linked()
llist.delete_node(0)
llist.print_linked()
print(llist.length_of_ll_recursive(llist.head))
