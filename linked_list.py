from typing import Optional


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.last_node: Optional[Node] = None

    def __repr__(self):
        ll_string = ""
        node = self.head
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node
        ll_string += "None"
        print(ll_string)

    def to_list(self):
        arr = []
        node = self.head
        if node is None:
            return arr

        while node:
            arr.append(node.data)
            node = node.next_node
        return arr

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        # if self.last_node is None:
        #     node = self.head
        #     # while node.next_node:
        #     #     node = node.next_node
        #     node.next_node = Node(data, None)
        #     self.last_node = node.next_node
        #
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_data_by_id(self, id):
        node = self.head
        while node:
            if node.data["id"] == int(id):
                return node.data
            node = node.next_node
        return None