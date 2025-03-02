import sys
from tokenizer import tokenize
from parser import Parser
from BytecodeGenerator import BytecodeGenerator

def compile_source(source_code):
    tokens = tokenize(source_code)
    parser = Parser(tokens)
    ast = parser.parse()
    generator = BytecodeGenerator()
    bytecode = generator.generate(ast)
    return bytecode

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compile.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    with open(source_file, 'r') as f:
        source_code = f.read()

    bytecode = compile_source(source_code)
    bytecode_file = source_file.replace('.worth', '.wby')
    with open(bytecode_file, 'w') as f:
        for instruction in bytecode:
            f.write(f"{instruction}\n")

    print(f"Compiled bytecode saved to {bytecode_file}")