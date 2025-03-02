class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.variables = {}

    def run(self, instructions):
        for instr in instructions:
            if instr[0] == 'PUSH':
                self.stack.append(instr[1])
            elif instr[0] == 'ADD':
                if len(self.stack) < 2:
                    raise RuntimeError("Not enough values on the stack for ADD operation")
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a + b)
            elif instr[0] == 'SUB':
                if len(self.stack) < 2:
                    raise RuntimeError("Not enough values on the stack for SUB operation")
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a - b)
            elif instr[0] == 'MUL':
                if len(self.stack) < 2:
                    raise RuntimeError("Not enough values on the stack for MUL operation")
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a * b)
            elif instr[0] == 'DIV':
                if len(self.stack) < 2:
                    raise RuntimeError("Not enough values on the stack for DIV operation")
                b, a = self.stack.pop(), self.stack.pop()
                if b == 0:
                    raise RuntimeError("Division by zero")
                self.stack.append(a / b)
            elif instr[0] == 'STORE':
                if not self.stack:
                    raise RuntimeError("No value on the stack to store")
                self.variables[instr[1]] = self.stack.pop()
            elif instr[0] == 'LOAD':
                if instr[1] not in self.variables:
                    raise RuntimeError(f"Undefined variable: {instr[1]}")
                self.stack.append(self.variables[instr[1]])
            elif instr[0] == 'PRINT':
                if not self.stack:
                    raise RuntimeError("No value on the stack to print")
                value = self.stack.pop()
                print(value)
            else:
                raise RuntimeError(f"Unknown instruction: {instr[0]}")
        return 0