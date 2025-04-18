# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/1610960569/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize counters for unmatched '(' and unmatched ')'
        c = 0  # Counter for unmatched '('
        p = 0  # Counter for unmatched ')'
        
        # Iterate through each character in the string
        for i in s:
            if i == "(":  # If the character is '(', increment the '(' counter
                c = c + 1
            elif c > 0 and i == ")":  # If there's an unmatched '(', match it with ')'
                c = c - 1
            else:  # If no unmatched '(' exists, increment the ')' counter
                p = p + 1
        
        # Return the total number of unmatched parentheses
        return p + c