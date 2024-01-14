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

def solution(dimensions, your_position, trainer_position, distance):
    targets, yimgs, _ = iterate_points_in_circle(dimensions, your_position, trainer_position, distance)
    return len(filtering(targets, yimgs, your_position))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# pos should not be all zeros
def cartesian_to_polar(pos):
    g = gcd(abs(pos[0]), abs(pos[1]))
    return pos[0] // g, pos[1] // g, g

def update_dict(dictionary, dx, dy):
    if dx == 0 and dy == 0:
        return
    rx, ry, g = cartesian_to_polar((dx, dy))
    dictionary[(rx, ry)] = min(g, dictionary.get((rx, ry), float("inf")))

def iterate_points_in_circle(dimensions, your_position, trainer_position, distance):
    targets, yimgs = {}, {}
    centers = []
    min_x, min_y = your_position[0] - distance - dimensions[0], your_position[1] - distance - dimensions[1]
    max_x, max_y = your_position[0] + distance + dimensions[0], your_position[1] + distance + dimensions[1]
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if not (x % (2 * dimensions[0]) or y % (2 * dimensions[1])): # if (x, y) is the center of a pattern
                centers.append((x, y))
                for sign in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    img_x, img_y = x + sign[0] * your_position[0], y + sign[1] * your_position[1]
                    targ_x, targ_y = x + sign[0] * trainer_position[0], y + sign[1] * trainer_position[1]
                    di_x, di_y = img_x - your_position[0], img_y - your_position[1]
                    dt_x, dt_y = targ_x - your_position[0], targ_y - your_position[1]
                    if (0 < di_x ** 2 + di_y ** 2 <= distance ** 2):
                        update_dict(yimgs, di_x, di_y)
                    if (0 < dt_x ** 2 + dt_y ** 2 <= distance ** 2):
                        update_dict(targets, dt_x, dt_y)
    return targets, yimgs, centers

def filtering(targets, yimgs, your_position):
    return [
        (target_key[0] * target_value + your_position[0], target_key[1] * target_value + your_position[1])
        for target_key, target_value in targets.items()
        if target_value < yimgs.get(target_key, float('inf'))
    ]

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
    for sign in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        plt.scatter(*(center + sign * ypos), color='green', s=6)
        plt.scatter(*(center + sign * tpos), color='red', s=6)

def plot_solution(dimensions, your_position, trainer_position, distance):
    dim, ypos, tpos = map(np.array, (dimensions, your_position, trainer_position))
    targets, yimgs, centers = iterate_points_in_circle(dim, ypos, tpos, distance)
    sol = filtering(targets, yimgs, ypos)

    for center in centers:
        plot_pattern(np.array(center), dim, ypos, tpos)
    for point in sol:
        plt.plot([ypos[0], point[0]], [ypos[1], point[1]], color='purple', linewidth=0.5)

    # plot room
    plot_rectangle([0, 0], dimensions, "-", linewidth=1.5)
    plt.scatter(*your_position, color='green')
    plt.scatter(*trainer_position, color='red')
    # plot range
    plt.gca().add_patch(patches.Circle(your_position, distance, fill=False))

    plt.axis('equal')
    plt.axis('off')
    plt.show()

# ----------------------------------------------------------------
# test code
# ----------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    dimensions = [3, 2]
    your_position = [1, 1]
    trainer_position = [2, 1]
    distance = 4
    plot_solution(dimensions, your_position, trainer_position, distance)

    def test_gcd(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(0, 4), 4)
        self.assertEqual(gcd(7, 0), 7)
        self.assertEqual(gcd(4, 4), 4)
        self.assertEqual(gcd(4, 6), 2)
        self.assertEqual(gcd(6, 4), 2)
        self.assertEqual(gcd(4, 7), 1)

    def test_cartesian_to_polar(self):
        self.assertEqual(cartesian_to_polar((6, 4)), (3, 2, 2))
        self.assertEqual(cartesian_to_polar((-4, 6)), (-2, 3, 2))
        self.assertEqual(cartesian_to_polar((4, -6)), (2, -3, 2))
        self.assertEqual(cartesian_to_polar((-6, -4)), (-3, -2, 2))
        self.assertEqual(cartesian_to_polar((0, 5)), (0, 1, 5))
        self.assertEqual(cartesian_to_polar((-7, 0)), (-1, 0, 7))

    def test1(self):
        dimensions = [3, 2]
        your_position = [1, 1]
        trainer_position = [2, 1]
        distance = 4
        self.assertEqual(solution(dimensions, your_position, trainer_position, distance), 7)
    
    def test2(self):
        dimensions = [300, 275]
        your_position = [150, 150]
        trainer_position = [185, 100]
        distance = 500
        self.assertEqual(solution(dimensions, your_position, trainer_position, distance), 9)

if __name__ == '__main__':
    unittest.main()