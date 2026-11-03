class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(pos,speed) for pos,speed in zip(position,speed)]
        pair.sort(reverse=True)
        stack = []

        for pos,speed in pair:
            time = (target-pos)/speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                 stack.pop()
        return len(stack)



# 💡 Basic Example

# If you have a list of names and a list of ages, you can pair them up instantly:
# python
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]

# # Combine them using zip
# zipped = zip(names, ages)

# # Convert the lazy iterator to a list to view it
# print(list(zipped))
# # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# The Analogy: The Single-Lane Mountain Road
# Imagine a single-lane mountain highway where no overtaking is allowed. Cars are scattered along the road at different starting positions, driving toward a resort at the very top of the mountain (the target).

# Because nobody can pass anyone else, if a fast car catches up to a slow car ahead of it, it gets stuck behind it. They merge into a single "fleet" and crawl along at the speed of the slow car.

# Your job is to figure out: How many distinct groups (fleets) of cars will cross the finish line at the top?

# Here is how the code's logic mirrors this mountain road:

# Step-by-Step Breakdown of the Code
# 1. Pairing and Sorting (pair.sort(reverse=True))
# What the code does: It pairs each car's starting position with its speed, then sorts them in reverse order (from the car closest to the finish line down to the car furthest behind).

# In the analogy: You stand at the finish line and look down the mountain. You evaluate the cars in order—starting with the car closest to the top, then the next closest, and so on, moving backward down the mountain.

# 2. Calculating Travel Time ((target - p) / s)
# What the code does: For every car, it calculates how many hours it would take to reach the finish line if it drove all by itself: (Distance remaining) / Speed.

# In the analogy: You look at a car and say, "If nobody blocked you, it would take you 4 hours to reach the resort." You write that arrival time down on a notepad (pushing it onto your stack).

# 3. The Traffic Jam Check (if stack[-1] <= stack[-2]: stack.pop())
# What the code does: As you look at the next car back, you compare its travel time with the car immediately ahead of it (which is sitting on top of your stack).

# If the car behind takes less time (or the exact same time) to reach the top as the car ahead of it, that means it's driving faster.

# Since there's only one lane, it will inevitably crash into the car ahead of it and join its fleet.

# Because they become one fleet, you cross the faster car off your notepad (stack.pop()) because it's now trapped behind the leader!

# In the analogy:

# Imagine Car A (ahead) takes 5 hours to reach the top.

# Car B (behind it) calculates it can make it in 3 hours.

# Because Car B is faster, it will zoom up the mountain and slam right into the back of Car A. From that point on, Car B is forced to match Car A's slow speed. They cross the finish line together as one fleet. Thus, Car B "disappears" into Car A's group.

# The Grand Finale (return len(stack))
# By the time you finish checking every car from the front of the pack to the back, any car that got stuck behind a leader has been popped off your notepad.

# Whatever cars are left on your notepad represent the ultimate leaders of each independent fleet. You simply count how many items remain (len(stack)), and that's your final answer!