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
        if new_node.data.Task_dependant_id is None:
            self.Root.children.append(new_node)
        elif root.data.Task_id == new_node.data.Task_dependant_id:
            root.children.append(new_node)
        elif len(root.children) > 0:
            for each_child in root.children:
                self.insert_child(each_child, new_node)

    def print_tree(self, root):
        dic = {}
        dic["Task_id"] = str(root.data.Task_id)
        dic["Task_des"] = str(root.data.Task_des)
        dic["Task_priority"] = str(root.data.Task_priority)
        dic["Task_weight"] = str(root.data.Task_weight)
        dic["Task_dependant"] = str(root.data.Task_dependant)
        dic["Task_dependant_id"] = str(root.data.Task_dependant_id)
        dic["Task_create"] = str(root.data.Task_create)
        dic["children"] = []
        if len(root.children) > 0:
            for each_child in root.children:
                print(each_child)
                dic.get("children").append(self.print_tree(each_child))

            for i in root.children:
                dic["Task_weight"] = int(dic.get("Task_weight")) + int(i.data.Task_weight)

        # print(dic)
        return dic
