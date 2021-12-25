import numpy as np
import matplotlib.pyplot as plt


class AStarAlgorithm:
    def __init__(self, obstacle_map, origin=(0, 0)):
        self.min_x = origin[0]
        self.min_x = origin[1]
        self.max_x = origin[0] + obstacle_map.shape[1]
        self.max_y = origin[1] + obstacle_map.shape[0]
        self.obstacle_map = obstacle_map
        self.motion = self.get_motion_model()

    class Node:
        def __init__(self, o, x, y, parent, cost):
            self.o = o
            self.x = x
            self.y = y
            self.parent = parent
            self.cost = cost

        def get_coords(self):
            return(self.x, self.y)

    def search(self, start_x, start_y, start_o, goal_x, goal_y, goal_o):
        start = self.Node(start_o, start_x, start_y, None, 0)
        goal = self.Node(goal_o, goal_x, goal_y, None, 0)

        plt.figure(figsize=(10, 10))
        plt.imshow(self.obstacle_map, origin='lower', cmap='gray')
        plt.scatter(x=[start.x, goal.x], y=[start.y, goal.y], c='b')
        plt.show()
        while True:

    @staticmethod
    def heuristic(start, finish):
        return np.linalg.norm([start.get_coords(), finish.get_coords()])

    @staticmethod
    def motion_model():
        # orientation, do, dx, dy, cost
        # VVVVVVVVVVV
        # 0: 0 degree x_axis +ve
        # 1: 90 degreee y_axis +ve
        # 2: 180 degree x_axis -ve
        # 3: 270 degree y_axis -ve
        #           o   do      dx      dy      cost
        motion = np.array([[0,   0,      10,     0,     10],     # 10 steps along the +ve x_axis
                           # 10 steps along the +ve x_axis then a left turn and another 10 steps along +ve y_axis
                           [0,   -1,     10,     10,    20],
                           # 10 steps along the +ve x_axis then a right turn and another 10 steps along -ve y_axis
                           [0,   1,      10,     -10,   20],
                           # 10 steps along the +ve y_axis
                           [1,   0,      0,      10,    10],
                           # 10 steps along the +ve y_axis then a left turn and another 10 steps along -ve x_axis
                           [1,   -1,     -10,    10,    20],
                           # 10 steps along the +ve y_axis then a right turn and another 10 steps along +ve x_axis
                           [1,   1,      10,     10,    20],
                           # 10 steps along the -ve x_axis
                           [2,   0,      -10,    0,     10],
                           # 10 steps along the +ve x_axis then a left turn and another 10 steps along -ve y_axis
                           [2,   -1,     -10,    -10,   20],
                           # 10 steps along the +ve x_axis then a right turn and another 10 steps along +ve y_axis
                           [2,   1,      -10,    10,    20],
                           # 10 steps along the -ve y_axis
                           [3,   0,      0,      -10,   10],
                           # 10 steps along the -ve y_axis then a left turn and another 10 steps along +ve x_axis
                           [3,   -1,     10,     -10,   20],
                           [3,   1,      -10,    -10,   20]])    # 10 steps along the -ve y_axis then a right turn and another 10 steps along -ve x_axis

        return motion


# Defining the borders
obstacle_map = np.zeros((1010, 1010))
obstacle_map[:, :10] = -1
obstacle_map[:10, :] = -1
obstacle_map[:, -10:] = -1
obstacle_map[-10:, :] = -1

# Defining the obstacles
obstacle_map[800:, :200] = -1
obstacle_map[:800, 400:600] = -1
obstacle_map[600:, 700:800] = -1
plt.figure(figsize=(10, 10))
plt.imshow(obstacle_map, origin='lower', cmap='gray')
plt.scatter(x=[50, 950], y=[50, 950], c='b')
plt.scatter(x=100, y=100, color='g', alpha=0.3, marker='s')
plt.plot([1, 800], [1, 800])
plt.show()
