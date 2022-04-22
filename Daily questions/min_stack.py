class Stack():

    def __init__(self):
        self.element_stack = []
        self.min_element_stack = []

    def push(self, item):
        if not self.min_element_stack:
            self.element_stack.append(item)
            self.min_element_stack.append(item)
            return
        if item < self.min_element_stack[-1]:
            self.min_element_stack.append(item)
        else:
            self.min_element_stack.append(self.min_element_stack[-1])
        self.element_stack.append(item)

    def display(self):
        print(self.min_element_stack)
        print(self.element_stack)


if __name__ == "__main__":
    obj = Stack()
    obj.push(4)
    obj.push(3)
    obj.push(6)
    obj.push(9)
    obj.push(1)
    print(obj.display())


