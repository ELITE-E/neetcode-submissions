class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap = defaultdict(list)

        # for index,char in enumerate(strs):
        #    sorted_string = "".join(sorted(strs[index]))

        #    if sorted_string in hashmap:
        #       return hashmap[tuple(sorted_string)]
        #    else:
        #        return hashmap[tuple(sorted_string)].append(sorted_string)
        # return list(hashmap.values())

        hashmap = defaultdict(list)

        for string in strs:
            sortedS="".join(sorted(string))
            hashmap[sortedS].append(string)
        return list(hashmap.values())

#  The Fatal Flaw: The return Keyword
# • Your Code: Inside your for loop, you have return statements under both the if and the else branches.
# • The Problem: The moment Python hits a return statement, it stops the entire function immediately. Your loop will only ever look at the very first word (strs[0]), execute the else block, and exit the function. It never gets a chance to look at the rest of the words.
# • How the 2nd Code Fixes It: The second code never returns inside the loop. It silently builds the dictionary step-by-step for every single word. It only uses return at the very end, outside the loop, after all words have been processed.
# 2. Misunderstanding .append() and return
# • Your Code: You wrote return hashmap[tuple(sorted_string)].append(sorted_string).
# • The Problem: In Python, the .append() method modifies a list in place and returns None. Because you put return in front of it, your function terminates on the first word and outputs None instead of your anagram list.
# • How the 2nd Code Fixes It: The second code performs the action on a standalone line: res[sortedS].append(s). It updates the dictionary but doesn't try to return anything yet.
# 3. What Goes into the Drawer? (The Intuition)
# • Your Code: You are appending the sorted_string to the hashmap (.append(sorted_string)).
# • The Problem: If the input is ["eat", "tea"], the sorted string for both is "aet". If you append the sorted version, your drawer will just contain ["aet", "aet"]. You have completely lost the original words!
# • How the 2nd Code Fixes It: The second code sorts the word to find the label of the drawer (sortedS), but appends the original, untouched word (s) into the drawer.
# 	• Drawer "aet" gets s ("eat").
# 	• Next round, drawer "aet" gets s ("tea").
# 	• Final drawer content: ["eat", "tea"].
# 4. Overcomplicating the Dictionary Checks
# • Your Code: You wrote an if/else block checking if sorted_string in hashmap:.
# • The Problem: Because you used defaultdict(list), you don't need to check if the key exists. A defaultdict automatically creates an empty list if the key is missing. Furthermore, you converted the string to a tuple (tuple(sorted_string)), which makes your key look like ('a', 'e', 't'), but your if statement was checking for a raw string "aet". They wouldn't match.
# • How the 2nd Code Fixes It: It leverages the power of defaultdict. It simply writes res[sortedS].append(s). If sortedS isn't there, defaultdict makes the list. If it is there, it appends to it. No if/else required!
