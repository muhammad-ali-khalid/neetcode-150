class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        d = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        for t in tokens:
            if t in d:
                b = s.pop()
                a = s.pop()
                s.append(d[t](a, b))
            else:
                s.append(int(t))
        return s.pop()