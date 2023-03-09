class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    
    def pop(self):
        temp = self.head
        deleted_node = None
        
        if not self.head:
            return False
        
        if self.length == 1:
            unique_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return unique_node.value
        
        while temp is not None:
            if temp.next.next is None:
                deleted_node = temp.next
                temp.next = None
                self.tail = temp
            temp = temp.next
            
        self.length -= 1 
        return deleted_node.value
    

    def prepend(self, value):
        new_head = Node(value)
        
        if self.length == 0:
            self.head = new_head
            self.tail = new_head
            self.length += 1
            return self.head.value
        else:
            new_head.next = self.head
            self.head = new_head
            self.length += 1
            return self.head.value
    

    def pop_first(self):
        old_head = None        
        
        if self.length == 0:
            return None
        
        if self.length == 1:
            head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return head.value
        
        new_head = self.head.next
        old_head = self.head
        self.head.next = None
        self.head = new_head
        self.length -= 1

        return old_head.value
    

    def get(self, index):
        temp = self.head
        pointer = 0
        
        if index > self.length - 1 or index < 0:
            return None
        
        while temp != None:
            if index == pointer:
                return temp
            pointer += 1
            temp = temp.next


    def set(self, index, value):
        if index > self.length or index < 0:
            return None
        
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return None


    
    def insert(self, index,  value):
        if index > self.length or index < 0:
            return None

        if index == 0:
            self.length += 1
            return self.prepend(value)
        
        if index == self.length:
            self.length += 1
            return self.append(value)
        
        new_node = Node(value)
        pre_node = self.get(index-1)
        if pre_node: 
            new_node.next = pre_node.next
            pre_node.next = new_node
            self.length += 1
            return True
        return None
    

    def remove(self, index):
        if index > self.length or index < 0:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()

        pre_node = self.get(index-1)
        pre_node.next = pre_node.next.next
        pre_node.next.next = None
        self.length -= 1
        return True
    

    def print_reverse_list(self):
        for index in range(self.length -1, -1, -1):
            print(self.get(index).value)
        
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



# before --- temp --- after ---  _  ---   temp.next

#   1    ---  2   ---   2   ---  0  ---    None     


#   3         3                             1




linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

linked_list.reverse()
linked_list.print_list()


