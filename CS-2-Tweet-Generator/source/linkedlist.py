#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
            Run Time:
            Worse Case O(n) l representing the linked list we loop through.
            Best case: O(1) if it's the first item.
            """
        # Loop through all nodes and count one for each
        node_counter = 0
        for item in self.items():
            node_counter += 1
        return node_counter
        
        # for current_node != None:
        #     count+=1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
            Run time: O(1) there's no loops because we the tail.
            """
        print("APPEND FUNCTION")
        new_node = Node(item)
        # edge case
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # confused by this? so what's the next exactly?
            new_node.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        
        # * Quality is a function that will be used to find the boolean value of
        # * a condition. For example, if "the" is in our linked list, it will 
        # * return true. This allows our quality function to be abstracted/generic.

        if self.is_empty():
            print("{} is not in linkedlist".format(quality))
            return None
        else:
            current_node = self.head
            # for item in self.items()
            #     if quality == item:
            #         return item
            for i in range(0, self.length()):
                if quality(current_node.data):
                    return current_node.data
                else:
                    current_node = current_node.next
            # more efficient ways of doin this?
    
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # keeping track of current node, last node and if node is found
        current = self.head
        last = None
        found_node = False
        # Loop through all nodes
        while current and found_node is False:
            # find one whose data matches given item
            if current.data == item:
                found_node = True
            else:
                # Update previous node to skip around node with matching data
                last = current
                current = current.next
        # if we got past the end of the list and did not find item
        if current is None:
            raise ValueError('Item not found: {}'.format(item))
        # if we are at the first node, delete by making next node first
        if last is None:
            self.head = current.next # what if current is None
        else:
            last.next = current.next
        # if we are at the last node, delete by making second last, new last
        if current.next is None:
            self.tail = last

    def replace(self, item, newData):
        """Replace the data of a node instead of deleting it O(n)
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        current = self.head
        while (current != None): #run it till we get a match or hit the end.
            if current == item:
                item.data  = newData
                return
            current = current.next
        # if it didn't break out it means the item was not found in the linked list
        raise ValueError('Could not find {} in the given Doubly Linked List'.format(item))
        


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()