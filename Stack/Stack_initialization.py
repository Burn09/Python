class Element(object):
    """Initializing an Element for a Linked List"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """Initializing a Linked List object"""

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """Appending new elements to the Linked List"""

        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        """Insert a new element as the head of the list"""

        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the element at the head of the list
        and return it"""

        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None


class Stack(object):
    """Initializing a stack object using a Linked List"""

    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """Pushing an element to the top of the Stack"""

        self.ll.insert_first(new_element)

    def pop(self):
        """Deleting an element at the top of the Stack
        and returning it"""

        return self.ll.delete_first()
