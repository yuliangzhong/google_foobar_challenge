# Prepare the Bunnies' Escape
# ===========================
# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's
# bunny workers, but once they're free of the work duties the bunnies are going to need to escape
# Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the
# space station are a maze of corridors and dead ends that will be a deathtrap for the escaping
# bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give
# you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you
# can't just remove all obstacles between the bunnies and the escape pods - at most you can remove
# one wall per escape pod path, both to maintain structural integrity of the station and to avoid
# arousing Commander Lambda's suspicions. 

# You have maps of parts of the space station, each starting at a work area exit and ending at the
# door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space
# and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into
# an escape pod is at the bottom right (w-1,h-1). 

# Write a function solution(map) that generates the length of the shortest path from the station door
# to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The
# path length is the total number of nodes you pass through, counting both the entrance and exit
# nodes. The starting and ending positions are always passable (0). The map will always be solvable,
# though you may or may not need to remove a wall. The height and width of the map can be from 2 to
# 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

import unittest

def solution(map):

    # define the state as (i, j, 0/1), where the third element indicates whether a wall is removed
    # we start from (0, 0, 0) and end at (I - 1, J - 1, 0/1)
    I = len(map)
    J = len(map[0])

    l0 = solve_path((0, 0, 0), (I - 1, J - 1, 0), map)
    if l0 == I + J - 1:
        return l0
    else:
        l1 = solve_path((0, 0, 0), (I - 1, J - 1, 1), map)
        return min(l0, l1)

def solve_path(start, end, map):

    I = len(map)
    J = len(map[0])

    # initialize the cost matrix
    cost = [[[float("inf"), float("inf")] for j in range(J)] for i in range(I)]
    cost[start[0]][start[1]][0] = 0

    # initialize the parent matrix
    parent = [[[None for k in range(2)] for j in range(J)] for i in range(I)]

    # initialize the open set
    open_set = {start}

    # use Label Correcting Algorithm to find the shortest path
    while open_set:
        node_i = open_set.pop()
        for child in find_all_children(node_i, map):
            d = cost[node_i[0]][node_i[1]][node_i[2]] + 1
            
            if d < cost[child[0]][child[1]][child[2]] and d < cost[end[0]][end[1]][end[2]]:
                cost[child[0]][child[1]][child[2]] = d
                parent[child[0]][child[1]][child[2]] = node_i

                if child != end:
                    open_set.add(child)
          
    # find the shortest path, just for visualization
    path = []
    tmp = end
    while tmp != None:
        path.append(tmp)
        tmp = parent[tmp[0]][tmp[1]][tmp[2]]
    path = path[::-1]
    print(path)

    return cost[end[0]][end[1]][end[2]] + 1

    
def find_all_children(node, map):
    I = len(map)
    J = len(map[0])
    children = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for di, dj in directions:
        ni, nj = node[0] + di, node[1] + dj  # new i and j
        # Check boundaries
        if 0 <= ni < I and 0 <= nj < J:
            if node[2] == 1:  # Already removed a wall
                if map[ni][nj] == 0:
                    children.append((ni, nj, 1))
            else:  # Hasn't removed a wall yet
                if map[ni][nj] == 0:
                    children.append((ni, nj, 0))
                else:
                    children.append((ni, nj, 1))
    return children


class Testing(unittest.TestCase):

    map1 = [[0, 0, 0, 0, 0, 0], \
            [1, 1, 1, 1, 1, 0], \
            [0, 0, 0, 0, 0, 0], \
            [0, 1, 1, 1, 1, 1], \
            [0, 1, 1, 1, 1, 1], \
            [0, 0, 0, 0, 0, 0]]

    map2 = [[0, 1, 1, 0], \
            [0, 0, 0, 1], \
            [1, 1, 0, 0], \
            [1, 1, 1, 0]]

    map3 = [[0, 1, 1, 0], \
            [0, 0, 1, 1], \
            [1, 1, 0, 0]]
    
    map4 = [[0, 0, 0, 0, 0, 1, 0, 0], \
            [1, 1, 1, 1, 0, 1, 1, 0], \
            [1, 0, 0, 0, 0, 1, 1, 0], \
            [0, 0, 1, 1, 1, 1, 1, 0], \
            [0, 1, 1, 1, 1, 1, 1, 0], \
            [0, 0, 0, 0, 0, 0, 0, 0]]
    
    
    def test_find_all_children(self):
        self.assertEqual(set(find_all_children((0, 0, 0), self.map1)), set([(1, 0, 1), (0, 1, 0)]))
        self.assertEqual(set(find_all_children((2, 1, 0), self.map1)), set([(1, 1, 1), (2, 0, 0), (2, 2, 0), (3, 1, 1)]))
        self.assertEqual(set(find_all_children((1, 1, 1), self.map1)), set([(0, 1, 1), (2, 1, 1)]))
        self.assertEqual(set(find_all_children((2, 1, 1), self.map1)), set([(2, 0, 1), (2, 2, 1)]))
    
    def test_solvePath(self):
        self.assertEqual(solve_path((0, 0, 0), (5, 5, 0), self.map1), 21)
        self.assertEqual(solve_path((0, 0, 0), (3, 3, 0), self.map2), 7)
        self.assertEqual(solve_path((0, 0, 0), (2, 3, 0), self.map3), float("inf"))
        self.assertEqual(solve_path((0, 0, 0), (5, 7, 0), self.map4), 21)

        self.assertEqual(solve_path((0, 0, 0), (5, 5, 1), self.map1), 11)
        self.assertEqual(solve_path((0, 0, 0), (3, 3, 1), self.map2), 7)
        self.assertEqual(solve_path((0, 0, 0), (2, 3, 1), self.map3), 6)
        self.assertEqual(solve_path((0, 0, 0), (5, 7, 1), self.map4), 13)
    
    def test_solution(self):
        self.assertEqual(solution(self.map1), 11)
        self.assertEqual(solution(self.map2), 7)
        self.assertEqual(solution(self.map3), 6)
        self.assertEqual(solution(self.map4), 13)

if __name__ == "__main__":
    unittest.main()