"""
Bidirectional Search Algorithm Implementation
Searches from both start and goal simultaneously
"""

import heapq
import time

class BidirectionalVisualizer:
    """
    Bidirectional Search Algorithm with visualization
    Searches from both start and end, meeting in the middle
    """

    def __init__(self, grid, start, end):
        """
        Initialize Bidirectional Search

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

        # Forward search (from start)
        self.forward_visited = set()
        self.forward_parent = {}
        self.forward_distance = {start: 0}
        self.forward_pq = [(0, start)]

        # Backward search (from end)
        self.backward_visited = set()
        self.backward_parent = {}
        self.backward_distance = {end: 0}
        self.backward_pq = [(0, end)]

        # Meeting point
        self.meeting_point = None
        self.found_path = False

        # Statistics
        self.nodes_explored = 0
        self.start_time = time.time()
        self.end_time = None

        # For visualization - combine both visited sets
        self.current_forward = None
        self.current_backward = None

        # Alternate direction flag (True = forward, False = backward)
        self.do_forward = True

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

        # 4-directional movement
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.grid[new_row][new_col] != 1:
                    neighbors.append((new_row, new_col))

        return neighbors

    def step(self):
        """
        Execute one step of bidirectional search
        Alternates between forward and backward search

        Returns:
            True if algorithm should continue, False if complete
        """
        # Check if both queues are empty
        if not self.forward_pq and not self.backward_pq:
            self.end_time = time.time()
            return False

        # Execute ONE direction per step (alternating)
        # This ensures animation properly represents computational work
        if self.do_forward:
            # Do forward step
            if self.forward_pq:
                if self._step_forward():
                    return False
                self.do_forward = False  # Only toggle if we did work
            elif self.backward_pq:
                # Forward queue empty, do backward instead
                self.do_forward = False
        else:
            # Do backward step
            if self.backward_pq:
                if self._step_backward():
                    return False
                self.do_forward = True  # Only toggle if we did work
            elif self.forward_pq:
                # Backward queue empty, do forward instead
                self.do_forward = True

        return True

    def _step_forward(self):
        """
        Execute one forward step (from start toward end)

        Returns:
            True if path found, False otherwise
        """
        if not self.forward_pq:
            return False

        dist, current = heapq.heappop(self.forward_pq)

        if current in self.forward_visited:
            return False

        self.forward_visited.add(current)
        self.current_forward = current
        self.nodes_explored += 1

        # Check if we've met the backward search
        if current in self.backward_visited:
            self.meeting_point = current
            self.found_path = True
            self.end_time = time.time()
            return True

        # Explore neighbors
        for neighbor in self.get_neighbors(current):
            if neighbor in self.forward_visited:
                continue

            new_distance = self.forward_distance[current] + 1

            if neighbor not in self.forward_distance or new_distance < self.forward_distance[neighbor]:
                self.forward_distance[neighbor] = new_distance
                self.forward_parent[neighbor] = current
                heapq.heappush(self.forward_pq, (new_distance, neighbor))

        return False

    def _step_backward(self):
        """
        Execute one backward step (from end toward start)

        Returns:
            True if path found, False otherwise
        """
        if not self.backward_pq:
            return False

        dist, current = heapq.heappop(self.backward_pq)

        if current in self.backward_visited:
            return False

        self.backward_visited.add(current)
        self.current_backward = current
        self.nodes_explored += 1

        # Check if we've met the forward search
        if current in self.forward_visited:
            self.meeting_point = current
            self.found_path = True
            self.end_time = time.time()
            return True

        # Explore neighbors
        for neighbor in self.get_neighbors(current):
            if neighbor in self.backward_visited:
                continue

            new_distance = self.backward_distance[current] + 1

            if neighbor not in self.backward_distance or new_distance < self.backward_distance[neighbor]:
                self.backward_distance[neighbor] = new_distance
                self.backward_parent[neighbor] = current
                heapq.heappush(self.backward_pq, (new_distance, neighbor))

        return False

    def get_visited(self):
        """Get set of all visited cells from both searches"""
        return self.forward_visited.union(self.backward_visited)

    def get_path(self):
        """
        Reconstruct path from start to end through meeting point

        Returns:
            List of positions forming the path, or empty list if no path
        """
        if not self.found_path or self.meeting_point is None:
            return []

        # Build path from start to meeting point
        forward_path = []
        current = self.meeting_point
        while current in self.forward_parent:
            forward_path.append(current)
            current = self.forward_parent[current]
        forward_path.append(self.start)
        forward_path.reverse()

        # Build path from meeting point to end
        backward_path = []
        current = self.meeting_point
        while current in self.backward_parent:
            backward_path.append(self.backward_parent[current])
            current = self.backward_parent[current]

        # Combine paths (meeting point appears once - in forward_path)
        return forward_path + backward_path

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
