class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        pairs = [[p,s] for p, s in zip(position, speed)]
        pairs = sorted(pairs)[::-1]
        for p, s in pairs:
            stack.append((target - p) / s)
            while len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
                else:
                    break
    
        return len(stack)

        