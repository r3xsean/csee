"""
Run Full Test Suite
Executes 30,000+ pathfinding algorithm tests for Extended Essay research
"""

import sys
from src.utils.batch_tester import BatchTester

def progress_callback(completed, total):
    """Print progress updates"""
    percent = (completed / total) * 100
    print(f"\rProgress: {completed}/{total} tests ({percent:.1f}%)", end='', flush=True)

    # Print newline every 100 tests
    if completed % 100 == 0:
        print()

def main():
    print("=" * 80)
    print("FULL TEST SUITE - Pathfinding Algorithm Comparison")
    print("=" * 80)
    print()
    print("Configuration:")
    print("  - Map sizes: 50x50, 100x100, 200x200, 400x400, 800x800")
    print("  - Obstacle densities: 10%, 25%, 40%, 55%, 70%")
    print("  - Map types: Random, Clustered, Maze, Mixed")
    print("  - Trials per configuration: 100")
    print("  - Total tests: 30,000")
    print("  - Estimated time: 1-2 hours")
    print()
    print("=" * 80)
    print()

    # Confirm with user
    response = input("Start full test suite? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("Test cancelled.")
        return

    print()
    print("Starting test suite...")
    print()

    # Create tester
    tester = BatchTester()

    try:
        # Run full test
        results_file = tester.run_full_test(progress_callback=progress_callback)

        print()
        print()
        print("=" * 80)
        print("TEST COMPLETE!")
        print("=" * 80)
        print(f"Results saved to: {results_file}")
        print()
        print("Next steps:")
        print("  1. Run statistical analysis:")
        print(f"     python -m src.analysis.statistical_analysis {results_file}")
        print()
        print("  2. Generate graphs:")
        print(f"     python -m src.analysis.graph_generator {results_file}")
        print()

    except KeyboardInterrupt:
        print()
        print()
        print("Test interrupted by user.")
        print("Partial results may have been saved.")
        sys.exit(1)
    except Exception as e:
        print()
        print()
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
