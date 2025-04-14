class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        # Helper function to
        # Helper function to check if Koko can eat all bananas at speed `k` within `h` hours
        def check(k):
            c = 0
            for i in piles:
                # Calculate the hours needed to eat the current pile at speed `k`
                c = c + math.ceil(i / k)
            
            # If total hours `c` is less than or equal to `h`, return "YES", otherwise "NO"
            if c <= h:
                return "YES"
            else:
                return "NO"
        
        # Binary search to find the minimum eating speed
        small = 1  # Minimum possible speed
        big = max(piles)  # Maximum possible speed (eating the largest pile in 1 hour)
        ans = 0  # Variable to store the result
        
        while small <= big:
            mid = (small + big) // 2  # Calculate the middle speed
            x = check(mid)  # Check if this speed is feasible
            
            if x == "YES":
                ans = mid  # Update the answer to the current speed
                big = mid - 1  # Try to find a smaller feasible speed
            else:
                small = mid + 1  # Increase the speed to make it feasible
        
        return ans  # Return the minimum eating speed
