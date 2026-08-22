class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Keep any triplet that <= target value
        # Merge all of them
        # If it match = True
        # Otherwise = False

        stack = []
        at, bt, ct = target
        for ai, bi, ci in triplets:
            # Skip any triplet exceed target.
            if ai <= at and bi <= bt and ci <= ct:
                if not stack:
                    stack.append((ai, bi, ci))
                else:
                    # Merge it 
                    a1, b1, c1 = stack.pop()
                    a2, b2, c2 = max(a1, ai), max(b1, bi), max(c1, ci)
                    stack.append((a2, b2, c2))
        
        # Final Comparison
        if not stack:
            return False
            
        aS, bS, cS = stack.pop()
        if aS != at or bS != bt or cS != ct:
            return False
        return True
