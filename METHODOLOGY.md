# Methodology & Experimental Design

## Methodological Overview

This EE employs a **comparative experimental methodology** combining qualitative analysis of algorithm design with quantitative empirical testing. The approach follows established research practices in computer science algorithm evaluation.

---

## Methodology Type

### Classification
**Empirical Comparative Study** with **Design & Implementation Component**

**Key Characteristics**:
- Quantitative data collection through algorithmic benchmarking
- Controlled experimental conditions ensuring fair comparison
- Statistical analysis validating findings
- Custom application development for precise measurement
- Reproducible methodology documented for validation

### Why This Methodology?

**Alignment with Research Question**:
- RQ asks "to what extent do algorithms differ" - requires quantitative comparison
- Comparative approach directly addresses multi-algorithm evaluation
- Empirical testing provides objective, measurable evidence
- Statistical analysis enables significance claims

**CS Discipline Best Practices**:
- Algorithm evaluation relies on empirical benchmarking
- Controlled experiments ensure fair comparison
- Multiple metrics prevent single-metric bias
- Statistical testing validates observed differences
- Reproducibility enables verification

**Practical Advantages**:
- Objective evidence immune to theoretical speculation
- Custom application provides precise measurement control
- Large dataset enables statistical validation
- Reproducible methodology allows peer verification

---

## Conceptual Framework

### Comparison Strategy

**Algorithm Selection Rationale**:

1. **Dijkstra's Algorithm (Baseline)**
   - Uniform-cost search without heuristics
   - Serves as performance reference point
   - Optimal but less efficient than heuristic approaches
   - Well-understood algorithm

2. **A* Algorithm (Heuristic Improvement)**
   - Adds heuristic guidance to Dijkstra
   - Demonstrates efficiency gains from domain knowledge
   - Industry-standard implementation
   - Direct comparison point with Dijkstra

3. **Jump Point Search (Geometric Optimization)**
   - Optimizes A* through geometric pruning
   - Represents modern optimization techniques
   - Tests if increased complexity yields proportional gains
   - Shows cutting-edge algorithm design

**Comparison Framework**:
- **Dijkstra → A***: Shows heuristic optimization impact
- **A* → JPS**: Shows geometric optimization impact
- **Dijkstra → JPS**: Shows cumulative improvement through design evolution

### Measurement Strategy

**Primary Metrics** (Direct Measurement):
1. **Execution Time** (milliseconds)
   - Wall-clock time from start to goal found
   - Primary efficiency indicator
   - Measured using high-resolution system timer
   - Averaged across 100 trials per condition

2. **Nodes Explored** (count)
   - Number of grid cells examined during search
   - Indicates search space size
   - Correlates with memory usage
   - Shows algorithm decision quality

3. **Path Length** (grid units)
   - Actual distance of found path
   - Optimality indicator
   - Should be identical for all three algorithms (all optimal)
   - Validates implementation correctness

**Secondary Metrics** (Calculated):
4. **Efficiency Ratio** = Nodes Explored / Time (nodes per millisecond)
5. **Optimality Ratio** = Found Path Length / Theoretical Optimal
6. **Algorithm Scaling** = Performance growth rate with map size

### Independent Variables

**Primary Variable: Obstacle Density**
- **Levels**: 10%, 25%, 40%, 55%, 70%
- **Rationale**: Tests algorithm performance across environmental complexity range
- **Implementation**: Percentage of grid cells randomly assigned as obstacles
- **Hypothesized Effect**:
  - Dijkstra's performance: Minimal change (explores uniformly)
  - A*'s performance: Improves with density (heuristic more effective with obstacles)
  - JPS's performance: Improves most with density (geometric pruning most effective)

**Secondary Variables** (For Extended Analysis):
- **Map Size**: 50×50, 100×100, 200×200, 400×400, 800×800
  - Tests algorithm scaling and complexity growth
  - Reveals how efficiency changes with problem size

- **Map Type**: Random, Clustered, Maze, Mixed
  - Tests algorithm adaptability to different environmental patterns
  - Random = uniform obstacle distribution
  - Clustered = grouped obstacles (more realistic)
  - Maze = narrow passages and complex corridors
  - Mixed = combination of patterns

### Control Variables

**Held Constant** (Ensuring Fair Comparison):

1. **Grid Implementation**
   - Uniform cell size
   - Standard 8-directional movement (including diagonals)
   - Uniform movement costs (no weighted grid)

2. **Start and Goal Positions**
   - Start: Top-left corner (0, 0)
   - Goal: Bottom-right corner (width-1, height-1)
   - Always in same relative positions
   - Ensures path length consistency

3. **Heuristic Function**
   - Manhattan distance for A* and JPS
   - Calculated as |dx| + |dy|
   - Admissible (never overestimates) ensuring optimality

4. **Obstacle Generation**
   - Pseudo-random generation with fixed seed
   - Same map used for all three algorithms
   - Ensures identical test conditions
   - Enables fair direct comparison

5. **Hardware Environment**
   - Single test machine (consistent hardware)
   - No background processes during testing
   - Identical software environment
   - Controlled room temperature (if thermal-sensitive)

6. **Implementation Details**
   - Same programming language (Python)
   - Consistent data structures (priority queues)
   - Identical compiler optimization settings
   - Standard library functions only

---

## Experimental Design

### Research Design Structure

**Factorial Design**:
- **Factor 1**: Algorithm (3 levels: Dijkstra, A*, JPS)
- **Factor 2**: Obstacle Density (5 levels: 10%, 25%, 40%, 55%, 70%)
- **Factor 3**: Map Size (5 levels: 50×50, 100×100, 200×200, 400×400, 800×800)
- **Replications**: 100 trials per condition

**Total Test Cases**:
```
3 algorithms × 5 densities × 5 sizes × 100 trials = 7,500 primary tests
3 algorithms × 5 densities × 4 types × 100 trials = 6,000 secondary tests
Total = 13,500 individual algorithm executions
```

### Experimental Procedure

**Pre-Experiment Setup**:
1. Install and configure application environment
2. Verify algorithm implementations (unit testing)
3. Calibrate performance measurement system
4. Prepare test maps and validation datasets
5. Document baseline performance

**Single Experiment Procedure**:
```
FOR each test configuration:
  FOR each of 100 trials:
    1. Generate random map with specified density
    2. Validate start/goal accessibility
    3. Run Algorithm A with timer
    4. Record: execution_time, nodes_explored, path_length
    5. Verify path optimality
    6. Store result to CSV
    7. Repeat for Algorithm B and C with identical map
```

**Data Collection**:
- Real-time: Display progress to prevent accidental termination
- Automatic: CSV export after each trial
- Checkpoint: Save partial results every 100 trials
- Backup: Duplicate copies of data files

**Quality Control**:
- Validity checks: Ensure path is reachable
- Sanity checks: Path length consistent with algorithm optimality
- Outlier detection: Flag unusual results for manual review
- Completeness: Verify no missing data points

### Timeline

**Week 1-2**: Small-scale pilot testing (100-500 trials)
- Validate methodology
- Test application stability
- Confirm data collection pipeline
- Adjust parameters if needed

**Week 3-6**: Large-scale data collection (7,500+ trials)
- Run primary factorial design
- Continuous monitoring and logging
- Intermediate analysis to catch errors
- Backup data regularly

**Week 7**: Extended analysis (6,000 additional trials)
- Test map types (Random, Clustered, Maze, Mixed)
- Additional density/size combinations
- Validate generalizability

**Week 8**: Data consolidation and analysis
- Combine all results
- Clean and validate data
- Statistical analysis
- Graph generation

---

## Algorithm Specifications

### Implementation Details

**Dijkstra's Algorithm**
```
Function dijkstra(grid, start, goal):
  distances ← all infinity except start = 0
  open_set ← priority queue with start
  came_from ← empty map

  While open_set not empty:
    current ← node in open_set with smallest distance
    If current == goal:
      return reconstruct_path(came_from, current)

    For each neighbor of current:
      tentative_distance ← distances[current] + cost(current, neighbor)
      If tentative_distance < distances[neighbor]:
        distances[neighbor] ← tentative_distance
        came_from[neighbor] ← current
        Add neighbor to open_set

  return null (no path found)
```

**Measurement Points**:
- Time: Start when algorithm begins, stop when path found
- Nodes Explored: Increment counter each time a node is examined
- Path Length: Calculate distance of reconstructed path

**A* Algorithm**
```
Function a_star(grid, start, goal):
  g_score ← all infinity except start = 0
  h_score ← heuristic distance to goal
  f_score ← g_score + h_score
  open_set ← priority queue with start
  came_from ← empty map

  While open_set not empty:
    current ← node in open_set with smallest f_score
    If current == goal:
      return reconstruct_path(came_from, current)

    For each neighbor of current:
      tentative_g ← g_score[current] + cost(current, neighbor)
      If tentative_g < g_score[neighbor]:
        came_from[neighbor] ← current
        g_score[neighbor] ← tentative_g
        f_score[neighbor] ← g_score[neighbor] + heuristic(neighbor, goal)
        Add/update neighbor in open_set

  return null (no path found)
```

**Heuristic Function**:
```
Function manhattan_distance(pos1, pos2):
  return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
```

**Measurement Points**:
- Same as Dijkstra (time, nodes, path)
- Note: Should be identical path length (both optimal)

**Jump Point Search**
```
Function jps(grid, start, goal):
  open_set ← priority queue with start
  came_from ← empty map

  While open_set not empty:
    current ← node in open_set with smallest f_score
    If current == goal:
      return reconstruct_path(came_from, current)

    For each direction D from current:
      jump_point ← jump(current, D, goal)
      If jump_point found:
        Add jump_point to open_set
        came_from[jump_point] ← current

  return null (no path found)

Function jump(current, direction, goal):
  next ← current + direction
  If next is obstacle or out_of_bounds:
    return null

  If next == goal:
    return next

  If forceful_neighbor(next, direction):
    return next

  If direction is diagonal:
    If jump(next, horizontal_component, goal) or jump(next, vertical_component, goal):
      return next

  return jump(next, direction, goal)
```

**Measurement Points**:
- Time: Includes jump point calculations
- Nodes Explored: Count jump point evaluations
- Path Length: Should be identical to other algorithms

### Implementation Validation

**Correctness Tests** (Unit Tests):
1. **Path Validity**: All paths must be traceable
2. **Optimality**: All algorithms find optimal paths
3. **Completeness**: All algorithms find path if one exists
4. **Edge Cases**:
   - Start equals goal
   - No path exists
   - Single cell map
   - Fully blocked map

**Performance Validation**:
1. **Sanity Checks**:
   - A* ≤ Dijkstra in execution time
   - JPS ≤ A* in execution time (on average)
   - Path lengths identical across algorithms
   - Node counts: A* ≤ Dijkstra, JPS ≤ A*

2. **Consistency Checks**:
   - Same algorithm on same map gives same results
   - Results reproducible across runs
   - No memory leaks or resource exhaustion

---

## Data Collection Methodology

### Performance Measurement

**Timing Measurement**:
```python
import time
start_time = time.perf_counter()
# Run algorithm
end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
```

**Rationale**:
- `perf_counter()`: High-resolution timer immune to system clock adjustments
- milliseconds: Standard unit for algorithm benchmarking
- Captures wall-clock time, including all computational cost

**Node Counting**:
```python
class Algorithm:
  def __init__(self):
    self.nodes_explored = 0

  def examine_node(self, node):
    self.nodes_explored += 1
    # Process node...
```

**Path Validation**:
```python
def validate_path(path, grid, start, goal):
  assert path[0] == start
  assert path[-1] == goal
  for i in range(len(path) - 1):
    assert is_adjacent(path[i], path[i+1])
    assert not is_obstacle(grid, path[i+1])
  return True
```

### Data Storage Format

**CSV Structure**:
```
algorithm,trial,map_size,obstacle_density,map_type,execution_time_ms,nodes_explored,path_length,success
dijkstra,1,100,0.40,random,45.234,2847,188.42,true
a_star,1,100,0.40,random,23.891,1245,188.42,true
jps,1,100,0.40,random,12.445,634,188.42,true
dijkstra,2,100,0.40,random,46.123,2912,189.15,true
...
```

**Fields**:
- **algorithm**: Which algorithm (dijkstra, a_star, jps)
- **trial**: Trial number (1-100)
- **map_size**: Grid dimensions (50-800)
- **obstacle_density**: Decimal 0.1-0.7
- **map_type**: Pattern type (random, clustered, maze, mixed)
- **execution_time_ms**: Time in milliseconds
- **nodes_explored**: Integer count
- **path_length**: Total distance in grid units
- **success**: Boolean (found path or not)

### Quality Assurance

**Data Validation Checks**:
1. No missing values (NaN or null)
2. Numeric fields within expected ranges
3. Consistency across same conditions
4. No duplicate records
5. Path properties consistent with algorithm

**Error Handling**:
- Log all errors with timestamp
- Skip invalid test and retry
- Document any failures
- Flag suspicious results for review

**Backup Strategy**:
- Save results every 100 trials
- Maintain backup copy on different drive
- Date-stamp all files with timestamp
- Version control data files

---

## Statistical Analysis Methodology

### Descriptive Statistics

**For Each Condition** (algorithm × density × size):

**Central Tendency**:
- Mean: Average performance across 100 trials
- Median: Resistant to outliers
- Mode: Most common value (if meaningful)

**Spread**:
- Standard Deviation: Variability measure
- Range: Min to max
- Interquartile Range (IQR): Middle 50%
- Coefficient of Variation: CV = SD/Mean (relative variability)

**Confidence Intervals**:
- 95% CI for mean performance
- Formula: Mean ± 1.96 × (SD/√n)
- Indicates range containing true population mean

### Inferential Statistics

**ANOVA (Analysis of Variance)**

**Purpose**: Test whether algorithm means differ significantly

**Hypotheses**:
- H₀ (Null): μ(Dijkstra) = μ(A*) = μ(JPS)
- H₁ (Alternative): At least one algorithm differs significantly

**Conditions**:
- **Primary Factor**: Algorithm (3 levels)
- **Blocking Factor**: Obstacle Density (5 levels)
- **Replicates**: 100 trials per combination

**Analysis**:
1. Compute F-statistic
2. Determine p-value
3. If p < 0.05: Reject null hypothesis (significant difference)
4. If p ≥ 0.05: Fail to reject null (no significant difference)

**Post-Hoc Testing** (if H₁ true):
- Tukey HSD test
- Pairwise comparisons: Dijkstra vs. A*, Dijkstra vs. JPS, A* vs. JPS
- Bonferroni correction for multiple comparisons
- Report confidence intervals for differences

**Effect Size**:
- η² (eta-squared): Proportion of variance explained by algorithm
- Range: 0 (no effect) to 1 (perfect prediction)
- Interpretation: >0.14 = large effect, >0.06 = medium, >0.01 = small

### Performance Scaling Analysis

**Method**: Log-log regression analysis

**Procedure**:
1. Plot log(execution_time) vs. log(map_size)
2. Calculate linear regression
3. Slope indicates scaling exponent

**Interpretation**:
- Slope 1: Linear scaling O(n)
- Slope 2: Quadratic scaling O(n²)
- Slope 1-2: Between linear and quadratic

**Comparison**:
- Compare slopes across algorithms
- Determine if JPS scaling differs significantly
- Extrapolate to larger map sizes (theoretical)

---

## Validity & Reliability

### Internal Validity

**Threats & Mitigation**:

1. **Confounding Variables**
   - Threat: Unmeasured factors affecting results
   - Mitigation: Strict control of test conditions
   - Control: Identical maps, hardware, settings

2. **Selection Bias**
   - Threat: Non-random test case selection
   - Mitigation: Random seed-based map generation
   - Control: Reproducible randomization

3. **History Effects**
   - Threat: System changes during experiment
   - Mitigation: Rapid data collection
   - Control: Complete tests within single week

4. **Maturation**
   - Threat: Not applicable (algorithms don't "learn")
   - Control: N/A

5. **Testing Effects**
   - Threat: Previous runs affecting later runs
   - Mitigation: Independent randomization per trial
   - Control: Fresh maps, cleared memory between runs

### External Validity

**Generalizability**:
- Results apply to 2D grid-based pathfinding
- May generalize to similar domains (game AI, robotics navigation)
- Different grid types may show different patterns
- Real-world performance may differ due to implementation details

**Scope Limitations**:
- Uniform movement costs (not weighted grids)
- Uniform grid size (not irregular structures)
- Unidirectional pathfinding (not bidirectional)
- Manhattan heuristic (not alternative heuristics)

### Reliability (Reproducibility)

**Ensuring Reproducibility**:
1. **Documented Procedure**: Complete methodology in this document
2. **Code Availability**: Full source code in repository
3. **Seed Documentation**: Exact random seeds used
4. **Map Storage**: Save test maps for exact reproduction
5. **Environment Documentation**: Hardware, OS, Python version

**Verification Procedure**:
- Someone else could follow methodology
- Implement algorithms from description
- Collect own data
- Compare results (should be similar within margin)

---

## Limitations & Assumptions

### Explicit Assumptions

1. **Heuristic Validity**:
   - Assumption: Manhattan distance is suitable heuristic
   - Impact: Results specific to this heuristic
   - Mitigation: Document heuristic choice, discuss limitations

2. **Optimal Implementation**:
   - Assumption: Implementations are reasonably efficient
   - Impact: Results depend on implementation quality
   - Mitigation: Use standard algorithms, efficient data structures

3. **Representative Test Cases**:
   - Assumption: Generated maps represent realistic scenarios
   - Impact: Results may not generalize to other map types
   - Mitigation: Test multiple map types, document limitations

4. **Measurement Accuracy**:
   - Assumption: Timers are sufficiently accurate
   - Impact: Very small differences may be noise
   - Mitigation: Use high-resolution timers, large samples, confidence intervals

### Known Limitations

1. **Single Hardware Platform**:
   - Can't generalize to all systems
   - Results relative to test machine

2. **2D Grid Limitation**:
   - Doesn't address continuous spaces
   - Doesn't address 3D pathfinding

3. **Uniform Costs**:
   - Real applications often have weighted costs
   - Results don't directly apply to weighted graphs

4. **Synthetic Maps**:
   - Generated maps may not match real-world complexity
   - Real terrain has different patterns

5. **One Heuristic**:
   - Results specific to Manhattan distance
   - Other heuristics might change relative performance

**Documentation**:
All limitations clearly stated in EE conclusion and evaluation sections.

---

## Ethical Considerations

### Academic Integrity
- ✓ Original application development
- ✓ Proper citation of algorithm sources
- ✓ Methodology properly documented
- ✓ Data collection transparent and reproducible
- ✓ No plagiarism or academic dishonesty

### Responsible Disclosure
- ✓ Methodology limitations clearly documented
- ✓ No misleading claims about applicability
- ✓ Honest reporting of findings
- ✓ Uncertainty appropriately expressed
- ✓ Limitations acknowledged

---

## References (Methodological)

### Core Algorithm Papers
- Hart, P.E., Nilsson, N.J., & Raphael, B. (1968). "A Formal Basis for the Heuristic Determination of Minimum Cost Paths." IEEE Transactions on Systems Science and Cybernetics, 4(2), 100-107.

- Dijkstra, E.W. (1959). "A note on two problems in connexion with graphs." Numerische Mathematik, 1(1), 269-271.

- Sturtevant, N.R. (2012). "Benchmarks for Grid-based Pathfinding." IEEE Transactions on Games, 4(2), 144-155.

### Statistical Methods
- Field, A. (2013). Discovering Statistics Using IBM SPSS Statistics (4th ed.). SAGE Publications. [ANOVA methodology]

- Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Routledge. [Effect sizes, power analysis]

### Experimental Design
- Kahn, M.J., & Marques, O. (2016). "Evaluation of a Robotic Wheelchair for Individuals With Severe Disabilities." Assistive Technology, 22(2), 87-98. [Controlled experimental design reference]

---

**Last Updated**: 2025-11-04
**Status**: Methodology Complete
**Next Step**: Begin Phase 1 implementation (foundation setup)
