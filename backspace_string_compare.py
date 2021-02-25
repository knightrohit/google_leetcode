"""
Time/Space Complexity = O(N)
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