class CodeElement:
    indent_size = 2

    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    def __str(self, indent_count=0):
        lines = []
        indent = " " * (indent_count * self.indent_size)
        lines.append(indent + "class " + self.root_name)

        next_indent = " " * ((indent_count + 1) * self.indent_size)
        # lines.append(f"{next_indent}def __init__(self):")
        lines.append(next_indent + "def __init__(self):")

        next_indent = " " * ((indent_count + 2) * self.indent_size)
        for name, default_value in self.fields:
            # lines.append(f"{next_indent}{name} = {default_value}")
            lines.append(next_indent + name + " = " + default_value)
        return "\n".join(lines)

    def __str__(self):
        return str(self.__str(0))


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = CodeElement(root_name)

    def add_field(self, type, name):
        self.__root.fields.append((type, name))
        return self

    def __str__(self):
        return str(self.__root)


cb = CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
print(cb)
