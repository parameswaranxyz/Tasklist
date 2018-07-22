from Task.models import TaskEntry


class Node(object):

    def __init__(self, data=TaskEntry()):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


class Tree:
    def __init__(self):
        self.Root = Node(TaskEntry())

    def insert_child(self, root, new_node):
        # print("child rec", new_node.data)
        if new_node.data.Task_dependant_id is None:
            print("root",new_node.data)
            self.Root.children.append(new_node)
        elif root.data.Task_id == new_node.data.Task_dependant_id:
            # print("dep",new_node.data)
            root.children.append(new_node)
        elif len(root.children) > 0:
            for each_child in root.children:
                # print("child rec",new_node.data)
                self.insert_child(each_child, new_node)

    def print_tree(self, root):
        print(root.data.Task_id,root.data.Task_dependant_id,root.data.Task_des)
        if len(root.children) > 0:
            for each_child in root.children:
                self.print_tree(each_child)
