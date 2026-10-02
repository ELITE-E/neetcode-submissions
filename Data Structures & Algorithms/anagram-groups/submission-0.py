class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for charactest [a-z];how many does each string have 
        #so the hashmap is :character patterns from
        #each string as (key):List(Ones that share same vals)
        #value 

        # When you initialize a defaultdict, you pass a callable object known as the default_factory. 
        # If you attempt to access or modify a missing key using bracket notation (d[key]), defaultdict automatically invokes this default_factory to generate and insert a default value for that key.
        #Standard dic raised KeyError 
        #You cnat accsee  what you dont posses vs can access what you dont posses
        hashmap = defaultdict(list)#mapping charCount to list of anagrams

        for string in strs :
            count=[0] * 26
            
            for char in string:
                #In mathematics and computer science, an ordinal number refers to the position of an element in a sequential order.
                #  The ord() function gives you the sequential position (or numeric code point) of that character within the Unicode character set.
                count[ord(char)-ord("a")]+=1 

            hashmap[tuple(count)].append(string)
        return list(hashmap.values())
#Mental model

# imagine you are a sorter at a post office, and your job is to create a unique "recipe barcode" for every word based only on the ingredients (letters) it contains.
# Here is exactly what is happening at each step:

# 1. count = [0] * 26

# The Mental Image: Picture an empty egg carton with 26 slots, laid out in a straight row.
# • Each slot represents a letter of the alphabet, from left to right: slot 0 is a, slot 1 is b, slot 2 is c, all the way to slot 25 which is z.
# • Right now, every single slot is empty (contains a 0).

# 2. count[ord(char) - ord("a")] += 1

# The Mental Image: You pick up a word, like "cat", and look at its letters one by one.
# • First, you see 'c'. You need to figure out which slot 'c' belongs to.
# • You look up their Unicode code numbers: ord('c') is 99, and ord('a') is 97.
# • You subtract them: \(99 - 97 = 2\). This tells you that 'c' belongs in slot index 2.
# • You drop a marble into slot 2. The carton now looks like this: [0, 0, 1, 0, 0...]
# • Next, you see 'a'. ord('a') - ord('a') is \(97 - 97 = 0\). You drop a marble into slot 0.
# • Next, you see 't'. You do the math, find its slot, and drop a marble there.
# Once the word "cat" is done, your egg carton has exactly three marbles in it: one in the a slot, one in the c slot, and one in the t slot.

# 3. hashmap[tuple(count)].append(string)

# The Mental Image: Now that the word is fully counted, you need to store it.

# • tuple(count): You freeze the egg carton in resin so the marbles can't roll around anymore. This frozen, unchangeable state is your tuple. It acts like a unique fingerprint or barcode for that exact combination of letters. For both "cat" and "act", the frozen carton looks identical because they have the exact same marbles in the exact same slots.

# • hashmap[...]: In front of you is a massive wall of filing cabinets (hashmap). You look at your frozen egg carton barcode. If a cabinet drawer already exists with that exact barcode, you slide it open. If it doesn't exist, you instantly build a new drawer and slap that barcode label on the front.

# • .append(string): You write the actual word "cat" on a piece of paper and drop it into that drawer.
# When you later process "act", it generates the exact same frozen barcode. You march up to the wall, find the same drawer you just used for "cat", open it, and drop "act" right next to it.