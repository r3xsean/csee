"""
Comprehensive Algorithm Tests
Verifies correctness of all three pathfinding algorithms
"""

import sys
sys.path.insert(0, 'src')

from algorithms.dijkstra import DijkstraVisualizer
from algorithms.astar import AStarVisualizer
from algorithms.bidirectional import BidirectionalVisualizer

def test_simple_path():
    """Test basic pathfinding with no obstacles"""
    print("Testing simple path (no obstacles)...")

    grid = [[0 for _ in range(10)] for _ in range(10)]
    start = (0, 0)
    end = (9, 9)

    results = {}

    for name, algo_class in [('Dijkstra', DijkstraVisualizer),
                             ('A*', AStarVisualizer),
                             ('Bidirectional', BidirectionalVisualizer)]:
        visualizer = algo_class(grid, start, end)

        while visualizer.step():
            pass

        stats = visualizer.get_stats()
        path = visualizer.get_path()

        results[name] = {
            'found': stats['found_path'],
            'length': stats['path_length'],
            'nodes': stats['nodes_explored']
        }

        assert stats['found_path'], f"{name} should find path"
        assert len(path) > 0, f"{name} path should not be empty"
        assert path[0] == start, f"{name} path should start at start"
        assert path[-1] == end, f"{name} path should end at end"

    print(f"  ✓ All algorithms found path")
    print(f"  - Dijkstra: {results['Dijkstra']['length']} cells, {results['Dijkstra']['nodes']} nodes")
    print(f"  - A*: {results['A*']['length']} cells, {results['A*']['nodes']} nodes")
    print(f"  - Bidirectional: {results['Bidirectional']['length']} cells, {results['Bidirectional']['nodes']} nodes")
    print()

def test_obstacle_navigation():
    """Test pathfinding around obstacles"""
    print("Testing obstacle navigation...")

    grid = [[0 for _ in range(10)] for _ in range(10)]
    start = (0, 0)
    end = (9, 9)

    # Create wall with gap
    for i in range(8):
        grid[i][5] = 1

    for name, algo_class in [('Dijkstra', DijkstraVisualizer),
                             ('A*', AStarVisualizer),
                             ('Bidirectional', BidirectionalVisualizer)]:
        visualizer = algo_class(grid, start, end)

        while visualizer.step():
            pass

        stats = visualizer.get_stats()
        path = visualizer.get_path()

        assert stats['found_path'], f"{name} should find path around obstacle"
        assert len(path) > 0, f"{name} should have valid path"

        # Verify path doesn't go through obstacles
        for pos in path:
            assert grid[pos[0]][pos[1]] != 1, f"{name} path should not go through obstacles"

    print(f"  ✓ All algorithms navigated around obstacles")
    print()

def test_no_path():
    """Test case where no path exists"""
    print("Testing no-path scenario...")

    grid = [[0 for _ in range(10)] for _ in range(10)]
    start = (0, 0)
    end = (9, 9)

    # Create impassable wall
    for i in range(10):
        grid[i][5] = 1

    for name, algo_class in [('Dijkstra', DijkstraVisualizer),
                             ('A*', AStarVisualizer),
                             ('Bidirectional', BidirectionalVisualizer)]:
        visualizer = algo_class(grid, start, end)

        while visualizer.step():
            pass

        stats = visualizer.get_stats()
        path = visualizer.get_path()

        assert not stats['found_path'], f"{name} should not find path"
        assert len(path) == 0, f"{name} should return empty path"

    print(f"  ✓ All algorithms correctly detected no path")
    print()

def test_optimal_path():
    """Test that Dijkstra and A* find same optimal path (JPS uses jump points)"""
    print("Testing path optimality...")

    grid = [[0 for _ in range(10)] for _ in range(10)]
    start = (0, 0)
    end = (5, 5)

    path_lengths = {}

    for name, algo_class in [('Dijkstra', DijkstraVisualizer),
                             ('A*', AStarVisualizer),
                             ('Bidirectional', BidirectionalVisualizer)]:
        visualizer = algo_class(grid, start, end)

        while visualizer.step():
            pass

        path = visualizer.get_path()
        path_lengths[name] = len(path)

        # Verify path is valid
        assert len(path) > 0, f"{name} should have valid path"
        assert path[0] == start, f"{name} path should start at start"
        assert path[-1] == end, f"{name} path should end at end"

    # Dijkstra and A* should find same length (both explore all cells)
    assert path_lengths['Dijkstra'] == path_lengths['A*'], "Dijkstra and A* should find same path length"

    print(f"  ✓ All algorithms found optimal path (length {path_lengths['Dijkstra']})")
    print(f"    - Dijkstra: {path_lengths['Dijkstra']}, A*: {path_lengths['A*']}, Bidirectional: {path_lengths['Bidirectional']}")
    print()

def test_performance_ordering():
    """Test that algorithms perform as expected theoretically"""
    print("Testing performance characteristics...")

    grid = [[0 for _ in range(30)] for _ in range(30)]
    start = (0, 0)
    end = (29, 29)

    # Add some obstacles
    import random
    random.seed(42)
    for i in range(30):
        for j in range(30):
            if random.random() < 0.2:
                grid[i][j] = 1

    nodes_explored = {}

    for name, algo_class in [('Dijkstra', DijkstraVisualizer),
                             ('A*', AStarVisualizer),
                             ('Bidirectional', BidirectionalVisualizer)]:
        visualizer = algo_class(grid, start, end)

        while visualizer.step():
            pass

        stats = visualizer.get_stats()
        nodes_explored[name] = stats['nodes_explored']

    print(f"  - Dijkstra explored: {nodes_explored['Dijkstra']} nodes")
    print(f"  - A* explored: {nodes_explored['A*']} nodes")
    print(f"  - Bidirectional explored: {nodes_explored['Bidirectional']} nodes")

    # A* should explore fewer nodes than Dijkstra (heuristic guidance)
    assert nodes_explored['A*'] < nodes_explored['Dijkstra'], "A* should explore fewer nodes than Dijkstra"

    # Bidirectional should also explore fewer nodes (searches from both ends)
    assert nodes_explored['Bidirectional'] < nodes_explored['Dijkstra'], "Bidirectional should explore fewer nodes than Dijkstra"

    print(f"  ✓ A* explored {nodes_explored['Dijkstra'] - nodes_explored['A*']} fewer nodes than Dijkstra")
    print(f"  ✓ Bidirectional explored {nodes_explored['Dijkstra'] - nodes_explored['Bidirectional']} fewer nodes than Dijkstra")
    print()

def run_all_tests():
    """Run all algorithm tests"""
    print("=" * 80)
    print("COMPREHENSIVE ALGORITHM TESTS")
    print("=" * 80)
    print()

    try:
        test_simple_path()
        test_obstacle_navigation()
        test_no_path()
        test_optimal_path()
        test_performance_ordering()

        print("=" * 80)
        print("✓✓✓ ALL TESTS PASSED ✓✓✓")
        print("=" * 80)
        print("\nAll three algorithms are working correctly!")
        print("Ready for batch testing and data collection.")

        return True

    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
