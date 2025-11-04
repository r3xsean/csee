# Pathfinding Algorithm Comparison - IB CS Extended Essay

## Quick Start

**One command to launch everything:**

```bash
python app.py
```

This opens a single unified application with three tabs:

1. **Single Algorithm View** - Test individual algorithms (Dijkstra, A*, Bidirectional)
2. **Triple Comparison View** - Watch all three algorithms run side-by-side simultaneously
3. **Batch Testing & Analysis** - Run large-scale tests and generate statistics/graphs

## Features

### Tab 1: Single Algorithm View
- Select algorithm: Dijkstra, A*, or Bidirectional Search
- Drag-and-drop start/end points
- Adjust obstacle density (0-70%)
- Real-time visualization with color-coded cells
- Live statistics (nodes explored, path length, execution time)

### Tab 2: Triple Comparison View
- Side-by-side visualization of all three algorithms
- Synchronized grid (same obstacles for fair comparison)
- Independent algorithm finishing - each shows results immediately
- Drag-and-drop works across all views
- Visual demonstration of algorithmic differences

### Tab 3: Batch Testing & Analysis
- **Quick Test**: 360 trials in ~5 minutes
- **Medium Test**: 3,000 trials in ~30 minutes
- **Full Test**: 30,000+ trials in 1-2 hours
- Automated statistical analysis (ANOVA, effect sizes, confidence intervals)
- Publication-quality graph generation (8 graphs at 300 DPI)
- Results saved to `data/results/` directory

## Installation

```bash
# Install dependencies
pip install matplotlib seaborn scipy pandas numpy

# Run application
python app.py
```

## Testing

Verify all algorithms work correctly:

```bash
python test_algorithms.py
```

Expected output:
```
✓✓✓ ALL TESTS PASSED ✓✓✓
All three algorithms are working correctly!
```

## Project Structure

```
csee/
├── app.py                       # ONE unified application (run this!)
├── test_algorithms.py           # Algorithm verification tests
├── requirements.txt             # Python dependencies
├── README.md                    # This file
│
├── src/                         # Core implementation
│   ├── algorithms/              # Three pathfinding algorithms
│   │   ├── dijkstra.py         # Dijkstra's Algorithm
│   │   ├── astar.py            # A* with Manhattan heuristic
│   │   └── bidirectional.py   # Bidirectional Search
│   │
│   ├── utils/                   # Testing and utilities
│   │   ├── batch_tester.py     # Automated testing framework
│   │   └── map_generator.py   # Map generation utilities
│   │
│   └── analysis/                # Statistical analysis
│       ├── statistical_analysis.py  # ANOVA, effect sizes
│       └── graph_generator.py      # Publication graphs
│
├── data/                        # Generated data
│   ├── results/                # CSV files from batch tests
│   └── analysis/               # Statistical reports
│
└── graphs/                      # Generated visualizations
```

## Algorithms Implemented

### 1. Dijkstra's Algorithm
- **Approach**: Uniform-cost exploration from start
- **Complexity**: O((V+E) log V) with binary heap
- **Role**: Baseline comparison
- **Optimality**: Guarantees optimal paths

### 2. A* Algorithm
- **Approach**: Heuristic-guided best-first search
- **Heuristic**: Manhattan distance (admissible)
- **Complexity**: Better than Dijkstra with good heuristic
- **Role**: Industry standard showing heuristic benefit

### 3. Bidirectional Search
- **Approach**: Searches from both start and end simultaneously
- **Optimization**: Meets in the middle for efficiency
- **Complexity**: Reduces effective search space
- **Role**: Modern approach showing dual-source optimization

All algorithms use **4-directional movement only** (up, down, left, right) for fair comparison.

## How to Use

### Interactive Visualization (Tabs 1 & 2)

1. **Launch**: `python app.py`
2. **Drag Points**: Click and drag green (start) or red (end) points
3. **Adjust Density**: Use slider to change obstacle density
4. **Run Algorithm**: Click "Run Algorithm" or "Run All Algorithms"
5. **Watch**: Algorithms explore the grid in real-time
   - Light blue = explored cells
   - Gold = final path
   - Dark gray = obstacles

### Batch Testing (Tab 3)

1. **Choose Test Size**:
   - Quick: Small-scale validation
   - Medium: Moderate data collection
   - Full: Complete research dataset (30,000+ trials)

2. **Monitor Progress**: Progress bar and log show real-time status

3. **Analyze Results**: Click "Analyze Results" for statistical report

4. **Generate Graphs**: Click "Generate Graphs" for visualizations

## Data Collection

Batch tests generate CSV files with columns:
- `algorithm`: Dijkstra, A*, or Bidirectional
- `map_size`: Grid dimensions (50×50 to 800×800)
- `obstacle_density`: 10%, 25%, 40%, 55%, or 70%
- `map_type`: random, clustered, maze, or mixed
- `trial_number`: Test repetition number
- `time_ms`: Execution time in milliseconds
- `nodes_explored`: Search space explored
- `path_length`: Solution path length
- `found_path`: Success indicator

## Statistical Analysis

The analysis module computes:

1. **Descriptive Statistics**: Mean, median, std dev, min/max
2. **ANOVA Testing**: F-statistic and p-values
3. **Effect Sizes**: Eta-squared (η²) and Cohen's d
4. **Post-hoc Tests**: Pairwise comparisons with Bonferroni correction
5. **Confidence Intervals**: 95% CI on all means
6. **Scaling Analysis**: Algorithm performance vs. map size

## Graph Generation

Eight publication-quality graphs at 300 DPI:
1. Execution time comparison (box plots)
2. Nodes explored comparison
3. Obstacle density impact on time
4. Obstacle density impact on nodes
5. Map size scaling analysis
6. Pairwise performance differences
7. Cumulative distribution functions
8. Heatmap of median execution times

## Legend

**Grid Colors:**
- 🟩 Green = Start position (draggable)
- 🟥 Red = End position (draggable)
- ⬛ Dark Gray = Obstacle
- 🔵 Light Blue = Explored cell
- 🟨 Gold = Final path

## Requirements

- Python 3.8+
- tkinter (built-in)
- matplotlib
- seaborn
- scipy
- pandas
- numpy

## IB Extended Essay Integration

This application supports the complete research workflow:

1. **Algorithm Implementation**: Three production-quality pathfinding algorithms
2. **Empirical Testing**: 30,000+ controlled trials
3. **Statistical Validation**: ANOVA, effect sizes, confidence intervals
4. **Visualization**: Real-time demonstration and publication graphs
5. **Data Export**: CSV format for analysis and reporting

## Research Question

"To what extent do the pathfinding algorithms Dijkstra's Algorithm, A* (A-star), and Bidirectional Search differ in computational efficiency and path optimality when navigating 2D grid-based maps with varying obstacle densities?"

---

**Date**: 2025-11-04
**Status**: Complete Application - All Features Integrated
