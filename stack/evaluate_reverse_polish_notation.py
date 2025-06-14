'''
150. Evaluate Reverse Polish Notation. https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
'''


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        def _result(op2, op1, operand):
            if operand == '+':
                return op1 + op2
            elif operand == '-':
                return op1 - op2
            elif operand == '/':
                return int(op1/op2)
            elif operand == '*':
                return op1 * op2
    

        for c in tokens:
            if c in operators:
                res = _result(stack.pop(), stack.pop(), c)
                stack.append(res)
            else:
                stack.append(int(c))
        
        return stack[-1]
