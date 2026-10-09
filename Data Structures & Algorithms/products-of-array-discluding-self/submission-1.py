class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *=nums[i] 
        
        postfix = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix #Avoids removing whats already    inside 
            postfix *= nums[i]
        return res

    #prefix of each Nunber:[1,1,2,6]
    #Prefix of each number :[24,12,4,1]

    #Initialize and populate the array with original val 1
    #pass from left to right 
    #Do the same but in reverse direction