class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_begining(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert_at_end(self, data):
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

    def insert_at_middle(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.length += 1
        else:
            temp = self.head
            while temp:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node
            self.head = temp
            self.length += 1

    def insert_after(self, data, check):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.length += 1
        else:
            temp = self.head
            new_node = Node(data)
            found = -1
            while temp.next:
                if temp.data == check:
                    print("found")
                    new_node.next = temp.next.next
                    temp.next = new_node
                    found = 1
                    self.length += 1
                    break
                if found != 1:
                    temp = temp.next
            if found != 1:
                if temp.data == check:
                    temp.next = new_node
                    self.length += 1
                else:
                    print("Element not found")

    def print_linked(self):
        temp = self.head
        while temp:
            print(str(temp.data) + '->'),
            temp = temp.next
        print('None')
        print('linked list is of length ' + repr(self.length))


if __name__ == '__main__':
    llist = LinkedList()
    while True:
        print("Select where to insert the element")
        print("1. Begining\n2. Ending\n3. After Specific element\n4. Print Linked List\n5. Exit")
        x = input("Enter you choise ")
        if x == 5:
            llist.print_linked()
            break
        elif int(x) > 5 or int(x) < 1:
            print("Please enter correct option\n")
        else:

            if x == 1:
                print("Enter the element ----- >")
                ele = input()
                llist.insert_at_begining(ele)
            elif x == 2:
                print("Enter the element ----- >")
                ele = input()
                llist.insert_at_end(ele)
            elif x == 3:
                print("Enter the element ----- >")
                ele = input()
                print("Enter the target element")
                tar = int(input())
                llist.insert_after(ele, tar)
            elif x == 4:
                llist.print_linked()
