class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l ,r = 0,len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum < target :
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l + 1,r + 1]

# Think of this as two friends trying to buy a specific souvenir that costs exactly a target amount of money.
# Because this is the "Two Sum II" problem, the numbers list is already sorted from smallest to largest. 
# Imagine all the available items are laid out on a long shelf, perfectly ordered from cheapest on the far left to most expensive on the far right.
# Here is how the analogy breaks down:

# Code Element	Analogy Concept
# l = 0	Friend Left stands at the very beginning of the shelf (the absolute cheapest item).
# r = len(numbers) - 1	Friend Right stands at the very end of the shelf (the absolute most expensive item).
# curSum	They pool their money together to see the total cost of the two items they are currently pointing at.


# Walking Through the Loop (while l < r)

# The two friends look at the total cost (curSum) of their current selection and compare it to their exact budget (target):
# • If the total is too low (curSum < target): 
# They need a more expensive pair. Since Friend Right is already at the max possible option for that pairing, the only logical move is for Friend Left to step one spot to the right (l += 1) to pick a slightly pricier item.
# • If the total is too high (curSum > target): 
# They need a cheaper pair. Since Friend Left is already at the lowest possible option for that pairing, Friend Right must step one spot to the left (r -= 1) to pick a slightly cheaper item.
# • If the total is exactly right: 
# They found the perfect combination! They look at their positions on the shelf, add 1 (because the gift shop labels shelves starting at 1 instead of 0), and walk up to the cashier.
# Because the shelf is perfectly sorted, they never have to randomly guess. They just smoothly step inward until their hands meet at the exact price tag they need.
