class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #The largest pile = the largest eat rate (k)
        #The smallest rate(k) can only be 1 not 0 
        #The range of eat rate(k) is btwin both vals
        #The worst possible answer is the larget val ?
       
        l,r = 1,max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            hrs = 0

            for p in piles:
                hrs += math.ceil(float(p) / k)

            if hrs <= h:
                res = k
                r = k - 1
                
            else:
                l = k + 1

        return res


            


#------------------------------------------------------
# The Analogy: The Road Trip & Cruise Control
# Imagine you are driving a car on a long road trip.

# The distance you have to travel is broken up into several checkpoints (the piles of bananas).

# You have a strict arrival deadline (the h hours).

# You must set your cruise control to a specific speed (k) at the beginning of the trip and leave it there.
#------------------------------------------------------
# The Story: Koko’s Goldilocks Speed Quest

# Imagine Koko standing in front of a line of banana piles, staring at a clock with a strict deadline of h hours before the zookeeper returns. She wants to find the slowest possible speed (k) so she doesn't get a stomachache, but just fast enough to finish everything on time.

# 1. Setting the Boundaries (l, r = 1, max(piles) and res = r)

# "What's the slowest I could possibly eat?" Koko thinks. 1 banana per hour (l = 1).
# "What's the absolute fastest I would ever need to eat?" The size of the biggest pile (r = max(piles)), because eating faster than the biggest pile is pointless—you'd clear it in an hour anyway.
# She temporarily sets her official answer (res) to the maximum possible speed, because eating at maximum speed is guaranteed to work.

# 2. The Guessing Game Begins (while l <= r:)

# Instead of testing every single speed from 1 to infinity (which takes forever), Koko decides to play a high-stakes game of "Higher or Lower" with her speed range, continuing as long as her low-speed marker hasn't passed her high-speed marker.

# 3. Picking the Middle Ground (k = (l + r) // 2)

# To be efficient, Koko always tests the exact middle speed between her current slowest and fastest options. Let's call this test speed k.

# 4. The Test Drive (totalTime = 0 loop with math.ceil)

# Koko sets her timer to speed k and simulates walking through every single pile:

# For each pile, she divides the number of bananas by her speed k.

# Because of the rule that an unfinished hour counts as a full hour (even if 1 banana is left over), she rounds up (math.ceil).

# She adds up all those hours into a totalTime.

# 5. Evaluating the Result (Did she make it?)

# If she finished on time (if totalTime <= h:):

# "Success! Speed k actually works!" Koko cheers. She writes down k as her new best record (res = k). But wait... she's ambitious. Could she go even slower? She decides to test slower speeds by pulling her upper limit down: r = k - 1.

# If she ran out of time (else:):

# "Oh no, the zookeeper caught me! Speed k was too slow," Koko groans. She realizes she needs to speed up. She throws away all speeds slower than k and pushes her lower limit up: l = k + 1.

# 6. The Grand Finale (return res)

# The search boundaries finally meet in the middle. Koko looks at her clipboard and reveals res—the absolute slowest, perfectly dialed-in speed she can possibly chew without missing her deadline.