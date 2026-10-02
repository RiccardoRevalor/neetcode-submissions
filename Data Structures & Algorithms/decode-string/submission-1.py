class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                #end of substring
                #loop back until you find a start of substring aka [
                substr = ""
                while stack and stack[-1] != '[':
                    #mantain order! you pop backwards!
                    substr = stack.pop() + substr

                #pop [, useless now
                stack.pop()

                #now we wanna have the number
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                #now do int(k)*substr
                stack.append(int(k) * substr)

        #final stack content is the final str
        return "".join(stack)

                


