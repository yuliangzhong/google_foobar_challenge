# Bringing a Gun to a Trainer Fight
# =================================
# Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately, you
# grabbed a beam weapon from an abandoned storeroom while you were running through the station, so
# you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as
# well as to the bunny trainers: its beams reflect off walls, meaning you'll have to be very careful
# where you shoot to avoid bouncing a shot toward yourself!

# Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause
# damage. You also know that if a beam hits a corner, it will bounce back in exactly the same
# direction. And of course, if the beam hits either you or the bunny trainer, it will stop
# immediately (albeit painfully). 

# Write a function solution(dimensions, your_position, trainer_position, distance) that gives an
# array of 2 integers of the width and height of the room, an array of 2 integers of your x and y
# coordinates in the room, an array of 2 integers of the trainer's x and y coordinates in the room,
# and returns an integer of the number of distinct directions that you can fire to hit the elite
# trainer, given the maximum distance that the beam can travel.

# The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite trainer
# are both positioned on the integer lattice at different distinct positions (x, y) inside the room
# such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel
# before becoming harmless will be given as an integer 1 < distance <= 10000.

# For example, if you and the elite trainer were positioned in a room with dimensions [3, 2],
# your_position [1, 1], trainer_position [2, 1], and a maximum shot distance of 4, you could shoot in
# seven different directions to hit the elite trainer (given as vector bearings from your location):
# [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at
# bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2]
# bounces off the left wall and then the bottom wall before hitting the elite trainer with a total
# shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before
# hitting the elite trainer with a total shot distance of sqrt(5).
signs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def solution(dimensions, your_position, trainer_position, distance):
    # use 'mirrors' to help me find all possible directions!
    # mirror once in the left wall, once in the bottom wall
    # then we get a pattern that replicates ... forever
    pass

# ----------------------------------------------------------------
# The code below is a visulization helper. 
# You know, how can a robotist work without visualization?
# ----------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def plot_rectangle(p1, p2, style='--', color='black', linewidth=0.75):
    x = [p1[0], p2[0], p2[0], p1[0], p1[0]]
    y = [p1[1], p1[1], p2[1], p2[1], p1[1]]
    plt.plot(x, y, linestyle=style, color=color, linewidth=linewidth)

def plot_pattern(center, dim, ypos, tpos):
    offsets = [dim, -dim, np.array([dim[0], -dim[1]]), np.array([-dim[0], dim[1]])]
    for offset in offsets:
        plot_rectangle(center, center + offset, style='--', color='black')
    for sign in signs:
        plt.scatter(*(center + sign * ypos), color='green', s=6)
        plt.scatter(*(center + sign * tpos), color='red', s=6)

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def xy_to_rad(pos):
    g = gcd(abs(pos[0]), abs(pos[1]))
    return (pos[0] // g, pos[1] // g, g)

def iterate_points_in_circle(dim, ypos, tpos, dist):
    targets, yimgs, centers = [], [], []
    min_pos = ypos - dist - dim
    max_pos = ypos + dist + dim
    for x in range(min_pos[0], max_pos[0] + 1):
        for y in range(min_pos[1], max_pos[1] + 1):
            pos = np.array([x, y])
            if not (pos % (2 * dim)).any(): # if (x, y) is the center of a pattern
                centers.append(pos)
                for sign in signs:
                    yimg = pos + sign * ypos
                    timg = pos + sign * tpos
                    if np.linalg.norm(yimg - ypos) <= dist:
                        yimgs.append(yimg)
                    if np.linalg.norm(timg - ypos) <= dist:
                        targets.append(timg)    
    return targets, yimgs, centers

def filtering(targets, yimgs, ypos):
    pass

# ----------------------------------------------------------------
# test code
# ----------------------------------------------------------------
dimensions = [4, 3]
your_position = [1, 1]
trainer_position = [2, 2]
distance = 12

dim, ypos, tpos = map(np.array, (dimensions, your_position, trainer_position))
targets, _, centers = iterate_points_in_circle(dim, ypos, tpos, distance)
for center in centers:
    plot_pattern(center, dim, ypos, tpos)
for target in targets:
    plt.plot([ypos[0], target[0]], [ypos[1], target[1]], color='purple', linewidth=0.5)

# plot room
plot_rectangle([0, 0], dimensions, "-", linewidth=1.5)
plt.scatter(*your_position, color='green')
plt.scatter(*trainer_position, color='red')
# plot range
plt.gca().add_patch(patches.Circle(your_position, distance, fill=False))

plt.axis('equal')
plt.axis('off')
plt.show()