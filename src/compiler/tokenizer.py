import re

TOKEN_SPEC = [
    ('NUMBER', r'\d+'),       # Integer numbers
    ('ID', r'[a-zA-Z_]\w*'),  # Identifiers
    ('ASSIGN', r'='),         # Assignment operator
    ('PLUS', r'\+'),          # Addition
    ('MINUS', r'-'),          # Subtraction
    ('MUL', r'\*'),           # Multiplication
    ('DIV', r'/'),            # Division
    ('LPAREN', r'\('),        # Left parenthesis
    ('RPAREN', r'\)'),        # Right parenthesis
    ('SKIP', r'[ \t]+'),      # Skip spaces and tabs
    ('NEWLINE', r'\n'),       # Newline
]

TOKEN_RE = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC))

def tokenize(code):
    tokens = []
    for match in TOKEN_RE.finditer(code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'SKIP':
            continue
        tokens.append((kind, value))
    return tokens