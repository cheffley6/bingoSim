import numpy as np

# We'll be calculating the probability of pulling 6 B's in a row

# Here are some rules about bingo cards that might be usefule to us:
#   1) There are 5 columns: B, I, N, G, O
#   2) Each column chooses 5 numbers from a range of 15 up to 75 (i.e. B = [1,15], I = [16,30], etc)
#   3) The center space (in column N) is a free space, so is always filled

# And some rules about the game in general:
#   1) The ball call is "randomly" selected from the 75 available numbers
#   2) There are 75! possible permutations of balls drawn. 
#      That's an incredibly large number... roughly 2.5e109


# First, lets calculate the odds that the first 5 draws are all B's.
# In other words, 5 numbers from 1-15 are called in a row, selected from 1-75.
# The probability of 1-15 being called first is 15/75.
# Both numerator and denominator are decremented by one for each consecutive draw 
# (we're calculating permutations)
all_b_first = (15/75)*(14/74)*(13/73)*(12/72)*(11/71)
print("5 B's: " + str(all_b_first))
## "5 B's: 0.00017399224422184098"


# More generally, the probability of a B at any given time in the game 
# is equal to (remaining B's)/(remaining balls)
# So 5 in a row is (product_(b = remaining b's, b-4)) / (product_(r = remaining, r-4))
# Rephrasing the problem posed above,
b_remain = 15
all_remain = 75
top = np.arange(b_remain, b_remain-5, -1)
bot = np.arange(all_remain, all_remain-5, -1)
occurences = [top[i]/bot[i] for i in range(len(top))]
all_b_first = np.prod(occurences)
print("5 B's (new calculation): " + str(all_b_first))
## "5 B's (new calculation): 0.00017399224422184098"


# Now, looking at the scene from Better Call Saul, we can determine the odds of that particular scenario.
# When the B series starts, the following balls have already been pulled:
# 20, 29, 32, 39, 42, 51, 57, 61, 64, 68, 73
# No B's have been called, but we're about to draw 6 in a row
b_remain = 15
all_remain = 75 - 11
top = np.arange(b_remain, b_remain-6, -1)
bot = np.arange(all_remain, all_remain-6, -1)
occurences = [top[i]/bot[i] for i in range(len(top))]
saul = np.prod(occurences)
print("Jimmy's Sanity: " + str(saul))
## "Jimmy's Sanity: 6.675614791444456e-05"


# This represents the probability that any 11 non-B numbers are drawn and then 6 b's are drawn in a row.
# What about the odds of the exact sequence? Well, each draw has probability 1/remaining.
# With 17 draws in the sequence, thats product_(1,17) (1/remaining)
all_remain = 75
bot = np.arange(all_remain, all_remain-17, -1)
occurences = [1/bot[i] for i in range(len(bot))]
exact = np.prod(occurences)
print("Absurd odds: " + str(exact))
## "Absurd odds: 9.474577733877882e-32"
