class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # Initialize an empty string 

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        
        res,i =  [],0
        
        while i < len(s):
            j = i
             
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length 
        return res


# The Setup: What the Data Looks Like

# If your input list was ["cat", "stop"], the encode function turned it into a single string:
# "3#cat4#stop"
# Here is how the inspector un-packs it step-by-step using the two pointers, i and j.

# 1. res, i = [], 0

# • The Analogy: You set down an empty box (res) to hold the unpacked words. You place your left finger (i) at the very beginning of the train (index 0).


# 2. while i < len(s): j = i

# • The Analogy: As long as your left finger hasn't reached the end of the train, you place your right finger (j) right next to your left finger.
# • Right now, both i and j are pointing at the character "3".


# 3. while s[j] != "#": j += 1

# • The Analogy: Your left finger (i) stays glued to the start of the number. You slide your right finger (j) forward until it bumps into the # wall.
# • In our case, j doesn't have to move far because "3" is followed immediately by #. So j stops right on the #.


# 4. length = int(s[i:j])

# • The Analogy: You read the text trapped between your two fingers (from i to j). The characters between them make up the string "3". You convert that to the actual integer 3.
# • Now you know: "The next word is exactly 3 characters long!"


# 5. res.append(s[j + 1 : j + 1 + length])

# • The Analogy: Since j is currently pointing at the #, you know the actual word starts right after it, at j + 1.
# • You grab a pair of scissors, cut out exactly 3 characters starting from j + 1 (which grabs "c", "a", "t"), and toss "cat" into your unpacked box.


# 6. i = j + 1 + length

# • The Analogy: You lift your left finger (i) and hop it completely over the word you just processed.
# • Where does it land? It lands right at the beginning of the next size number ("4").


# The Next Loop Round

# The outer loop runs again.
# 1. Your left finger (i) is now on "4".
# 2. You place your right finger (j) there too.
# 3. You slide j forward until it hits the next #.
# 4. You read the number between i and j, which is 4.
# 5. You cut out the next 4 characters after the # ("s", "t", "o", "p").
# 6. You jump your left finger (i) forward past "stop".
# Now i is at the end of the string, the loop ends, and you successfully return ["cat", "stop"].

