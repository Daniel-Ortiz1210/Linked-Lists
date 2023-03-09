class Node:
    def __init__(self, data,  next=None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next_node(self):
        return self.next
    
    def set_next_node(self, node):
        self.next = node


class LinkedList:
    
    def __init__(self, head):
        self.head = head
    
    def get_length(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next_node()
        
        return count

    def get_head_node(self):
        return self.head.data
    
    def get_tail_node(self):
        current = self.head

        if current.get_next_node() == None:
            return current.get_data()

        while current != None:
            if current.get_next_node() == None:
                return current.get_data()
            current = current.get_next_node()
    
    def get_middle_node(self):
        lenght = self.get_length()
        current = self.get_head_node()
        
        for i in range(lenght//2):
            current = current.get_next_node()
        
        return current.get_data()
    
    def get_node_by_position(self, position):
        current = self.head
        current_position = 0
        
        if position == 0:
            return current.get_data()
        
        while current != None:
            if current_position == position:
                return current.get_data()
            current_position += 1
            current = current.get_next_node()
    
    def search_node_by_value(self, value):
        current = self.head

        if current.get_data() == value:
            return current.get_data()
        
        while current != None:
            if current.get_data() == value:
                return current
            current = current.get_next_node()
        return "There is not a node with this value."

    
    def remove_at_the_beggining(self):
        current = self.head
        next = current.get_next_node()

        if next is None:
            self.head = None
        self.head = next
        current = None
    
    def remove_at_the_end(self):
        current = self.head

        if self.head is None:
            return "The Linked List is empty"
        
        while current != None:
            if current.get_next_node().get_next_node() == None:
                current.next = None
                break
            current = current.get_next_node()
    
    def insert_at_the_beggining(self, value):
        head = self.head
        new_node = Node(data=value)
        new_node.set_next_node(head)
        self.head = new_node

    
    def insert_at_the_end(self, value):
        tail = get_tail_node()
        new_tail = Node(data=value)
        tail.set_next_node(new_tail)
    
    def insert_at_the_middle(self, position, value):
        current = self.head
        lenght = self.get_length()
        new_node = Node(value)
        count = 0

        if position > lenght - 1:
            print('Prosition to large to insert')
            return

        while current != None:
            if position == 0:
                self.insert_at_the_beggining(value)
                return
            
            if count == position - 1:
                new_node.set_next_node(current.next)
                current.set_next_node(new_node)
                return
            
            count += 1
            current = current.next
    
    def print_linked_list(self):
        current = linked_list.head
        while current != None:
            print(current.get_data())
            current = current.get_next_node()
    


    
node1 = Node(data="A")
node2 = Node(data="B")
node3 = Node(data="C")
node4 = Node(data="D")
node5 = Node(data="E")
node6 = Node(data="F")


linked_list = LinkedList(node1)
linked_list.head.set_next_node(node2)
node2.set_next_node(node3)
node3.set_next_node(node4)
node4.set_next_node(node5)
node5.set_next_node(node6)

# Z - A - B - C - D - E - F

print(linked_list.get_head_node())