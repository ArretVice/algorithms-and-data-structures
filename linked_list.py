class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.extend(values)


    def append(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = self.head 
        else:
            self.tail.next_node = new
            self.tail = new

    def extend(self, values):
        for value in values:
            self.append(value)

    def find_by_value(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next_node
        else:
            print('Item is not in list')
            return False

    def find_index_by_value(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next_node
            index += 1
        else:
            print('Item is not in list')
            return False

    def show_list(self, verbose=True):
        if not self.find_loop(verbose = False):
            total = []
            current_node = self.head
            while current_node.next_node:
                total.append(current_node.value)
                current_node = current_node.next_node
            else:
                total.append(current_node.value)
                if verbose: print(total)
            return total
        else:
            return False

    def insert_at_head(self, value):
        new = Node(value)
        new.next_node = self.head
        self.head = new
        return True

    # def delete_by_value(self, value):
    #     previous_node = None
    #     current_node = self.head
    #     while current_node:
    #         if current_node.value == value:
    #             if current_node == self.head:
    #                 self.head = current_node.next_node
    #             else:
    #                 next_node = current_node.next_node
    #                 previous_node.next_node = next_node
    #             print(f'Deleted {current_node}')
    #             del current_node
    #             return True
    #         else:
    #             previous_node = current_node
    #             current_node = current_node.next_node
    #     else:
    #         print('Item not in list')
    #         return False

    def delete_by_value(self, value):
        index = self.find_index_by_value(value)
        return self.delete_by_index(index)


    def delete_by_index(self, n):
        item = self.find_by_index(n)
        if item:
            if item == self.head:
                self.head = item.next_node
            else:
                previous_node = self.find_by_index(n - 1)
                next_node = item.next_node
                previous_node.next_node = next_node
                if next_node == None:
                    self.tail = previous_node
            print(f'Item {item} deleted at index {n}')
            del item
            return True
        else:
            return False

    def reverse(self, verbose=True):
        current_node = self.head
        previous_node = None
        next_node = None
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        else:
            self.head = previous_node
        if verbose: print('List reversed')
        return True

    def find_by_index(self, n):
        if isinstance(n, int):
            current_index = 0
            current_node = self.head
            while current_node:
                if current_index == n:
                    return current_node
                else:
                    current_index += 1
                    current_node = current_node.next_node
            else:
                print('Index out of range')
                return False
        else:
            print('Index must be integer')
            return False

    def find_loop(self, verbose=True):
        slow_pointer = self.head
        fast_pointer = self.head
        while slow_pointer:
            slow_pointer = slow_pointer.next_node
            try:
                fast_pointer = fast_pointer.next_node.next_node
            except AttributeError:
                if verbose: print('There is no loop')
                return False
            if fast_pointer == slow_pointer:
                if verbose: print('There is a loop')
                return True
        else:
            if verbose: print('There is no loop')
            return False

    def delete_duplicates(self):
        items = []
        current_node = self.head
        current_index = 0
        previous_node = None
        there_were_duplicates = False
        while current_node:
            next_node = current_node.next_node
            if current_node.value in items:
                self.delete_by_index(current_index)
                current_node = next_node
            else:
                items.append(current_node.value)
                previous_node = current_node
                current_node = next_node
                current_index += 1
        if there_were_duplicates:
            print('Duplicates were deleted')
        else:
            print('There were no duplicates')
        return True

    def __str__(self):
        return str(self.head.value)


if __name__ == '__main__':
    # setting up list items
    ll = LinkedList()
    ll.append(7)
    ll.append(3)
    ll.append(5)
    ll.append(0)
    ll.extend([1, 5, 0, 5])
    ll.extend('andef')

    # testing functionality
    print(f'Initial list: {ll.show_list(verbose=False)}')
    ll.find_loop()
    ll.reverse(verbose=False)
    print(f'Reversed list: {ll.show_list(verbose=False)}')
    ll.reverse(verbose=False)
    print('\n')

    # list with loop
    ll_with_loop = LinkedList()
    ll_with_loop.extend('abcdefgh')
    print(f'List with loop: {ll_with_loop.show_list(verbose=False)}')
    ll_with_loop.tail.next_node = ll_with_loop.find_by_value('d') # adding loop from tail to "d"
    ll_with_loop.find_loop()
    print('\n')
    
    # return N-th element from start
    n = 3
    print(f'{n}-th item is {ll.find_by_index(n)}')
    n = 9
    print(f'{n}-th item is {ll.find_by_index(n)}')
    print('\n')

    # delete duplicates
    ll_with_duplicates=LinkedList('abcdefddsfaa')
    print(f'List with duplicates: {ll_with_duplicates.show_list(verbose=False)}')
    ll_with_duplicates.delete_duplicates()
    print(f'List with duplicates: {ll_with_duplicates.show_list(verbose=False)}')
    print('\n')


    ll_without_duplicates=LinkedList('abcde')
    print(f'List without duplicates: {ll_without_duplicates.show_list(verbose=False)}')
    ll_without_duplicates.delete_duplicates()
    print(f'List without duplicates: {ll_without_duplicates.show_list(verbose=False)}')
    