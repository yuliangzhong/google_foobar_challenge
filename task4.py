def solution(n):
    # suppose i, j are natural numbers (0, 1, 2, ...)

    # define g(i, j) as the number of different staircases we can build
    # with i bricks in total and j bricks as the maximum step
    
    # suppose one-column staircase is allowed. so g(n, n) = 1
    # by convention, g(0, 0) = 1

    # define h(i, j) = g(i, j) + g(i, j - 1) + ... + g(i, 0)
    # so the sol(i) = h(i, i) - 1

    # we have h(i, j) = g(i, j) + h(i, j - 1)
    # and from the story, we know
    # g(i, j) = h(i - j, j - 1)
    
    # ------------------------

    # define a G table to store g(i, j)
    G = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        G[i][i] = 1
    
    for i in range(3, n + 1):
        for j in range(1, i):
            G[i][j] = sum(G[i - j][k] for k in range(j))

    # ------------------------
    # print("G table:")
    # for l in G:
    #     print(l)
    return sum(G[n][k] for k in range(n + 1)) - 1

print(solution(3))
print(solution(7))
print(solution(200))