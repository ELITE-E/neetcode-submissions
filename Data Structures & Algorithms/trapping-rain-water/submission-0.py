class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 ,len(height) - 1
        leftMax,rightMax = height[l] ,height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax ,height[l])
             
                res +=leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r]
        return res

# Think of this correct solution as two separate rescue teams building a levee from opposite sides of a flooded valley.
# The terrain is made up of solid stone pillars. Rain has fallen, and puddles have formed in the dips. To find the total water trapped, we must measure the depth of the puddle on top of every single pillar, one by one.
# Here is the setup for our rescue teams:
# • Team Left (l) starts at the far-left pillar, and Team Right (r) starts at the far-right pillar.
# • leftMax is the height of the tallest stone wall Team Left has built or encountered so far on their side.
# • rightMax is the height of the tallest stone wall Team Right has built or encountered so far on their side.

# Step 1: The Initial Check (if leftMax < rightMax)

# Why do we have to start with this check? What is its use?
# Water is lazy—it always leaks out of the lowest possible exit. For any individual pillar in the middle of the valley, the amount of water it can hold depends on the shorter of its two surrounding walls (the left horizon vs. the right horizon).
# By comparing leftMax and rightMax, the code is asking: "Which side of our valley currently has the lower backup wall?"
# • If leftMax < rightMax, we know with 100% mathematical certainty that the left wall is the bottleneck for the immediate left side. Even if there are massive unvisited mountains hidden in the middle of the map, Team Right has already found a wall (rightMax) that is taller than leftMax. Water on the left cannot spill out to the right; it will spill over leftMax first.
# • Therefore, it is completely safe for Team Left to take a step inward and calculate water, because their local leftMax is the absolute ruling limit.

# Step 2: Moving Inward and Updating the Wall (l += 1 and max())

# Because the left wall was determined to be the bottleneck, Team Left steps one pillar to the right (l += 1).
# The very first thing they do at this new pillar is check its height:
# python
# leftMax = max(leftMax, height[l])
# Use code with caution.
# • Analogy: Team Left looks at the stone pillar they are standing on. If this new pillar is taller than their previous leftMax, they update their records. This new pillar is now their highest wall.

# Step 3: Measuring the Puddle Depth (res += leftMax - height[l])

# Now that the wall height is updated, they look down at their feet to measure the water:
# python
# res += leftMax - height[l]
# Use code with caution.
# • Analogy: If the stone pillar they are standing on (height[l]) is shorter than the leftMax wall right behind them, it means they are standing in a dip!
# • Because leftMax is the bottleneck, water will fill up exactly to the height of leftMax. The depth of the water right above this specific pillar is the distance from the top of the wall down to the stone (leftMax - height[l]). They add this exact amount to the total scoreboard (res +=).
# • (Note: If they just discovered a new highest pillar, leftMax equals height[l], so the math automatically results in 0 water trapped on top of a mountain peak).

# Step 4: Repeating the Process (The else block)

# What if the initial check found that rightMax was smaller or equal to leftMax?
# The exact same logic applies, but in reverse!
# • Team Right knows that the right side is the bottleneck.
# • Team Right steps one pillar to the left (r -= 1).
# • They update their rightMax.
# • They look down at their feet and calculate the puddle depth on that column (rightMax - height[r]), adding it to the total.

# Closing the Loop

# The two teams keep comparing their walls (while l < r) and moving the bottleneck side inward. They smoothly walk across the landscape, measuring the exact puddle depth on every single pillar without ever double-counting or letting water "leak" past their logic. When the two teams finally meet in the middle, every puddle in the valley has been perfectly itemized and summed up.

