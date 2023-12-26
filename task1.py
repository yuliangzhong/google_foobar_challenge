# Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday
# device was completed AND Lambda set a new personal high score in Tetris. To celebrate, the
# Commander ordered cake for everyone -- even the lowliest of minions! But competition among minions
# is fierce, and if you don't cut exactly equal slices of cake for everyone you'll get in big
# trouble. 

# The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the
# cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the
# same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you
# also want to make sure you can serve the entire cake.

# To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into
# a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of
# M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

# Write a function called solution(s) that, given a non-empty string less than 200 characters in
# length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut
# from the cake without leaving any leftovers.

def solution(s):
    n = len(s)
    for i in range(n, 0, -1):
        if n%i == 0:
            length = n // i
            part = s[:length]
            if all(s[j:j+length] == part for j in range(length, n, length)):
                return i
    return 1

s = "abababab"
print(s[99:102])

print(solution(s))
