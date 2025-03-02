class iota:
    """
    A class that generates a sequence of integers starting from 1.
    """
    def __init__(self) -> None:
        self.value: int = -1

    def __call__(self) -> int:
        self.value += 1
        return self.value