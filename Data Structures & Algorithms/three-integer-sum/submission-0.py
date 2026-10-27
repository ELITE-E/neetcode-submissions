class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
# Think of this solution as a team of three balance-beam inspectors trying to find groups of three weights that perfectly balance a scale to zero.

# The weights are laid out on a long table, sorted perfectly from heaviest negative weights (left) to heaviest positive weights (right).

# Here is the setup:

# Code Element	Analogy Concept
# for i, a in enumerate(nums)	Inspector 1 (The Anchor): They walk down the table from left to right, picking a baseline weight a.

# l = i + 1	Inspector 2 (Left Hand): They stand right next to Inspector 1 and look toward the right.

# r = len(nums) - 1	Inspector 3 (Right Hand): They stand at the absolute far-right end of the table (the heaviest positive weight).


# The Strategy: How They Work Together


# 1. The Early Lunch Rule (if a > 0: break)

# Because the table is sorted, if Inspector 1 moves so far right that they pick up a weight greater than zero, they stop completely and go home. Why? Because all remaining weights to their right are also positive. You can't add three positive numbers together and get zero!

# 2. The "No Dejavu" Rule (if i > 0 and a == nums[i - 1]: continue)

# If Inspector 1 picks up a weight and realizes it is the exact same value as the one they just tested, they immediately drop it and skip to the next one. They already found all possible zero-combinations for that weight size.

# 3. Shifting Inward (while l < r)

# With Inspector 1 holding the baseline weight a, Inspector 2 (l) and Inspector 3 (r) look at the total sum of their three weights (threeSum):
# • Too Heavy (threeSum > 0): The total is too positive. To lower the sum, Inspector 3 steps one spot to the left (r -= 1) to grab a lighter positive weight.
# • Too Light (threeSum < 0): The total is too negative. To increase the sum, Inspector 2 steps one spot to the right (l += 1) to grab a lighter negative (or heavier positive) weight.
# • Perfect Balance (else): They found a match! They log it (res.append).

# 4. Clearing the Twins (while nums[l] == nums[l - 1] ...)

# After finding a match, Inspector 2 and 3 both take a step inward (l += 1, r -= 1) to look for new combinations. However, if Inspector 2 looks down at their new position and sees the exact same weight value they just used, they keep stepping right (l += 1) until they find a brand-new number. This efficiently blocks duplicate triples without needing a slow lookup table.