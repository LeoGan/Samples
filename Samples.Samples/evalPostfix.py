import Stack

class evalPostfix:
    """description of class"""

    def eval(self, expr):
        import re
        tokenList = re.split(" ", expr)
        s = Stack.Stack()

        for token in tokenList:
            if token == '' or token == ' ':
                continue
            elif token == '+':
                sum = s.pop() + s.pop()
                s.push(sum)
            elif token == '*':
                mul = s.pop() * s.pop()
                s.push(mul)
            else:
                s.push(int(token))

        return s.pop()



