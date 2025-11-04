"""
A* Algorithm Implementation
With heuristic-guided pathfinding and visualization support
"""

import heapq
import time

class AStarVisualizer:
    """
    A* Algorithm with visualization capabilities
    Uses Manhattan distance heuristic for grid-based pathfinding
    """

    def __init__(self, grid, start, end):
        """
        Initialize A* algorithm

        Args:
            grid: 2D list where 0=empty, 1=obstacle, 2=start, 3=end
            start: (row, col) tuple for start position
            end: (row, col) tuple for end position
        """
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

        # Algorithm state
        self.visited = set()
        self.parent = {}
        self.g_score = {start: 0}  # Cost from start to node
        self.f_score = {start: self.heuristic(start)}  # g + h
        self.pq = [(self.f_score[start], start)]  # Priority queue: (f_score, position)
        self.current = None
        self.found_path = False

        # Statistics
        self.nodes_explored = 0
        self.start_time = time.time()
        self.end_time = None

    def heuristic(self, pos):
        """
        Manhattan distance heuristic (admissible for grid-based pathfinding)

        Args:
            pos: (row, col) tuple

        Returns:
            Estimated distance to goal
        """
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])

    def get_neighbors(self, pos):
        """
        Get valid neighboring cells (4-directional)

        Args:
            pos: (row, col) tuple

        Returns:
            List of valid neighbor positions
        """
        row, col = pos
        neighbors = []

        # 4-directional movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                # Check if not obstacle
                if self.grid[new_row][new_col] != 1:
                    neighbors.append((new_row, new_col))

        return neighbors

    def step(self):
        """
        Execute one step of A* algorithm

        Returns:
            True if algorithm should continue, False if complete
        """
        # Check if priority queue is empty
        if not self.pq:
            self.end_time = time.time()
            return False

        # Get node with minimum f_score
        f, current = heapq.heappop(self.pq)

        # Skip if already visited
        if current in self.visited:
            return True

        # Mark as visited
        self.visited.add(current)
        self.current = current
        self.nodes_explored += 1

        # Check if reached goal
        if current == self.end:
            self.found_path = True
            self.end_time = time.time()
            return False

        # Explore neighbors
        current_g = self.g_score[current]

        for neighbor in self.get_neighbors(current):
            if neighbor in self.visited:
                continue

            # Calculate new g_score (uniform cost of 1 per move)
            tentative_g = current_g + 1

            # Update if shorter path found
            if neighbor not in self.g_score or tentative_g < self.g_score[neighbor]:
                self.g_score[neighbor] = tentative_g
                f_score = tentative_g + self.heuristic(neighbor)
                self.f_score[neighbor] = f_score
                self.parent[neighbor] = current
                heapq.heappush(self.pq, (f_score, neighbor))

        return True

    def get_visited(self):
        """Get set of all visited cells"""
        return self.visited.copy()

    def get_path(self):
        """
        Reconstruct path from start to end

        Returns:
            List of positions forming the path, or empty list if no path
        """
        if not self.found_path:
            return []

        path = []
        current = self.end

        while current in self.parent:
            path.append(current)
            current = self.parent[current]

        path.append(self.start)
        path.reverse()

        return path

    def get_stats(self):
        """
        Get algorithm performance statistics

        Returns:
            Dictionary with performance metrics
        """
        path = self.get_path()
        time_ms = (self.end_time - self.start_time) * 1000 if self.end_time else 0

        return {
            'nodes_explored': self.nodes_explored,
            'path_length': len(path) if path else 0,
            'time_ms': time_ms,
            'found_path': self.found_path
        }
