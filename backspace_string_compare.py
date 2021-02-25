"""
Time/Space Complexity = O(M+N)
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def chk(inp):   
            stack = []
            for i in inp:
                if i == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
        
        return chk(S) == chk(T)


"""
Time Complexity = O(M+N)
Space Complexity = O(1)
"""
from itertools import zip_longest

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def chk(inp):
            skip = 0
            for i in reversed(inp):
                if i == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield i
        
        return all(x == y for x, y in zip_longest(chk(S), chk(T)))