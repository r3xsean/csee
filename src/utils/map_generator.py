"""
Map Generator
Creates different types of maps for testing
"""

import random
import json

class MapGenerator:
    """Generates various map configurations for testing"""

    @staticmethod
    def generate_random_map(size, density, seed=None):
        """
        Generate random obstacle map

        Args:
            size: Grid size (size x size)
            density: Obstacle density (0.0 to 1.0)
            seed: Random seed for reproducibility

        Returns:
            2D list representing the map
        """
        if seed is not None:
            random.seed(seed)

        grid = [[0 for _ in range(size)] for _ in range(size)]

        # Place obstacles randomly
        for i in range(size):
            for j in range(size):
                if random.random() < density:
                    grid[i][j] = 1

        return grid

    @staticmethod
    def generate_clustered_map(size, density, seed=None):
        """
        Generate map with clustered obstacles

        Args:
            size: Grid size
            density: Obstacle density
            seed: Random seed

        Returns:
            2D list with clustered obstacles
        """
        if seed is not None:
            random.seed(seed)

        grid = [[0 for _ in range(size)] for _ in range(size)]

        # Create clusters
        num_clusters = int(size * size * density / 10)

        for _ in range(num_clusters):
            # Random cluster center
            center_row = random.randint(0, size - 1)
            center_col = random.randint(0, size - 1)

            # Random cluster size
            cluster_size = random.randint(3, 8)

            # Fill cluster
            for i in range(center_row - cluster_size, center_row + cluster_size):
                for j in range(center_col - cluster_size, center_col + cluster_size):
                    if 0 <= i < size and 0 <= j < size:
                        if random.random() < 0.7:  # 70% fill within cluster
                            grid[i][j] = 1

        return grid

    @staticmethod
    def generate_maze_map(size, density, seed=None):
        """
        Generate maze-like map with corridors

        Args:
            size: Grid size
            density: Wall density
            seed: Random seed

        Returns:
            2D list with maze pattern
        """
        if seed is not None:
            random.seed(seed)

        grid = [[1 for _ in range(size)] for _ in range(size)]

        # Create corridors using recursive division
        def divide(x1, y1, x2, y2):
            if x2 - x1 < 3 or y2 - y1 < 3:
                return

            # Create horizontal or vertical wall with gap
            if random.random() < 0.5:
                # Horizontal wall
                wall_row = random.randint(y1 + 1, y2 - 1)
                gap_col = random.randint(x1, x2)

                for col in range(x1, x2 + 1):
                    if col != gap_col:
                        grid[wall_row][col] = 1
                    else:
                        grid[wall_row][col] = 0

                divide(x1, y1, x2, wall_row - 1)
                divide(x1, wall_row + 1, x2, y2)
            else:
                # Vertical wall
                wall_col = random.randint(x1 + 1, x2 - 1)
                gap_row = random.randint(y1, y2)

                for row in range(y1, y2 + 1):
                    if row != gap_row:
                        grid[row][wall_col] = 1
                    else:
                        grid[row][wall_col] = 0

                divide(x1, y1, wall_col - 1, y2)
                divide(wall_col + 1, y1, x2, y2)

        # Clear initial grid
        for i in range(size):
            for j in range(size):
                grid[i][j] = 0

        # Create maze
        divide(0, 0, size - 1, size - 1)

        return grid

    @staticmethod
    def generate_mixed_map(size, density, seed=None):
        """
        Generate map with mixed obstacle patterns

        Args:
            size: Grid size
            density: Obstacle density
            seed: Random seed

        Returns:
            2D list with mixed patterns
        """
        if seed is not None:
            random.seed(seed)

        # Combine random and clustered
        grid1 = MapGenerator.generate_random_map(size, density / 2, seed)
        grid2 = MapGenerator.generate_clustered_map(size, density / 2, seed + 1 if seed else None)

        # Merge grids
        grid = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if grid1[i][j] == 1 or grid2[i][j] == 1:
                    grid[i][j] = 1

        return grid

    @staticmethod
    def save_map(grid, filename):
        """Save map to JSON file"""
        with open(filename, 'w') as f:
            json.dump(grid, f)

    @staticmethod
    def load_map(filename):
        """Load map from JSON file"""
        with open(filename, 'r') as f:
            return json.load(f)

    @staticmethod
    def get_valid_start_end(grid, size):
        """
        Find valid start and end positions in grid

        Returns:
            Tuple of (start_pos, end_pos)
        """
        # Try corners first
        corners = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]

        valid_corners = [c for c in corners if grid[c[0]][c[1]] != 1]

        if len(valid_corners) >= 2:
            return valid_corners[0], valid_corners[-1]

        # Find any two valid positions
        valid_positions = []
        for i in range(size):
            for j in range(size):
                if grid[i][j] != 1:
                    valid_positions.append((i, j))

        if len(valid_positions) >= 2:
            return valid_positions[0], valid_positions[-1]

        # No valid path possible
        return None, None
