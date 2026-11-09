class Solution:
    def findMin(self, nums: List[int]) -> int:
       #return min(nums)
       l,r = 0 ,len(nums)-1
       res =nums[0]

       while l <= r:
          #An array :Not roatated
          if nums[l] < nums[r]:
            res = min(res,nums[l])
            break

          mid = l + ((r-l) // 2)
          res = min(res,nums[mid])

          if nums[mid] >= nums[l]:
            l = mid + 1 
            
          else :
            r = mid - 1
       return res


# The Analogy: 
#The Shifted DictionaryImagine an alphabet book that is supposed to be in neat, clean order: A, B, C, D, E, F.
# Now, imagine a mischievous prankster tears the book right down the middle, takes the back half (E, F), and tapes it onto the front of the book.
# If you open this pranked book, the pages now read:$$\mathbf{[E, F, A, B, C, D]}$$Your goal is to find the absolute start of the original book (A).


# Why res = nums[0] and NOT res = 0?
# This is a critical distinction!

# res = nums[0] stores the actual value of the first element in the array (e.g., if the array starts with 3, res holds 3).

# res = 0 would store the index number 0 (or the number zero itself).

# If you initialized res = 0, look at what happens inside the loop during this line:res = min(res, nums[m])

# If your array contains all positive numbers—for example, [3, 4, 5, 1, 2]—and the middle number is 4, Python evaluates min(0, 4). Because 0 is smaller than 4, your tracker would forever lock onto 0, and your function would return 0 at the end... even though 0 isn't even in the array!

# By setting res = nums[0], you are giving the code a realistic starting value from inside the array to act as your baseline for comparison.

# Step-by-Step Breakdown of the Code
# Let’s walk through the solution block by block to see how it uses Binary Search smartly.

# 1. Setup
# Python
# res = nums[0]
# l, r = 0, len(nums) - 1
# res = nums[0]: Sets our initial guess for the minimum to the very first item.

# l, r = 0, len(nums) - 1: Sets up two pointers—l (left) at the very beginning of the array, and r (right) at the very end.

# 2. The Main Loop & The Shortcut
# Python
# while l <= r:
#     if nums[l] < nums[r]:
#         res = min(res, nums[l])
#         break
# The Shortcut (if nums[l] < nums[r]): This is a brilliant optimization. In a binary search, if the section of the array you are currently looking at is already completely sorted (meaning the leftmost number is smaller than the rightmost number), you don't need to keep searching that chunk. The smallest number in that chunk is guaranteed to be right there at the left (nums[l]). You grab it, update res, and break out of the loop instantly!

# 3. Finding the Middle and Updating the Record
# Python
#     m = (l + r) // 2
#     res = min(res, nums[m])
# m = (l + r) // 2: Finds the middle index of your current search window.

# res = min(res, nums[m]): Checks if this middle number is smaller than our current record-holder (res), and updates res if it's a new minimum.

# 4. The Core Binary Search Decision (Which way do we go?)
# Python
#     if nums[m] >= nums[l]:
#         l = m + 1
#     else:
#         r = m - 1
# Because the array is rotated, one half of your current window will always be normally sorted, and the other half will contain the weird "drop-off" cliff.

# if nums[m] >= nums[l]: If the left side (from l to m) looks completely normal and sorted, that means the minimum element cannot be hiding in this left section (since numbers are just climbing upwards). So, you throw away the left side by moving your left pointer past the middle: l = m + 1.

# else: If the left side is broken/out of order, that means the "drop-off cliff" (and thus your minimum value) is hiding right there on the left side! So, you narrow your search window by moving your right pointer down: r = m - 1.

# 5. Returning the Winner
# Python
# return res
# Once the pointers cross (l > r), the search is complete, and res holds the absolute smallest value found on the mountain highway.

