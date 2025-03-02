class Node:
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assign(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Print(Node):
    def __init__(self, value):
        self.value = value

class Variable(Node):
    def __init__(self, name):
        self.name = name

class Subtract(Node):
    def __init__(self, left, right, result):
        self.left = left
        self.right = right
        self.result = result

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self):
        self.pos += 1
        return self.tokens[self.pos - 1]

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def parse_expression(self):
        left = self.parse_term()
        while self.peek()[0] in ('PLUS', 'MINUS'):
            op = self.consume()[0]
            right = self.parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.peek()[0] in ('MUL', 'DIV'):
            op = self.consume()[0]
            right = self.parse_factor()
            left = BinOp(left, op, right)
        return left

    def parse_factor(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Unexpected end of input")
        token, value = self.consume()
        if token == 'NUMBER':
            return Number(value)
        elif token == 'LPAREN':
            expr = self.parse_expression()
            if self.peek()[0] != 'RPAREN':
                raise SyntaxError("Expected ')'")
            self.consume()  # Expect RPAREN
            return expr
        elif token == 'ID':
            return Variable(value)  # Return a Variable node
        raise SyntaxError(f"Unexpected token: {token}")

    def parse_statement(self):
        while self.peek()[0] == 'NEWLINE':
            self.consume()  # Skip newlines
        token, value = self.peek()
        if token == 'ID':
            self.consume()
            if self.peek()[0] == 'ASSIGN':
                self.consume()
                expr = self.parse_expression()
                return Assign(value, expr)
            elif value == 'print':
                expr = self.parse_expression()
                return Print(expr)
            elif value == 'sub':
                left = self.consume()[1]
                right = self.consume()[1]
                result = self.consume()[1]
                return Subtract(left, right, result)
        raise SyntaxError(f"Unexpected token: {token}")

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.parse_statement())
            while self.peek()[0] == 'NEWLINE':
                self.consume()  # Skip newlines between statements
        return statements