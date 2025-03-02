import sys
from vm import VirtualMachine

def load_bytecode(bytecode_file):
    with open(bytecode_file, 'r') as f:
        bytecode = [eval(line.strip()) for line in f]
    return bytecode

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <bytecode_file>")
        sys.exit(1)

    bytecode_file = sys.argv[1]
    bytecode = load_bytecode(bytecode_file)

    vm = VirtualMachine()
    result = vm.run(bytecode)
    print(f"process ended with code {result}")