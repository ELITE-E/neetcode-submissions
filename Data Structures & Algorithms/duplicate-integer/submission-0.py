class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()

        for num in nums :
            
            if num in hashtable:
                return True

            hashtable.add(num)
        return False
        
        

