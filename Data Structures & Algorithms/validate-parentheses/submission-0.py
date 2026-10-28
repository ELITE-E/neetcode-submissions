class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" :"(",
            "]" :"[",
            "}":"{"
        }

        for char in s :
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False


# Think of this classic Valid Parentheses solution as a bouncer managing a VIP coat check at a nightclub, where couples arrive together but must leave in a strict, perfectly nested order.

# The rule of the club is simple: The last person to check in their coat must be the first one to leave with their partner.
# Here is how the code sets up the nightclub:

# Code Element	Analogy Concept
# stack = []	The coat check rack. Items are hung up one after another. You can only easily see or remove the most recent coat hung at the very end of the rack (stack[-1]).
# closeToOpen	The relationship registry. It maps every closing partner (), ], }) to their exact matching opening partner ((, [, {).


# Walking Through the Line (for char in s)

# The bouncer looks at each character in the string one by one as they walk through the door:

# 1. An Opening Bracket Arrives (else: stack.append(char))

# If a character is an opening bracket ((, [, or {), it represents a partner entering the club alone.
# • Analogy: The bouncer takes their coat and hangs it up on the end of the rack (stack.append).

# 2. A Closing Bracket Arrives (if char in closeToOpen)

# If a character is a closing bracket (), ], or }), it represents a partner arriving to pick up their significant other and leave the club. The bouncer checks the registry to see exactly who they are looking for (closeToOpen[char]).
# The bouncer checks two things (if stack and stack[-1] == ...):
# • Is the rack empty? If a closing partner shows up but the rack is empty (not stack), it means they are trying to leave with a partner who never even entered the club! Immediate rejection (return False).
# • Is it a perfect match? The bouncer looks at the very last coat hung on the rack (stack[-1]). If it matches the partner they are looking for, the bouncer removes the coat from the rack (stack.pop()), and the couple happily leaves the club together.
# • Is it a mismatched partner? If the last coat on the rack belongs to a different type of bracket, the strict nested order is broken. Immediate rejection (return False).

# The Final Inspection (return True if not stack else False)

# Once the entire line of characters has been processed, the bouncer looks back at the coat check rack one last time:
# • If the rack is completely empty (not stack): Every single person found their correct partner, and they all left in the perfect order. The string is valid (True).
# • If there are still coats left on the rack: Some opening brackets entered the club but were abandoned because their closing partners never showed up. The string is invalid (False).
