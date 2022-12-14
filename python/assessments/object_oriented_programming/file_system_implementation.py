class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        # Write your code here.
        self._validate_path(path)
        node_names = self.path_to_node_names(path)
        new_dir_name = node_names.pop()
        new_dir = Directory(new_dir_name)

        last_dir = self._find_bottom_node(node_names)
        if last_dir:
            if type(last_dir) == Directory:
                last_dir.add_node(new_dir)
            else:
                raise ValueError()
        else:
            raise ValueError()

    def create_file(self, path, contents):
        # Write your code here.
        self._validate_path(path)
        node_names = self.path_to_node_names(path)
        file_name = node_names.pop()
        last_dir = self._find_bottom_node(node_names)

        if last_dir:
            new_file = File(file_name)
            new_file.write_contents(contents)

            last_dir.add_node(new_file)
        else:
            raise ValueError("Path invalid")

    def read_file(self, path):
        # Write your code here.
        self._validate_path(path)
        node_names = self.path_to_node_names(path)
        file = self._find_bottom_node(node_names)

        if type(file) == File:
            return file.contents
        else:
            raise ValueError(f"File not found.")

    def delete_directory_or_file(self, path):
        # Write your code here.
        self._validate_path(path)
        node_names = self.path_to_node_names(path)
        to_del_name = node_names.pop()
        last_dir = self._find_bottom_node(node_names)

        if last_dir:
            if to_del_name in last_dir.children:
                last_dir.delete_node(to_del_name)
            else:
                raise ValueError()
        else:
            raise ValueError()

    def size(self):
        # Write your code here.
        def size_helper(dir):
            next_dirs = []
            for node_name in dir.children:
                node = dir.children[node_name]
                if type(node) == File:
                    sizes.append(len(node))
                else:
                    next_dirs.append(node)
            for next_dir in next_dirs:
                size_helper(next_dir)

        sizes = []

        size_helper(self.root)

        return sum(sizes)

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"

    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    @staticmethod
    def path_to_node_names(path):
        path = path[1:]
        node_names = path.split("/")

        return node_names

    def _find_bottom_node(self, node_names):
        # Write your code here.
        # ex: node_names = ["a", "b", "c"]
        current_dir = self.root
        while len(node_names) > 0:
            next_node = node_names.pop(0)
            if next_node in current_dir.children:
                current_dir = current_dir.children[next_node]
            else:
                return False
        
        return current_dir


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)


    # def create_directory(self, path):
    # # Write your code here.
    # self._validate_path(path)
    # node_names = self.path_to_node_names(path)
    # new_dir_name = node_names.pop()
    #  new_dir = Directory(new_dir_name)

    #   current_dir = self.root
    #    while len(node_names) > 0:
    #         node_name = node_names.pop(0)
    #         if node_name in current_dir.children:
    #             current_dir = current_dir.children[node_name]
    #             if type(current_dir) != Directory:
    #                 raise ValueError()
    #         else:
    #             child_dir = Directory(node_name)
    #             current_dir.add_node(child_dir)
    #             current_dir = current_dir.children[node_name]

    #     current_dir.add_node(new_dir)
