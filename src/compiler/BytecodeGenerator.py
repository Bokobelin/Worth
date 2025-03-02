from parser import Number, BinOp, Assign, Print, Variable, Subtract

class BytecodeGenerator:
    def __init__(self):
        self.instructions = []
    
    def generate(self, node):
        if isinstance(node, list):
            for stmt in node:
                self.generate(stmt)
        elif isinstance(node, Number):
            self.instructions.append(('PUSH', node.value))
        elif isinstance(node, BinOp):
            self.generate(node.left)
            self.generate(node.right)
            if node.op == 'PLUS':
                self.instructions.append(('ADD',))
            elif node.op == 'MINUS':
                self.instructions.append(('SUB',))
            elif node.op == 'MUL':
                self.instructions.append(('MUL',))
            elif node.op == 'DIV':
                self.instructions.append(('DIV',))
            else:
                raise ValueError(f"Unknown binary operator: {node.op}")
        elif isinstance(node, Assign):
            self.generate(node.value)
            self.instructions.append(('STORE', node.name))
        elif isinstance(node, Print):
            self.generate(node.value)
            self.instructions.append(('PRINT',))
        elif isinstance(node, Variable):
            self.instructions.append(('LOAD', node.name))
        elif isinstance(node, Subtract):
            self.instructions.append(('LOAD', node.left))
            self.instructions.append(('LOAD', node.right))
            self.instructions.append(('SUB',))
            self.instructions.append(('STORE', node.result))
        else:
            raise ValueError(f"Unknown node type: {type(node)}")
        return self.instructions