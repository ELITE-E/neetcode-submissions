class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for num,cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for idx in range(len(freq)-1,0,-1):
            for num in freq[idx]:
                res.append(num)
            
            if len(res) == k:
                return res
#01.Count the votes 

# • The Analogy: You sit at a desk with a blank sheet of paper (count = {}). You pull votes out of the bucket one by one. You look up the number on your sheet. If it’s not there, you write it down with 0 votes and add 1. If it is already there, you just add 1 to its current score.
# • Result: Your sheet now reads: 1: 3 votes, 2: 2 votes, 3: 1 vote.

# 1. "Look up a number" (count.get(num, ...))
# You look at your tally sheet to see if the number 5 already has a row dedicated to it.
# 2. "If it's not there, write it down with 0 votes" (..., 0)
# The .get(num, 0) method is a safety feature. It says: "Look for 5. If you don't find it, don't crash with an error—just pretend the current count is 0."
# So, because this is the first time you are seeing 5, your brain temporarily registers its current score as 0.
# 3. "And add 1" (1 + ...)
# Now you perform the addition: 1 + 0 = 1.
# Finally, the code takes that result (1) and writes it permanently onto your sheet:

#02.Set up scoreboards 

# • The Analogy: You look at the total number of votes cast (6 votes). You line up 7 physical buckets on the floor, numbered 0 to 6.
# • The Meaning of the Buckets: The bucket number represents how many votes a candidate got. Bucket 3 is for candidates who got exactly 3 votes. Bucket 0 is for candidates who got zero votes.

#03.Sort candidates into their buckets

# • The Analogy: You take your tally sheet and look at each candidate:
# 	• Candidate 1 got 3 votes. You walk over to Bucket 3 and drop a card with the number 1 into it.
# 	• Candidate 2 got 2 votes. You walk over to Bucket 2 and drop a card with the number 2 into it.
# 	• Candidate 3 got 1 vote. You drop a card with the number 3 into Bucket 1.
# Now, your floor looks like this:
# • Bucket 6: [] (Empty)
# • Bucket 5: []
# • Bucket 4: []
# • Bucket 3: [1]
# • Bucket 2: [2]
# • Bucket 1: [3]
# • Bucket 0: []

#04. Collect winners

# • The Analogy: You want to hand out prizes to the top \(k\) (\(2\)) winners. Naturally, you start looking from the highest-numbered bucket (Bucket 6) and walk backwards toward Bucket 0.
# 	• Buckets 6, 5, and 4 are empty. You keep walking.
# 	• You reach Bucket 3. Inside, you find candidate 1. You grab them and put them in your prize basket (res = [1]).
# 	• You check your basket size. It only has 1 person, but you need \(k=2\). Keep looking.
# 	• You step back to Bucket 2. Inside, you find candidate 2. You grab them and add them to the basket (res = [1, 2]).
# 	• You check your basket size. It now has 2 people! You have reached your target (\(k = 2\)).

