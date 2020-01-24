#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3). N cubed. Since the loop will run while a is less than n\*\*3.

b) O(n^2). N squared. Since there are two nested for loops, and both are in range of n.

c) O(n), with n = bunnies. Bunnies is recursive, but it only runs in a linear fashion.

## Exercise II

I'd begin by making a function that takes in n. I'd then do something similar to a binary sort, wherein I'd drop the egg at the midpoint (e.g., midpoint = n // 2) and see if it broke. If it did not break, I'd make midpoint + 1 the start, and search from there to the end. Likewise, if it did break, I'd make the new ending point at midpoint, and search from the start to the new midpoint. I'd keep doing this. I'd return n once n did break, but n - 1 did not.

O(log n), with n being the number of floors. Since we're using binary sort.
