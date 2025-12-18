# Solving Classic AI Problems with Search Algorithms

## Project Title

Robot Pathfinding in a Grid with Obstacles

## Course

Introduction to Artificial Intelligence

## Project Description

This project implements and compares multiple classic AI search algorithms to solve a robot pathfinding problem in a two-dimensional grid environment with obstacles. The robot starts from a given position and must reach a target goal while avoiding blocked cells.

The goal of the project is to analyze the behavior, efficiency, and optimality of different uninformed, informed, and optimization-based search strategies.

---

## Problem Description

* Environment: 2D Grid
* Cell Types:

  * S : Start position
  * G : Goal position
  * 0 : Free cell
  * 1 : Obstacle
* Allowed Movements: Up, Down, Left, Right
* Cost per Move: 1

---

## Implemented Algorithms

### Uninformed Search

* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Uniform Cost Search (UCS)
* Iterative Deepening Search (IDS)

### Informed Search

* A* Search (Manhattan Distance Heuristic)
 

### Optimization Technique

* Genetic Algorithm

---

## Technologies Used

* Python 3
* Standard Libraries: collections, heapq, random

---

## How to Run the Project

1. Make sure Python 3 is installed on your machine.
2. Clone the repository or download the source files.
3. Navigate to the source code directory.
4. Run the following command:

```
python Main.py
```

The output will display the paths found by each search algorithm.

---

## Output

Each algorithm prints the path it finds from the start position to the goal (if a solution exists).

---

## Notes

* A* Search provides the best performance in terms of speed and optimality.
* DFS and Hill Climbing may fail to find optimal solutions.
* Genetic Algorithm is used as an optimization approach and does not guarantee optimality.

---

## Author

AI Project Team
