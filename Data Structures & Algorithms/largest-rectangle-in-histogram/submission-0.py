class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index,height)

        for idx ,hgt in enumerate(heights):
            start = idx
            while stack and stack[-1][1 ] > hgt:
                index ,height = stack.pop()
                maxArea = max(maxArea ,height * (idx -index))
                start = index

            stack.append((start,hgt)) 
        
        for idx ,hgt in stack :
            maxArea = max(maxArea, hgt * (len(heights) - idx))
        return maxArea



# ### The Big Idea: The Core Secret

# To find the largest rectangle, the code uses a clever trick: **Every time you encounter a bar, you ask: *"If this bar acts as the bottleneck (the shortest height), how wide can my rectangle stretch?"***

# Instead of checking every single combination, the code walks through the bars from left to right. It uses a **stack** to hold onto bars that are waiting to find out how far they can stretch to the right.

# ---

# ### The Analogy: The Retaining Wall Construction Crew

# Imagine you are managing a construction crew building a flat retaining wall block by block, moving from **left to right**.

# Each block has a specific height. You want to find the largest rectangular section of wall you can build.

# You keep a **waiting line (the stack)** of blocks that haven't finished growing yet.

# #### 1. When a Taller Block Arrives (`stack.append`)

# * **What happens:** You pick up a new block, and it is **taller** than or equal to the previous block.
# * **In the analogy:** Great news! This block can keep stretching to the right. You throw it onto your waiting line (`stack.append`) and keep moving forward. It’s hoping it can stretch even wider.

# #### 2. When a Shorter Block Arrives (`while stack and stack[-1][1] > h:`)

# * **What happens:** Suddenly, you pick up a block that is **shorter** than the blocks waiting in your line.
# * **In the analogy:** This short block causes a **crisis** for the taller blocks sitting behind it!
# * Because this new block is shorter, those tall blocks **cannot stretch any further to the right**. Their journey stops right here, because this new short block would block their height if they tried to cross it.
# * So, the tall blocks are forced to "retire" right then and there.
# * One by one, you pop those tall blocks off the line. Each one calculates its final area:

# $$\text{Area} = \text{Height} \times \text{How far back it started up to the current position}$$


# * You check if this area is the new record (`maxArea`).
# * **The Munchies Effect (`start = index`):** Because the new short block is short, it can actually stretch all the way back to where those tall blocks *used* to start! It inherits their old starting positions because it is short enough to fit anywhere they were.



# #### 3. The Leftovers at the End (`for i, h in stack:`)

# * **What happens:** You reach the end of the entire row of bars, but some blocks are still sitting in your waiting line because they never hit a shorter block to stop them.
# * **In the analogy:** If a block made it all the way to the end of the row without ever being blocked, it means **it could stretch all the way to the very end of the wall!**
# * The code does a quick final loop over whatever is left in the stack, calculating their final areas using the total length of the chart (`len(heights)`).

# ---

# ### Summary of Why It's Brilliant

# Instead of looking forward from every single bar (which takes forever), the stack looks **backward** whenever a shorter bar cuts things short. Every bar is added to the stack once and removed once, turning a messy, slow problem into a lightning-fast **$O(N)$** sweep!