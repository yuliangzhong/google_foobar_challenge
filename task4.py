# The Grandest Staircase Of Them All
# ==================================
# With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic
# stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's
# personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

# Lambda has given you an overview of the types of bricks available, plus a budget. You can buy
# different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue
# lace bricks). Commander Lambda wants to know how many different types of staircases can be built
# with each amount of bricks, so they can pick the one with the most options.

# Each type of staircase should consist of 2 or more steps. No two steps are allowed to be at the
# same height - each step must be lower than the previous one. All steps must contain at least one
# brick. A step's height is classified as the total amount of bricks that make up that step.
# For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step
# having a height of 2 and the second step having a height of 1: (# indicates a brick)

# #
# ##
# 21

# When N = 4, you still only have 1 staircase choice:

# #
# #
# ##
# 31

# But when N = 5, there are two ways you can build a staircase from the given bricks. The two
# staircases can have heights (4, 1) or (3, 2), as shown below:

# #
# #
# #
# ##
# 41

# #
# ##
# ##
# 32

# Write a function called solution(n) that takes a positive integer n and returns the number of
# different staircases that can be built from exactly n bricks. n will always be at least 3 (so you
# can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

def solution(n):
    # suppose i, j are natural numbers (0, 1, 2, ...)

    # define g(i, j) as the number of different staircases we can build
    # with i bricks in total and j bricks as the maximum step
    
    # suppose one-column staircase is allowed. so g(n, n) = 1
    # by convention, g(0, 0) = 1

    # define h(i, j) = g(i, j) + g(i, j - 1) + ... + g(i, 0)
    # so the sol(i) = h(i, i) - 1

    # From the story, we know
    # g(i, j) = h(i - j, j - 1)
    
    # ------------------------

    # define a G table to store g(i, j)
    G = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        G[i][i] = 1
    
    for i in range(3, n + 1):
        for j in range(1, i):
            G[i][j] = sum(G[i - j][k] for k in range(j))

    return sum(G[n][k] for k in range(n + 1)) - 1

print(solution(3))
print(solution(7))
print(solution(200))