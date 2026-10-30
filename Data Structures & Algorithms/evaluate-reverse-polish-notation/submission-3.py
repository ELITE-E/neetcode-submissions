class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == '+':
                stack.append(stack.pop()+stack.pop()) 

            elif char == '*':
                stack.append(stack.pop() * stack.pop())

            elif char == '-':
                a , b = stack.pop(),stack.pop()
                stack.append(b-a)

            elif char == '/':
                a , b =  stack.pop(),stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))
        return stack[0]




# The Big Idea: Why This Solution Works
# Computers are great at following simple, mechanical rules, but they don't naturally understand math expressions with parentheses and order of operations.

# The brilliant trick behind this code is reversing the roles of numbers and operators.

# Instead of looking at the whole expression at once, the code scans through the tokens one by one from left to right.

# Whenever it sees a number, it sets it aside (on the stack) waiting to be used.

# Whenever it sees an operator (+, -, *, /), it immediately reaches for the most recently saved numbers, does the math, and saves the new answer back down.

# Because a stack is Last-In, First-Out (LIFO), the numbers you just wrote down are always the exact ones the next operator needs. By the time you reach the end of the list, all the math has collapsed down into a single final number.

# The Analogy: The "Assembly Line" Chef
# Imagine you are a chef working on a very strict, fast-paced assembly line kitchen. Your workspace has a single vertical plate dispenser (the stack).

# Plates can only be stacked on top of each other. You can only grab the top plate (pop), or put a new plate on the very top (append).

# Here is how you process the orders as they come down the belt:

# When an ingredient/number comes down the belt (else):

# It's just a raw ingredient (like a potato or a tomato). You put a label on a plate, put the number on it, and stack it on top of your pile.

# When a + (Addition machine) comes down the belt:

# This machine yells, "Combine the last two things we prepped!"

# You reach out and grab the top plate (stack.pop()), then grab the next plate down (stack.pop()).

# You add their values together, write the total on a fresh plate, and slam that new plate right back onto the top of the stack.

# When a - or / (Subtraction or Division machine) comes down the belt:

# Order matters here! The machine yells, "Subtract the newest ingredient from the one before it!"

# You grab the top plate (a, the newest one).

# You grab the plate right below it (b, the older one).

# You calculate b - a (or b / a), write that result on a fresh plate, and put it on top of the stack.

# At the very end of the shift:

# The belt stops. You look at your stack. There is only one plate left sitting on the dispenser. That single plate holds your final answer (return stack[0]).


# What the Question is Asking
# You are given a list (array) of strings called tokens. This list contains a mix of numbers (represented as strings, like "1") and operators ("+", "-", "*", "/").

# Your job is to read through this list, perform the math as the operators appear, and return the final single integer result.

# Step-by-Step Walkthrough of the Example
# Let's look at the example provided:tokens = ["1", "2", "+", "3", "*", "4", "-"]

# How do you read this like a computer? You scan from left to right:

# "1": It's a number. Keep track of it.

# "2": It's a number. Keep track of it.

# "+": It's an operator! This means you take the two most recent numbers you encountered (1 and 2) and add them together: 1 + 2 = 3.

# Now replace those three tokens with the result (3). Your working list becomes: [3, "3", "*", "4", "-"]

# "3": It's a number. Keep track of it.

# "*": It's an operator! Take the two most recent numbers (3 and 3) and multiply them: 3 * 3 = 9.

# Replace them with the result (9). Your list becomes: [9, "4", "-"]

# "4": It's a number. Keep track of it.

# "-": It's an operator! Take the two most recent numbers (9 and 4) and subtract them: 9 - 4 = 5.

# Replace them with the result (5).

# You've reached the end of the tokens list, and your final remaining value is 5. This matches the explanation: ((1 + 2) * 3) - 4 = 5.

# Important Quirks to Keep in Mind
# As you think about how to tackle this conceptually, keep these two rules in mind:

# Order Matters for Subtraction and Division:
# In RPN, when you see a subtraction operator like a b -, it means a - b, not b - a. The first number you encountered goes on the left side of the operator.

# Integer Division Truncation:
# When dividing integers, division always truncates toward zero (meaning it chops off the decimals, moving closer to zero). For example:

# 6 / 4 = 1 (instead of 1.5)

# -6 / 4 = -1 (instead of -1.5, which would truncate toward negative infinity if it weren't heading toward zero).

# The Conceptual Riddle to Ponder
# Think about how you are holding onto numbers as you scan from left to right. Every time you see a number, you save it. Every time you see an operator, you grab the most recent numbers you saved, compute the result, and save that new result.