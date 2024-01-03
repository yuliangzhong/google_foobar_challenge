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

def solution(map):

    I = len(map)
    J = len(map[0])

    # initialize the distance matrix
    dist = [[float("inf") for j in range(J)] for i in range(I)]
    dist[0][0] = 0

    # initialize the parent matrix
    parent = [[None for j in range(J)] for i in range(I)]

    # initialize the open set
    open_set = {(0, 0)}

    # use Label Correcting Algorithm to find the shortest path
    while open_set:
        node_i = open_set.pop()
        for child in find_all_children(node_i, I, J, map):
            d = dist[node_i[0]][node_i[1]] + 1
            
            if d < dist[child[0]][child[1]] and d < dist[I - 1][J - 1]:
                dist[child[0]][child[1]] = d
                parent[child[0]][child[1]] = node_i

                if child != (I - 1, J - 1):
                    open_set.add(child)
          
    # find the shortest path
    path = []
    tmp = (I - 1, J - 1)
    while tmp != None:
        path.append(tmp)
        tmp = parent[tmp[0]][tmp[1]]
    path = path[::-1]
    
    # if the path length is aleady the shortest, return the path length
    if len(path) == I + J - 1:
        return len(path)
    else:
        return "not the shortest path, remove a wall?"
    
def find_all_children(node, I, J, map):
    # find the children of the node
    children = []
    if node[0] >= 1 and map[node[0] - 1][node[1]] == 0:
        children.append((node[0] - 1, node[1]))
    if node[0] <= I - 2 and map[node[0] + 1][node[1]] == 0:
        children.append((node[0] + 1, node[1]))
    if node[1] >= 1 and map[node[0]][node[1] - 1] == 0:
        children.append((node[0], node[1] - 1))
    if node[1] <= J - 2 and map[node[0]][node[1] + 1] == 0:
        children.append((node[0], node[1] + 1))
    return children

print(solution(map1))
print(solution(map2))
