class MinStack:
    def __init__(self):
        self._stack = []
        self._mins = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        try:
            self._mins.append(min(self._mins[-1], val))
        except IndexError:
            self._mins.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._mins.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._mins[-1]
        