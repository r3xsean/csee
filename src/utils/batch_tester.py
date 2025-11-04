"""
Batch Testing Framework
Runs large-scale algorithm comparisons
"""

import os
import csv
import time
from datetime import datetime
from algorithms.dijkstra import DijkstraVisualizer
from algorithms.astar import AStarVisualizer
from algorithms.greedy import GreedyVisualizer
from utils.map_generator import MapGenerator

class BatchTester:
    """Runs batch tests and collects performance data"""

    def __init__(self, output_dir="data/results"):
        """
        Initialize batch tester

        Args:
            output_dir: Directory to save results
        """
        self.output_dir = output_dir
        self.algorithms = {
            'Dijkstra': DijkstraVisualizer,
            'A*': AStarVisualizer,
            'Greedy': GreedyVisualizer
        }

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def run_single_test(self, algorithm_name, grid, start, end):
        """
        Run a single test

        Args:
            algorithm_name: Name of algorithm
            grid: Map grid
            start: Start position
            end: End position

        Returns:
            Dictionary with test results
        """
        algo_class = self.algorithms[algorithm_name]
        visualizer = algo_class(grid, start, end)

        # Run algorithm to completion
        while visualizer.step():
            pass

        stats = visualizer.get_stats()

        return {
            'algorithm': algorithm_name,
            'nodes_explored': stats['nodes_explored'],
            'path_length': stats['path_length'],
            'time_ms': stats['time_ms'],
            'found_path': stats['found_path']
        }

    def run_test_suite(self, map_sizes=[50, 100, 200],
                       obstacle_densities=[0.1, 0.25, 0.4, 0.55, 0.7],
                       map_types=['random', 'clustered', 'maze', 'mixed'],
                       trials_per_config=100,
                       progress_callback=None):
        """
        Run comprehensive test suite

        Args:
            map_sizes: List of grid sizes to test
            obstacle_densities: List of obstacle densities
            map_types: List of map types
            trials_per_config: Number of trials per configuration
            progress_callback: Optional callback for progress updates

        Returns:
            Path to results file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = os.path.join(self.output_dir, f"batch_results_{timestamp}.csv")

        # Create CSV file
        with open(results_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'trial', 'map_size', 'obstacle_density', 'map_type',
                'algorithm', 'nodes_explored', 'path_length', 'time_ms',
                'found_path', 'seed'
            ])
            writer.writeheader()

            total_tests = (len(map_sizes) * len(obstacle_densities) *
                          len(map_types) * trials_per_config * len(self.algorithms))
            completed_tests = 0

            # Run tests
            for map_size in map_sizes:
                for density in obstacle_densities:
                    for map_type in map_types:
                        for trial in range(trials_per_config):
                            # Generate unique seed
                            seed = trial + int(time.time() * 1000) % 100000

                            # Generate map
                            if map_type == 'random':
                                grid = MapGenerator.generate_random_map(map_size, density, seed)
                            elif map_type == 'clustered':
                                grid = MapGenerator.generate_clustered_map(map_size, density, seed)
                            elif map_type == 'maze':
                                grid = MapGenerator.generate_maze_map(map_size, density, seed)
                            elif map_type == 'mixed':
                                grid = MapGenerator.generate_mixed_map(map_size, density, seed)

                            # Get start and end positions
                            start, end = MapGenerator.get_valid_start_end(grid, map_size)

                            if start is None or end is None:
                                continue

                            # Mark start and end in grid
                            grid[start[0]][start[1]] = 2
                            grid[end[0]][end[1]] = 3

                            # Test each algorithm
                            for algo_name in self.algorithms.keys():
                                result = self.run_single_test(algo_name, grid, start, end)

                                # Write result
                                writer.writerow({
                                    'trial': trial,
                                    'map_size': map_size,
                                    'obstacle_density': density,
                                    'map_type': map_type,
                                    'algorithm': algo_name,
                                    'nodes_explored': result['nodes_explored'],
                                    'path_length': result['path_length'],
                                    'time_ms': result['time_ms'],
                                    'found_path': result['found_path'],
                                    'seed': seed
                                })

                                completed_tests += 1

                                # Progress callback
                                if progress_callback:
                                    progress_callback(completed_tests, total_tests)

        return results_file

    def run_quick_test(self, num_trials=10, progress_callback=None):
        """
        Run a quick test for demonstration

        Args:
            num_trials: Number of trials
            progress_callback: Progress callback

        Returns:
            Path to results file
        """
        return self.run_test_suite(
            map_sizes=[50, 100],
            obstacle_densities=[0.1, 0.25, 0.4],
            map_types=['random', 'clustered'],
            trials_per_config=num_trials,
            progress_callback=progress_callback
        )

    def run_full_test(self, progress_callback=None):
        """
        Run full test suite (30,000+ trials)

        Args:
            progress_callback: Progress callback

        Returns:
            Path to results file
        """
        return self.run_test_suite(
            map_sizes=[50, 100, 200, 400, 800],
            obstacle_densities=[0.1, 0.25, 0.4, 0.55, 0.7],
            map_types=['random', 'clustered', 'maze', 'mixed'],
            trials_per_config=100,
            progress_callback=progress_callback
        )
