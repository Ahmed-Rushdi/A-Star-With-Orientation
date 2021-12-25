# Ahmed Rushdi Mohammed 20180008

import math
import numpy as np
import matplotlib.pyplot as plt


class AStarAlgorithm:
    def __init__(self, obstacle_map, origin=(0, 0)):
        self.min_x = 10
        self.min_y = 10
        self.max_x = 999
        self.max_y = 999
        self.obstacle_map = obstacle_map
        self.motion = self.motion_model()

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

        open_nodes, closed_nodes = dict(), dict()
        open_nodes[(start.o, start.x, start.y)] = start
        j = 0
        while True:
            if len(open_nodes) == 0:
                print("No solution..")
                break

            current_i = min(
                open_nodes, key=lambda o: open_nodes[o].cost + self.heuristic(start=open_nodes[o], finish=goal))
            current = open_nodes[current_i]

            plt.scatter(current.x, current.y, color='r',
                        alpha=0.1, marker='s')  # , s=100)
            
            # Comment the line below to disable animations and make the code much faster
            plt.pause(0.00001)
            
            
            if current.x == goal.x and current.y == goal.y and current.o == goal.o:
                print("Find goal")
                goal.parent = current.parent
                goal.cost = current.cost
                break
            # Remove the item from the open set
            del open_nodes[current_i]

            # Add it to the closed set
            closed_nodes[current_i] = current

            for i in np.where(self.motion[:, 0] == current.o)[0]:
                new_o = (current.o + self.motion[i, 1]) % 4
                new_x = current.x + self.motion[i, 2]
                new_y = current.y + self.motion[i, 3]
                new_cost = current.cost + self.motion[i, 4]
                if new_x > self.max_x or new_x < self.min_x or new_y > self.max_y or new_y < self.min_y or obstacle_map[new_y, new_x] == -1 or (new_o, new_x, new_y) in closed_nodes or (new_o, new_x, new_y) in open_nodes:
                    continue
                else:
                    open_nodes[(new_o, new_x, new_y)] = self.Node(
                        new_o, new_x, new_y, current, new_cost)
            j += 1
            print("iteration "+str(j)+' cost '+str(current.cost) + ' hueristic ' + str(self.heuristic(current, goal)) +
                  ' (x,y,o) ' + str((current.x, current.y, current.o)))
        return self.final_path(start, goal, closed_nodes)

    def final_path(self, start, goal, closed_nodes):
        y_list = []
        x_list = []
        current = goal
        while current.parent != None:
            y_list.append(current.y)
            x_list.append(current.x)
            current = current.parent
        return x_list, y_list

    @staticmethod
    def heuristic(start, finish):
        return math.hypot(finish.x-start.x, finish.y-start.y)

    @staticmethod
    def motion_model():
        # orientation, do, dx, dy, cost
        # VVVVVVVVVVV
        # 0: 0 degree x_axis +ve
        # 1: 90 degreee y_axis +ve
        # 2: 180 degree x_axis -ve
        # 3: 270 degree y_axis -ve
        #                   o   do      dx      dy      cost
        motion = np.array([[0,   0,      10,     0,     10],    # 10 steps along the +ve x_axis
                           [0,   -1,     10,     10,    20],# 10 steps along the +ve x_axis then a left turn and another 10 steps along +ve y_axis
                           [0,   1,      10,     -10,   20],# 10 steps along the +ve x_axis then a right turn and another 10 steps along -ve y_axis
                           [1,   0,      0,      10,    10],# 10 steps along the +ve y_axis
                           [1,   -1,     -10,    10,    20],# 10 steps along the +ve y_axis then a left turn and another 10 steps along -ve x_axis
                           [1,   1,      10,     10,    20],# 10 steps along the +ve y_axis then a right turn and another 10 steps along +ve x_axis
                           [2,   0,      -10,    0,     10],# 10 steps along the -ve x_axis
                           [2,   -1,     -10,    -10,   20],# 10 steps along the +ve x_axis then a left turn and another 10 steps along -ve y_axis
                           [2,   1,      -10,    10,    20],# 10 steps along the +ve x_axis then a right turn and another 10 steps along +ve y_axis
                           [3,   0,      0,      -10,   10],# 10 steps along the -ve y_axis
                           [3,   -1,     10,     -10,   20],# 10 steps along the -ve y_axis then a left turn and another 10 steps along +ve x_axis
                           [3,   1,      -10,    -10,   20]])   # 10 steps along the -ve y_axis then a right turn and another 10 steps along -ve x_axis

        return motion


if __name__ == '__main__':
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

    A_Star = AStarAlgorithm(obstacle_map=obstacle_map)
    x, y = A_Star.search(50, 50, 0, 950, 950, 1)
    plt.plot(x, y, c='g')
    plt.show()
