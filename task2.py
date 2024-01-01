# Please Pass the Coded Messages
# ==============================
# You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use
# is... obscure, to say the least. The bunnies are given food on standard-issue plates that are
# stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create
# the numbers in the code. The signal that a number is part of the code is that it is divisible by 3.
# You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little
# trickier. Write a program to help yourself quickly create large numbers for use in the code, given
# a limited number of plates to work with.

# You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the
# largest number that can be made from some or all of these digits and is divisible by 3. If it is
# not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9
# digits. The same digit may appear multiple times in the list, but each element in the list may only
# be used once.

def solution(l):
    
    ones = []
    twos = []

    s = sum(l)
    if s % 3 == 0:
        return int(''.join(map(str, sorted(l, reverse=True))))
    else:
        for i in l:
            if i % 3 == 1:
                ones.append(i)
            elif i % 3 == 2:
                twos.append(i)
    
    if s % 3 == 1:
        if len(ones) != 0:
            ones.sort()
            l.remove(ones[0])
        elif len(twos) >= 2:
            twos.sort()
            l.remove(twos[0])
            l.remove(twos[1])
        else:
            return 0
    elif s % 3 == 2:
        if len(twos) != 0:
            twos.sort()
            l.remove(twos[0])
        elif len(ones) >= 2:
            ones.sort()
            l.remove(ones[0])
            l.remove(ones[1])
        else:
            return 0
    
    if len(l) == 0:
        return 0
    else:
        return int(''.join(map(str, sorted(l, reverse=True))))

print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))