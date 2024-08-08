
# node class
class Node:

    def __init__(self, cargo, next=None) -> None:

        self.cargo = cargo
        self.next = next

    def __str__(self):

        return str(self.cargo)



class LinkedList:

    def __init__(self, obj: list) -> None:
        
        # initializing linked list
        self.start_node = Node(obj.pop(0))

        current_node = self.start_node
        for value in obj:
            new_node = Node(value)
            current_node.next = new_node

            current_node = new_node

    # it will return container of the list if the object will used as an argument in the print function
    def __str__(self) -> str:

        return str(self.__container())

    def __getitem__(self, key) -> Node:

        node = None

        # checking for integer data type
        if isinstance(key, int):

            if key >= 0:
                node = self.__get_node(key)
            else:
                node = self.__get_node( len(self) + key )

        # checking for slice data type
        elif isinstance(key, slice):

            # getting slice values
            start, stop, step = key.indices(len(self))
            nodes = []

            # loop that getting needed nodes and adds them to the list 'nodes'
            for i in range(start, stop, step):
                nodes.append(self.__get_node(i).cargo)       

            return nodes

        else: 
            print(type(key))

        if node is not None:
            return node
        else:
            error_text = f"out of range. Key was: {key}, when maximum is from 0 to {len(self)-1} or from -1 to -{len(self)}"
            raise IndexError(error_text)

    def __setitem__(self, key, value) -> None:

        if key < len(self):
            self.change_value(value, key)
        else:
            self.put_value(value, key)

    def __delitem__(self, key) -> None:

        if key != 0:
            node_child = self[key].next
            parent_node = self[key-1]
            parent_node.next = node_child

        node = self[key]
        del node

    def __len__(self) -> int:

        node = self.start_node
        iters = 0
        while node:
            iters += 1
            node = node.next

        return iters


    def __get_node(self, index: int) -> Node:

        node = self.start_node
        iters = 0

        while node:

            if iters == index:
                return node
            node = node.next
            iters += 1


    def __container(self) -> list:

            node = self.start_node
            container: list = []

            while node is not None:

                container.append(node.cargo)

                node = node.next  

            return container


    # puts value at suggested position, if no position given it puts to the end of the list.
    def put_value(self, value, position: int = None) -> None:

        if position is None or position >= len(self):

            parent_node = self[-1]
            new_node = Node(value)

            parent_node.next = new_node

        elif position == 0:

            node_on_current_postion = self[position]
            new_node = Node(value, node_on_current_postion)

        else:
            
            node_on_current_postion = self[position]
            parent_node = self[position-1]

            new_node = Node(value, node_on_current_postion)
            parent_node.next = new_node


    def change_value(self, value, position: int) -> None:

        node = self[position]
        node.cargo = value
