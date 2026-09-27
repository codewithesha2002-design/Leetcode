class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                portion = []
                while stack and stack[-1] != '(':
                    portion.append(stack.pop())
                
                # Remove '('
                stack.pop()
                
                # Re-add reversed characters
                stack.extend(portion)
            else:
                stack.append(char)
                
        return "".join(stack)