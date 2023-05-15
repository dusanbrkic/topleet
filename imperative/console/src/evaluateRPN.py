class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # 3 5 * 4 +
        numbersStack = []
        for token in tokens:
            try:
                numbersStack.append(int(token))
            except ValueError:
                n2 = numbersStack.pop()
                n1 = numbersStack.pop()
                if token == "+":
                    numbersStack.append(n1 + n2)

                if token == "-":
                    numbersStack.append(n1 - n2)

                if token == "*":
                    numbersStack.append(n1 * n2)
                
                if token == "/":
                    numbersStack.append(int(n1 / n2))
        return numbersStack.pop()