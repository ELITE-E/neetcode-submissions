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