class MaxStack:
    global max, test 

    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):
        self.stack.append(val)
        if(self.maxes and self.maxes[-1] > val):
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)

    def pop(self):
        if(self.maxes):
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        if(self.maxes):
            return self.maxes[-1]
    
    def test(self):
        print('showing each max per pop')
        while(self.stack):
            print('max ', max(self))
            print(self.pop())


stack = MaxStack()

#change here
stack.push(1)
stack.push(2)
stack.push(5)
stack.push(8)
stack.push(9)
stack.push(7)

test(stack)
