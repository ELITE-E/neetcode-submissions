class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = [] #pair:[temp,index]

        for idx ,temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:

                stackT ,stackInd = stack.pop()
                res[stackInd] = (idx - stackInd)

            stack.append([temp,idx]) 
        return res       




# The Analogy: The Weather Watchers' Waiting Room
# Imagine a long hallway with a single bench. People walk in day by day, holding a clipboard with two pieces of info: their temperature and which day they arrived.

# The golden rule of this bench is: Everyone sitting on the bench must be in strict descending order of temperature (coldest at the front/top, or rather, people waiting for a warmer day).

# Here is how the days unfold as you walk down the street:

# 1. When a Colder or Equal Day Arrives (stack.append((t, i)))
# What happens: A new person walks in with a temperature that is lower than or equal to the person currently sitting at the front of the bench.

# In the analogy: They take a seat on the bench and wait. They haven't found a warmer day yet, so they just sit tight.

# 2. When a Hotter Day Arrives (while stack and t > stack[-1][0]:)
# What happens: A brand-new person walks in, and they are hotter than the person sitting at the front of the bench.

# In the analogy: This hot day acts like a celebrity walking into a waiting room! They don't just sit down. Instead, they look at the front of the bench, tap the person sitting there on the shoulder, and say: "Hey! My temperature is higher than yours! Your wait is over!"

# They calculate how many days that person waited (current_day_index - their_arrival_index), write it down on the master scoreboard (res[stackInd] = i - stackInd), and kick them off the bench (stack.pop()).

# The magic part: They don't stop there! They look at the next person still sitting on the bench. Are they also colder than this new hot day? If yes, kick them off and give them their answer too, continuing in a loop (while) until they hit someone who is actually hotter than them or the bench is empty.

# Finally, once the hot day has cleared out everyone they are warmer than, they take a seat on the bench to wait for an even hotter day.