class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0 ,len(heights) -1
        res = 0

        while l < r:
            area = (r - l) * min(heights[l] , heights[r])
            res = max(res ,area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
        return res


# Think of this code as two walls of a modular water tank moving inward to find the layout that can trap the maximum amount of water.

# You are given a lineup of vertical pillars of different heights. You place two long, movable barrier gates at the very outer edges of the line and try to create the biggest possible reservoir container between them.
# Here is the setup:

# Code Element	Analogy Concept
# l = 0	Left Gate: Starts at the very beginning of the lineup.

# r = len(heights) - 1	Right Gate: Starts at the very end of the lineup.

# res	A scoreboard tracking the largest volume of water captured so far.

# (r - l)	The width of the tank (the distance between the two gates).

# min(heights[l], heights[r])	The maximum water level. Water spills over the lower gate, so the shorter gate dictates the maximum fill height.


# The Strategy: How the Gates Move

# The gates start at maximum width. As they move closer together (while l < r), the width (r - l) will inevitably shrink. To get a bigger volume, the gates must find much taller pillars to make up for the loss of width.
# Every step of the way, the code calculates the current water volume (area) and updates the scoreboard if it breaks a record (res = max(res, area)).
# Then, the director looks at both gates to decide which one to move:
# • If the Left Gate is shorter (heights[l] < heights[r]): The Left Gate is the bottleneck limiting the water level. Keeping it there is useless because moving the taller Right Gate inward will only decrease width without helping height. Therefore, they abandon the short Left Gate and move it one step right (l += 1) in hopes of finding a taller pillar.
# • If the Right Gate is shorter (heights[l] > heights[r]): The Right Gate is the bottleneck. They abandon the short Right Gate and move it one step left (r -= 1) to search for a taller option.
# • If both gates are equal (else): Both are bottlenecks. Moving either one is fine, so the code arbitrarily chooses to move the Right Gate one step left (r -= 1).
# By always abandoning the shorter pillar, the algorithm guarantees it never misses a potentially larger container, squeezing out the maximum area in just one pass.