class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # for idx,num in enumerate(nums):
        #   return nums[target]
        # return -1

        l , r = 0,len(nums)-1

        while l < r :
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        l,r = 0 ,len(nums)-1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] ==  target:
                return m
            elif nums[m] < target :
                l = m + 1
            else:
                r = m - 1

        return -1 



# The Big Picture: The Two-Step Mission
# Imagine you are looking for a specific house (your target) in a neighborhood built on a circular mountain that got cut and laid out flat. Because of the cut, the street numbers are broken and shifted (rotated).

# If you just start searching blindly, you'll get lost. So you divide your mission into two distinct chapters:

# Mission 1: Find the Cliff (The Pivot). Locate the exact spot where the street wraps around and drops from the highest number back down to the lowest number.

# Mission 2: Pick Your Neighborhood and Search. Use that cliff as a permanent dividing line to split the street into two normal, orderly sections, pick the section where your target lives, and hunt it down.

# Mission 1: Finding the Cliff (The Pivot)
# Python
# l, r = 0, len(nums) - 1

# while l < r:
#     mid = (l + r) // 2

#     if nums[mid] > nums[r]:
#         l = mid + 1
#     else:
#         r = mid

# pivot = l
# What we are doing: We set two pointers at opposite ends of the entire street (l at the start, r at the end) and look at the middle house (mid).

# The Clue (if nums[mid] > nums[r]): We compare the middle house's number to the house at the very end (r).

# If the middle house has a larger number than the end house, it means the street is still climbing, but a cliff (the drop-off) must be hiding further to the right. So we move our left boundary up (l = mid + 1).

# If not, the drop-off is to our left (or right where we are), so we pull our right boundary down (r = mid).

# The Result (pivot = l): We keep shrinking our window until l and r crash into the exact same house. That house is the absolute lowest point on the street—the cliff edge (the pivot).

# Mission 2: Resetting the Map and Choosing a Side
# Now we hit the part that felt tricky earlier. We found our cliff, but before we search for our target, we need to reset our boundaries and pick a side:

# Python
# l, r = 0, len(nums) - 1

# if target >= nums[pivot] and target <= nums[r]:
#     l = pivot
# else:
#     r = pivot - 1
# 1. Why reset l, r = 0, len(nums) - 1?
# In Mission 1, our pointers (l and r) shrunk all the way down until they were tightly hugging just the pivot. But now, we want to look at the entire street again as our full map so we can make a clean choice between the left half and the right half of the cliff.

# 2. The Security Guard (if/else)
# The cliff naturally cuts the street into two completely normal, perfectly sorted halves:

# The Right Half: Runs from pivot to the end of the array (r).

# The Left Half: Runs from the very beginning (0) up to pivot - 1.

# The if/else block looks at the right half of the cliff and asks: "Does our target number fit within the value range of this right side?"

# If YES (l = pivot): The target lives on the right side! We adjust our pointers to lock only onto the right half.

# If NO (r = pivot - 1): The target isn't there, which means it must live on the left side. We adjust our pointers to lock only onto the left half.

# Mission 3: The Final Hunt
# Python
# while l <= r:
#     m = (l + r) // 2
#     if nums[m] == target:
#         return m
#     elif nums[m] < target:
#         l = m + 1
#     else:
#         r = m - 1

# return -1
# What we are doing: Now that our pointers (l and r) have been narrowed down to guard only the correct half (either the left section or the right section), the trickiest part is over.

# This is just a standard, classic binary search. Because the section we locked onto is 100% normally sorted (no cliffs here!), we can safely search it using regular "higher or lower" logic.

# If we find the target, we return its index (m). If we search the whole section and find nothing, we return -1.

