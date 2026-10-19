class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0 ,len(s)-1

        while left < right:
            while left<right and not self.isAlpha(s[left]):
                left += 1
            while right>left and not self.isAlpha(s[right]):
                right -= 1 
            if s[left].lower() != s[right].lower() :
             return False
            
            left,right = left + 1 ,right -1
        return True

        

    def isAlpha(self,c):
       return  ((ord('A') <=ord(c)<=ord('Z')) or
         (ord('a') <=ord(c)<=ord('z'))or
         (ord('0') <=ord(c)<=ord('9')))        

#  imagine you are a Quality Inspector evaluating a mirror.
# A palindrome is a string that reads the same backward as forward (like "racecar"). However, the input string might contain messy "garbage" characters—like spaces, commas, or exclamation points—that you are told to completely ignore. You only care about actual letters and numbers.
# To check the string, you place your Left Finger (l) at the very beginning of the sentence and your Right Finger (r) at the very end. You will move them inward until they meet in the middle.  

# 1. The helper :AplhaNum
# • The Analogy: Before doing anything, you hire a security guard named alphaNum. Whenever you point at a character, the guard checks its Unicode value (ord) to see if it is a valid letter or number. If it's a space or punctuation mark, the guard says, "This is garbage, ignore it."


# The Walkthrough: Step-by-Step

# Let's say your string is: "A man, a plan!"
# • Your Left Finger (l) starts on "A".
# • Your Right Finger (r) starts on !" (the exclamation mark).

# 1. Skipping Garbage from the Left

# python
# while l < r and not self.alphaNum(s[l]):
#     l += 1
# Use code with caution.
# • The Analogy: You look at your Left Finger. If it is pointing at a space or a comma, you slide it forward (l += 1) until it lands on a real letter or number.
# • In our example: It's already on "A", which is a real letter, so it doesn't move.

# 2. Skipping Garbage from the Right

# python
# while r > l and not self.alphaNum(s[r]):
#     r -= 1
# Use code with caution.
# • The Analogy: At the same time, you look at your Right Finger. If it's pointing at garbage, you slide it backward (r -= 1) toward the center until it finds a valid letter or number.
# • In our example: It starts on !" (garbage) → moves back to "n" (real letter).


# 3. The Mirror Test (The if Check)

# python
# if s[l].lower() != s[r].lower():
#     return False
# Use code with caution.
# • The Analogy: Now that both fingers are resting on valid characters, you compare them. Because capitalization doesn't matter, you convert them both to lowercase (.lower()).
# • In our example: Your left finger has "A" (becomes "a"). Your right finger has "n".
# • Do they match? If "a" did not equal "n", you would immediately stop, break the mirror, and shout False (Not a palindrome).


# 4. Stepping Inward

# python
# l, r = l + 1, r - 1
# Use code with caution.
# • The Analogy: If they do match, you successfully validated this pair! You move both fingers one step closer together toward the middle to check the next set of characters.

# what happens when we add not in front of the guard's answer:

# Character	Guard's Answer (self.alphaNum)	Adding not in front	What it means to the loop
# ',' (Comma)	False	not False → True	"Yes, this is garbage! Enter the loop and slide the finger forward."

# 'A' (Letter)	True	not True → False	"No, this is a real letter! Stop looping, freeze your finger here."


