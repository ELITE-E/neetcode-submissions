class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #Check if length is equal
       if len(s)!= len(t):
        return False
       #Initialize hashmaps:empty dicts in python
       counterS ,counterT = {},{}

       for i in range(len(s)):
        counterS[s[i]] = 1 + counterS.get(s[i],0)
        counterT[t[i]] = 1 + counterT.get(t[i],0)

        # • s[i]: Finds the letter at position i in string s.
        # • counterS[s[i]]: Looks up the current count 
        #  for that specific letter.
        # • 1 + ...: Adds 1 to the current
        #  count (adds a tally mark).
        # • counterS[...] = : Saves the updated 
        # number back into the tally sheet.

       return counterS == counterT