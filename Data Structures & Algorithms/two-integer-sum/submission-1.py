class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We dont have to initialize the hashmap 
        #Can be empty then populated as we iterate through 
        #the array ....in one pass
        #We're guranteed that the first value is in hashmap 
        #iff we have iterated the array and found the 2nd
        #value(element) that sums up to the target
        hashmap = {} # Empty key:val pair 

        for index,num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff],index]

        # The function was returning None because
        #  the elements visited during the loop
        #   were never    stored in hashmap.
        #   As a result, diff in hashmap was always False.

        # Added hashmap[num] = index at the end
        # of each loop iteration to record 
        #  each number and its index.

            hashmap[num] = index
        return
        