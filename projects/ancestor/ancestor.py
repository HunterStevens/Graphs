class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    result = -1
    stck = Stack()
    stck.push(starting_node)

    while stck.size() > 0:
        ancestor_path = stck.pop()
        oldest_ancester = ancestor_path
        for i in ancestors:
            if i[1] == oldest_ancester:
                stck.push(i[0])
                result = i[0]
                break
    print(result)
    return result


