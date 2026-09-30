class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sort(text:str):
         char_list = list(text)
         char_list.sort()
         sorted_text = "".join(char_list)

         return sorted_text


        if sort(s) == sort(t):
            return True
        else:
            return False

        