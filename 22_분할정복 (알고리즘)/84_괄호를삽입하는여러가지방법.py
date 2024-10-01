# https://leetcode.com/problems/different-ways-to-add-parentheses/

# 0. 분할정복 
class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        if all(x not in expression for x in ['+','-','*']) :
            return [int(expression)]
        
        answer = []
        for i in range(len(expression)) :
            if expression[i] in ['+','-','*'] :
                for x in self.diffWaysToCompute(expression[:i]) :
                    for y in self.diffWaysToCompute(expression[i+1:]) :
                        if expression[i] == '+' :
                            answer.append(x+y)
                        elif expression[i] == '-' :
                            answer.append(x-y)
                        elif expression[i] == '*' :
                            answer.append(x*y)
        return answer
        
        