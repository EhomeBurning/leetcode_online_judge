class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.


    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print(node.data)
            node = node.next


    def add_two_list(self, l1, l2):
        carry = 0
        root = n = node(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n = node(val)
        return root.next 

# initial l1 
l1 = linked_list()
l1.add_node(2)
l1.add_node(4)
l1.add_node(3)

l1.list_print()

# initial l2 
l2 = linked_list()
l2.add_node(4)
l2.add_node(6)
l2.add_node(5)

l2.list_print()
    

sum = linked_list()
solution = sum.add_two_list(l1, l2)
solution.list_print()
# if '__init__' == 'main':
#     main()

# def main():
#     list_print(root.next)









        