from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the self.storage.length(length of nodes) < self.capacity (limit set by instance)
        if self.storage.length < self.capacity:
        #    # add the item to the tail of the list
            self.storage.add_to_tail(item) 
            self.current = self.storage.head
        #    #  [a,b,c,d] is th tail
        #  head is still equal to none and tail has 5 items
        # if the length is equal to the capacity
        elif self.storage.length == self.capacity:
            head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if head == self.current:
            # the new tail becomes the new current
                self.current = self.storage.tail
                

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.current 
        list_buffer_contents.append(node.value)
        # TODO: Your code here
        if node.next is None:
            next_node = self.storage.head
        else:
            next_node = node.next
        
        while next_node != node:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node + self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
