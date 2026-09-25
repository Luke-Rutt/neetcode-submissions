class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []

        for o in operations:
            if o.lstrip('-').isdigit():
                score.append(int(o))
                
            elif o == "C":
                score.pop()
            
            elif o == "+":
                score.append(score[-1] + score[-2])
            
            elif o == "D":
                d = score[-1] * 2
                score.append(d)
            
        return sum(score)