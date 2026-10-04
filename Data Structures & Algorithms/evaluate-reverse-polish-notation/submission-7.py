class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []

        for tok in tokens:
            if tok.replace("-", "").isdigit():
                self.stack.append(int(tok))
            else:
                #operand reached
                #pop last two from stack
                op1 = self.stack.pop()
                op0 = self.stack.pop()
                if tok == "+":
                    self.stack.append(op0+op1)
                elif tok == "*":
                    self.stack.append(op0*op1)
                elif tok == "-":
                    self.stack.append(op0-op1)
                else:
                    self.stack.append(int(op0 / op1))
        
        return self.stack.pop()

        