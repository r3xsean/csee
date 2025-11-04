# IB Extended Essay Writing Guide - Comprehensive

Complete guide to structuring, formatting, and writing your Computer Science Extended Essay. This document covers official IB requirements and best practices specific to your pathfinding algorithm analysis project.

---

## PART 1: OFFICIAL IB STRUCTURE & FORMATTING

### Word Count Requirements

**CRITICAL:** Maximum 4,000 words

| Component | Included in Count | Typical Length |
|-----------|------------------|-----------------|
| Introduction | ✓ Yes | 300-500 words |
| Background/Context | ✓ Yes | 800-1000 words |
| Methodology | ✓ Yes | 600-800 words |
| Results/Analysis | ✓ Yes | 1500-1800 words |
| Discussion | ✓ Yes | 400-600 words |
| Conclusion | ✓ Yes | 200-400 words |
| **TOTAL** | | **3,900-4,000** |
| | | |
| Title Page | ✗ No | 1 page |
| Abstract | ✗ No | Max 300 words |
| Table of Contents | ✗ No | 1-2 pages |
| Bibliography | ✗ No | 1-3 pages |
| Appendices | ✗ No | Unlimited |

**Important Notes:**
- Examiners will NOT read beyond 4,000 words
- Anything past the limit is not considered in marking
- Minimum ~3,500 words recommended for sufficient depth
- All quotations count toward limit
- Code snippets in body count, but full code in appendix doesn't

### Required Document Order

```
1. Title Page (separate page, no content on reverse)
2. Abstract (separate page)
3. Table of Contents
4. Introduction
5. Body/Main Text
6. Conclusion
7. Bibliography
8. Appendices (optional)
```

### Formatting Specifications

**Font:**
- Size: 12 points
- Type: Professional readable font
- Acceptable: Times New Roman, Arial, Calibri, Georgia
- Consistent throughout

**Spacing:**
- Double-spacing throughout entire document
- Includes: body, references, appendices, quotations
- Line spacing: 2.0 (exactly double-spaced)
- Paragraph indentation: First-line indent 0.5 inch OR space between paragraphs (choose ONE)

**Margins:**
- 1 inch (2.54 cm) on all sides
- Top, bottom, left, right equal
- Headers/footers within margins

**Page Numbering:**
- Begin numbering on Table of Contents (page i, ii, iii in Roman numerals)
- Switch to Arabic numerals (1, 2, 3) starting with Introduction
- Place in top right corner or bottom center (be consistent)
- Continue consecutively through appendices

**Page Layout:**
```
[1 inch margin]
                                                                  [page number]

[Content area: 6.5 inches wide for 8.5" page]

[1 inch margin]
```

### Title Page Format

**Must include ONLY these four elements (centered, double-spaced):**

```
                    To what extent do the pathfinding algorithms
                    Dijkstra's Algorithm, A* (A-star), and Jump
                    Point Search differ in computational efficiency
                    and path optimality when navigating 2D grid-based
                    maps with varying obstacle densities?

                               Research Question

                       Computer Science (Category X)

                              Word Count: 3,847
```

**Critical Requirements:**
- ✗ Do NOT include candidate name
- ✗ Do NOT include school name
- ✗ Do NOT include candidate number
- ✗ Do NOT include supervisor name
- ✓ Title should be your actual essay title (usually based on RQ)
- ✓ Word count must be exact
- ✓ Double-spaced throughout
- ✓ Centered alignment

### Abstract Format

**Maximum 300 words (counted separately from 4,000)**

**Must appear on separate page immediately after title page**

**Purpose:**
- Summarize your entire essay
- Help reader understand scope and findings
- Provide standalone understanding of work

**What to Include:**
- Research question (how it was formulated)
- Scope of investigation (what was tested/analyzed)
- Methodology used (briefly)
- Key findings/conclusions (what you discovered)
- Significance of results

**Format:**
- Use complete sentences (NO bullet points)
- Third person preferred
- Brief but comprehensive
- Should be understandable independently

**Example Abstract:**
```
This essay investigates the extent to which three pathfinding algorithms
(Dijkstra's Algorithm, A*, and Jump Point Search) differ in computational
efficiency and path optimality when navigating 2D grid-based maps with
varying obstacle densities. A custom desktop application was developed to
conduct empirical testing across multiple map conditions (sizes 50×50 to
800×800, obstacle densities 10% to 70%), collecting 30,000+ performance
measurements. Statistical analysis using ANOVA testing revealed significant
differences in execution time and nodes explored (p < 0.001), with Jump
Point Search demonstrating 3-4x faster performance than Dijkstra's
Algorithm on average. Results indicate that heuristic-guided search and
geometric optimization provide substantial efficiency gains in grid-based
pathfinding, with practical implications for algorithm selection based on
environmental characteristics. The findings support theoretical complexity
predictions while revealing context-dependent performance patterns not
captured by Big-O notation alone.
```

### Table of Contents Format

**Appears after Abstract on separate page(s)**

**Requirements:**
- List all main sections with page numbers
- Use Roman numerals for pre-introduction pages (i, ii, iii)
- Use Arabic numerals for Introduction onward (1, 2, 3)
- Show hierarchical structure with indentation
- Include appendices

**Example Format:**
```
TABLE OF CONTENTS

Introduction ......................................... 1

Background Information ............................... 2
  - Historical Context ................................ 2
  - Dijkstra's Algorithm .............................. 3
  - A* Algorithm ....................................... 4
  - Jump Point Search .................................. 5

Methodology ........................................... 6
  - Research Design .................................... 6
  - Algorithm Implementations .......................... 7
  - Experimental Conditions ............................ 8
  - Data Collection Procedures ......................... 9

Results ............................................... 10
  - Performance Metrics ................................ 10
  - Execution Time Analysis ............................ 12
  - Search Efficiency Analysis ......................... 14

Analysis and Discussion ............................... 16
  - Algorithm Performance Comparison .................. 16
  - Impact of Obstacle Density ......................... 18
  - Scaling Behavior Analysis .......................... 20

Conclusion ............................................ 22

Bibliography .......................................... 24

Appendices ............................................ 25
  Appendix A: Algorithm Implementations .............. 25
  Appendix B: Raw Data Tables ......................... 30
  Appendix C: Statistical Analysis Output ............ 35
```

### Citations and Bibliography

**CRITICAL: IB Requirement for Date-Stamping**
- ALL electronic sources MUST include access date
- This supersedes individual citation style requirements
- Format: [Accessed: DD Month YYYY] or similar

**Acceptable Citation Styles:**
Choose ONE and apply consistently throughout

**IEEE Style (Recommended for Computer Science):**
```
[1] P. E. Hart, N. J. Nilsson, and B. Raphael, "A formal basis for
    the heuristic determination of minimum cost paths," IEEE
    Transactions on Systems Science and Cybernetics, vol. 4, no. 2,
    pp. 100–107, 1968.

[2] Red Blob Games, "Introduction to A*," available at
    https://www.redblobgames.com/pathfinding/a-star/
    [Accessed: 15 November 2023].
```

**Harvard Style (Author-Date):**
```
Hart, P.E., Nilsson, N.J. and Raphael, B. (1968) 'A formal basis for
the heuristic determination of minimum cost paths', IEEE Transactions
on Systems Science and Cybernetics, 4(2), pp. 100-107.

Red Blob Games (2023) Introduction to A*. Available at:
https://www.redblobgames.com/pathfinding/a-star/
(Accessed: 15 November 2023).
```

**Bibliography Requirements:**
- Include ONLY sources actually cited in essay
- Alphabetically ordered by author's last name (or title if no author)
- Hanging indent format (first line flush left, subsequent lines indented)
- Include: author, date, title, source, page numbers, URL (if online), access date (if online)
- Double-spaced like rest of document

**Minimum Bibliography for Computer Science:**
- At least 6-8 academic sources
- Mix of sources: academic papers, textbooks, technical documentation
- At least half should be from peer-reviewed sources
- Balance between primary (original papers) and secondary sources

---

## PART 2: SECTION-BY-SECTION WRITING GUIDE

### INTRODUCTION (300-500 words, typically page 1)

**Purpose:**
Orient reader, establish context, state RQ clearly, outline approach

**Structure:**

**Opening (Engaging Context - 50-100 words)**
- Hook: Why should reader care about pathfinding algorithms?
- Provide real-world context
- Explain significance of the problem

*Example:*
```
Pathfinding algorithms are fundamental to numerous modern applications,
from game artificial intelligence that steers non-player characters
through complex environments to autonomous vehicle navigation and
robotic path planning. The efficiency of these algorithms directly
impacts system performance, user experience, and computational resource
consumption. While multiple pathfinding approaches exist, significant
variation in their computational efficiency suggests that algorithm
selection could substantially improve application performance.
```

**Research Context (100-150 words)**
- Explain why this question matters
- Reference existing knowledge/research
- Position your work within the field
- Show this is a meaningful investigation

*Example:*
```
Dijkstra's Algorithm, developed in 1959, established the foundation for
shortest-path finding in weighted graphs through uniform-cost expansion.
However, this approach examines all directions equally, potentially
exploring vast portions of the search space. Later developments, including
the A* algorithm, incorporated heuristic guidance to focus search toward
the goal. More recently, Jump Point Search introduced geometric
optimization by pruning symmetric paths. Despite theoretical
improvements, empirical comparison of these algorithms across varying
environmental conditions remains limited, making it unclear how practical
performance compares across diverse scenarios.
```

**Research Question (Verbatim - clearly marked)**
- State exactly and clearly
- Formulate as actual question (not statement)
- Place in distinct paragraph or highlighted
- Should appear word-for-word as on title page

*Example:*
```
This investigation addresses the following research question:

"To what extent do the pathfinding algorithms Dijkstra's Algorithm,
A* (A-star), and Jump Point Search differ in computational efficiency
and path optimality when navigating 2D grid-based maps with varying
obstacle densities?"
```

**Scope and Approach (100-150 words)**
- Define what will be investigated
- Define what will NOT be investigated
- Outline methodology briefly
- Preview essay structure

*Example:*
```
This essay investigates these three algorithms specifically in the context
of 2D grid-based pathfinding with unweighted movement costs. The scope
excludes weighted graphs, continuous pathfinding spaces, and alternative
algorithms (such as bidirectional search or D*). The investigation employs
an empirical methodology, developing a custom application to measure
algorithm performance across varying map sizes and obstacle densities.
Metrics include execution time, search space size (nodes explored), and
path optimality. Statistical analysis using ANOVA testing evaluates
whether observed performance differences are statistically significant.
The essay proceeds with background information on each algorithm, detailed
methodology explanation, results presentation and analysis, and concluding
evaluation of findings.
```

**Introduction Checklist:**
- [ ] Opening establishes importance of topic
- [ ] Context explains why question matters
- [ ] Research question is clearly stated (word-for-word)
- [ ] Scope defined (what's included/excluded)
- [ ] Methodology briefly outlined
- [ ] Essay structure previewed
- [ ] No conclusions or findings mentioned
- [ ] Appropriate academic tone
- [ ] 300-500 words
- [ ] Flows logically into background section

---

### BACKGROUND & CONTEXT (800-1,000 words)

**Purpose:**
Establish knowledge foundation, demonstrate discipline understanding, position research

**Structure for Algorithm Comparison:**

**1. Historical/Theoretical Context (150-200 words)**

Explain the problem domain and theoretical basis

*Example structure:*
```
Graph theory provides the theoretical foundation for pathfinding.
Shortest-path problems have been central to computer science since
the advent of digital computing, with applications spanning network
routing, transportation planning, and artificial intelligence. The
formal definition of shortest paths in weighted directed graphs
establishes the mathematical framework against which algorithms are
evaluated. This context is essential for understanding how different
algorithmic approaches attempt to solve this optimization problem more
efficiently than exhaustive search methods.
```

**2. Algorithm #1: Dijkstra's Algorithm (200-250 words)**

For each algorithm, include:
- Historical development and author
- Core concept/approach
- How it works (high-level explanation)
- Time and space complexity
- Optimality guarantee
- Practical applications
- Key strengths and limitations

*Example:*
```
Dijkstra's Algorithm, published by Edsger W. Dijkstra in 1959,
represents a foundational approach to shortest-path finding. The
algorithm operates through uniform-cost expansion, systematically
examining nodes in order of their distance from the start point. At
each step, the algorithm selects the unexplored node with the smallest
known distance, marks it as explored, and updates distances to its
neighbors. This process continues until reaching the goal node.

The algorithm guarantees optimal paths in graphs with non-negative
weights, providing certainty about solution quality. With a binary heap
implementation, time complexity reaches O((V + E) log V), where V
represents vertices and E represents edges. Space complexity is O(V)
for storing distances and visited nodes.

Dijkstra's strength lies in its simplicity and guaranteed optimality.
However, its weakness is the exploration of nodes in all directions
uniformly, potentially examining large portions of the search space
regardless of goal location. In a grid with 10,000 cells where the goal
is nearby, Dijkstra might examine 8,000+ cells needlessly.
```

**3. Algorithm #2: A* Algorithm (250-300 words)**

Continue pattern for second algorithm

*Key points for A*:*
```
A*, developed by Hart, Nilsson, and Raphael (1968), addresses
Dijkstra's directional blindness through heuristic guidance. The
algorithm combines actual path cost (g(n), distance traveled) with
estimated remaining cost (h(n), heuristic estimate to goal), creating
a priority score f(n) = g(n) + h(n).

This heuristic component directs search toward the goal while
maintaining optimality IF the heuristic is "admissible" (never
overestimates true remaining distance). Manhattan distance, commonly
used on grids, is admissible, guaranteeing A* finds optimal paths.

Time complexity matches Dijkstra worst-case O((V + E) log V), but
practical performance is significantly better due to reduced search
space. The heuristic effectiveness depends on the problem domain—good
heuristics yield massive efficiency gains.

A* has become the industry standard for pathfinding in games, robotics,
and navigation systems due to its balance of optimality and efficiency.
```

**4. Algorithm #3: Jump Point Search (250-300 words)**

Continue pattern for third algorithm

*Key points for JPS:*
```
Jump Point Search, presented by Sturtevant (2012), optimizes A*
specifically for grid-based pathfinding. The algorithm leverages
geometric properties of rectangular grids to prune symmetric paths,
jumping multiple cells in a single step when no obstacles require
directional changes.

The core mechanism identifies "forced neighbors"—cells that become
reachable only through the current path due to obstacle placement. When
forced neighbors don't exist, the algorithm jumps across open space
rather than examining each cell. This geometric pruning reduces the
number of cells added to the open set.

JPS maintains A*'s optimality guarantee while typically achieving
10-40x speedup on grid-based problems. The improvement scales with
obstacle density—sparse environments (few obstacles) see less benefit
since fewer paths are pruned, while dense environments (many obstacles)
see greater benefits as pruning opportunities increase.

However, JPS complexity comes from jump point calculation, making it
less suitable for weighted grids or non-rectangular structures.
```

**5. Research Gap & Why This Matters (100-150 words)**

Connect theory to your investigation

*Example:*
```
While theoretical complexity analysis predicts relative algorithm
performance, empirical verification across varying conditions remains
limited in accessible literature. Specifically, most studies focus on
large-scale game environments or specific problem categories, leaving
unclear how these algorithms perform across systematically varying
obstacle densities and map sizes. Additionally, understanding
context-dependent performance—when each algorithm excels or struggles—
would provide practical guidance for algorithm selection in real
applications. This investigation addresses these gaps through
comprehensive empirical testing.
```

**Background Checklist:**
- [ ] Establishes theoretical context clearly
- [ ] Each algorithm explained with adequate detail
- [ ] Complexity analysis included
- [ ] Practical applications mentioned
- [ ] Sources cited appropriately (e.g., Hart et al. 1968)
- [ ] Uses subject-specific terminology accurately
- [ ] Flows logically from simple to complex
- [ ] Research gap identified and connected to investigation
- [ ] 800-1,000 words
- [ ] Transitions smoothly to methodology

---

### METHODOLOGY (600-800 words)

**Purpose:**
Enable reader to understand and evaluate your testing approach

**Critical for IB Criterion A (Focus and Method)**

**Structure:**

**1. Research Design Overview (100-150 words)**

*Why this approach?*
```
This investigation employs empirical comparative methodology, testing
algorithms under controlled conditions to measure performance
differences. This approach directly addresses the research question
by enabling quantitative comparison across multiple dimensions
(execution time, search efficiency, path quality) and conditions
(obstacle densities, map sizes). The empirical approach provides
objective evidence rather than relying on theoretical analysis alone,
capturing practical performance including implementation-specific
factors not captured by Big-O notation.
```

**2. Implementation Approach (150-200 words)**

- Programming language and choice justification
- Libraries/tools used
- Development methodology
- Environment specifications

*Example:*
```
All three algorithms were implemented in Python 3.10 using custom
implementations rather than existing libraries, ensuring consistent,
comparable code quality across algorithms. Python was selected for its
balance of readability (enabling peer review of algorithms) and
sufficient performance for pathfinding benchmarking. The tkinter GUI
framework provided real-time visualization, while numpy enabled
efficient numerical computation. All implementations use identical data
structures (priority queues, dictionaries for state management) to
ensure fair comparison. The A* and JPS implementations both employ
Manhattan distance as the heuristic function, making algorithms
comparable on the same basis.

Implementation was performed on [Windows 10, 16GB RAM, Intel i7
processor], with background processes minimized during testing.
```

**3. Experimental Conditions (200-250 words)**

**What variables were tested?**

*Example:*
```
Independent Variable—Obstacle Density:
The primary investigation variable was obstacle density, defined as
the percentage of grid cells containing obstacles. Testing covered
five density levels: 10%, 25%, 40%, 55%, and 70%. These levels span
from relatively sparse (10%—few obstacles, vast open space) to dense
(70%—many obstacles, constrained pathways). Selection of these specific
levels was based on preliminary testing revealing that performance
differences between algorithms were most pronounced across this range.

Secondary Variables—Map Size and Type:
To assess algorithm scaling, five map sizes were tested: 50×50,
100×100, 200×200, 400×400, and 800×800 cells. Size selection
represents a doubling progression, enabling logarithmic scaling analysis.

Map types included: Random (uniformly distributed obstacles), Clustered
(grouped obstacles, more realistic), Maze (narrow corridors), and Mixed
(combination of patterns).

Dependent Variables Measured:
1. Execution Time (milliseconds): Wall-clock time from algorithm start
   to goal-found completion, measured using Python's time.perf_counter()
   with microsecond precision
2. Nodes Explored (count): Number of cells examined during search
3. Path Length (grid units): Distance of discovered path
4. Success Rate (%): Percentage of test cases finding valid paths
```

**4. Testing Procedure (150-200 words)**

*Step-by-step process:*
```
For each test configuration (algorithm × map size × density × type):

1. Generate random map with specified obstacle density using
   pseudorandom generation (seeded for reproducibility)
2. Validate that start (top-left corner) and goal (bottom-right corner)
   are both accessible (not surrounded by obstacles)
3. Initialize performance measurement: start timer, zero node counter
4. Execute algorithm: run search from start to goal
5. Record measurements:
   - Execution time (start_time to completion_time)
   - Nodes explored (incremented during search)
   - Path length (calculated from final path)
6. Verify path optimality (all three should find identical length paths)
7. Save results to CSV file with timestamp
8. Repeat 100 times per configuration for statistical validity

Each trial used a unique random map to assess algorithm consistency
across environmental variations. No algorithm received advantage through
caching or pre-computation.
```

**5. Data Collection and Quality Control (100-150 words)**

```
Total test cases: 3 algorithms × 5 sizes × 5 densities × 4 types ×
100 trials = 30,000 individual algorithm runs

Data validation checks:
- Verified path validity (connected, obstacle-free, correct endpoints)
- Confirmed path optimality (identical path lengths for all algorithms)
- Identified outliers (runs >2 standard deviations from mean)
- Checked for missing data or collection errors
- Monitored system stability (noted any crashes or anomalies)

Results were automatically exported to CSV files with columns:
algorithm, trial, map_size, obstacle_density, map_type, execution_time,
nodes_explored, path_length, success.

Backup copies of data files were maintained on separate storage device.
```

**Methodology Checklist:**
- [ ] Research design justified for RQ
- [ ] Implementation approach described clearly
- [ ] Programming language choice explained
- [ ] All test conditions specified quantitatively
- [ ] Measurement procedures detailed
- [ ] Control variables identified
- [ ] Sample size justified (100 trials)
- [ ] Data collection process clear enough for replication
- [ ] Quality control measures described
- [ ] 600-800 words
- [ ] Uses appropriate technical terminology
- [ ] Flows logically into Results section

---

### RESULTS & ANALYSIS (1,500-1,800 words)

**Critical Section - Where IB Criterion C (Critical Thinking) is Assessed**

**This is the LONGEST section - allocate accordingly**

**Key Principle:** ANALYZE, don't just describe

**Structure:**

**1. Descriptive Statistics Presentation (300-400 words)**

Present processed data, not raw data

*Example format:*
```
Performance Metrics Summary:

Execution time across all conditions showed substantial variation by
algorithm (Table 1). Dijkstra's Algorithm averaged 47.2 ms ±15.3 ms
(mean ± standard deviation) across all test conditions, with minimum
time of 8.4 ms (50×50 grid, 10% density) and maximum of 156.2 ms
(800×800 grid, 70% density).

A* Algorithm averaged 21.8 ms ±9.1 ms, representing approximately 46%
reduction compared to Dijkstra. The improvement was consistent across
conditions, suggesting heuristic guidance systematically enhances
performance rather than providing context-dependent advantages.

Jump Point Search showed the lowest average execution time of 12.3 ms
±6.7 ms, approximately 74% faster than Dijkstra and 44% faster than A*.
This improvement was more pronounced at higher obstacle densities,
suggesting geometric optimization provides greater benefits in constrained
environments.

Search Space Analysis:
Nodes explored (proxy for search space size) mirrored execution time
patterns. Dijkstra averaged 2,847 nodes ±943, A* averaged 1,245 nodes
±521, and JPS averaged 634 nodes ±387 across conditions. These differences
directly correspond to the gap in execution times, indicating that
efficiency gains stem from examining fewer cells rather than faster
processing of each cell.

All algorithms successfully found optimal paths in 99.8% of test cases,
with the 0.2% failures occurring only on impossible-to-complete maps
where start/goal were isolated by obstacle rings (though validation
prevented such invalid test cases, confirming implementation
correctness).
```

**2. Graphical Presentation (With interpretation)**

Include 4-6 key graphs with caption explanations

*Graph 1: Execution Time by Algorithm across Obstacle Density*
```
[Description of what graph shows]
Figure 1: Mean execution time (milliseconds) for each algorithm across
five obstacle density levels, with error bars indicating ±1 standard
deviation. Data represents average of 100 trials per condition across
all map sizes combined.

[CRITICAL: Interpret the graph, don't just describe it]
The graph reveals several important patterns. First, execution time
increases monotonically with obstacle density for all three algorithms,
suggesting that obstacles complicate pathfinding. However, the rate of
increase differs significantly. Dijkstra's execution time increases
approximately linearly with density, while A* shows a more modest
increase, and JPS increases least dramatically. At 10% density, A*
demonstrates only 30% improvement over Dijkstra, but at 70% density,
this gap widens to 58%, suggesting that heuristic guidance becomes
increasingly valuable as obstacles become denser.

This pattern supports the theoretical prediction that heuristics (which
focus search toward the goal) provide greater benefit when obstacles
constrain the solution space, forcing more careful pathfinding decisions.
```

**3. Statistical Analysis (300-400 words)**

*ANOVA Testing Results:*
```
Statistical Significance Testing:

To determine whether observed performance differences are statistically
significant (not due to random variation), Analysis of Variance (ANOVA)
testing was performed on execution times across algorithm types.

Null Hypothesis (H₀): Mean execution times are equal across all three
algorithms
Alternative Hypothesis (H₁): At least one algorithm differs significantly

ANOVA Results:
F-statistic = 1,247.3
p-value < 0.001
Degrees of freedom: algorithm (2), error (8,998)

With p < 0.001 (far below standard significance threshold of 0.05),
the null hypothesis is decisively rejected. The probability that these
performance differences arose by random chance is less than 0.1%,
providing very strong evidence that algorithm choice genuinely affects
performance.

Effect Size:
Eta-squared (η²) = 0.216
This indicates that algorithm type explains 21.6% of the variance in
execution time. Approximately 78.4% of variation stems from other
factors (map size, obstacle density, specific map configuration),
confirming that while algorithm choice matters significantly, other
conditions also substantially influence performance.

Post-Hoc Analysis (Tukey HSD Test):
Pairwise comparisons between algorithms:

Dijkstra vs. A*: Mean difference = 25.4 ms, 95% CI [24.1, 26.7]
Significance: p < 0.001 (highly significant)

Dijkstra vs. JPS: Mean difference = 34.9 ms, 95% CI [33.6, 36.2]
Significance: p < 0.001 (highly significant)

A* vs. JPS: Mean difference = 9.5 ms, 95% CI [8.2, 10.8]
Significance: p < 0.001 (highly significant)

All three pairwise comparisons are statistically significant,
confirming that each algorithm differs meaningfully from the others.
```

**4. Condition-Specific Analysis (400-500 words)**

Deep analysis by condition - this is where critical thinking shines

*Example:*
```
Obstacle Density Effects:

At 10% density (sparse obstacles):
All algorithms performed well with minimal differences in execution
time (Dijkstra: 35.2 ms, A*: 19.1 ms, JPS: 11.3 ms). With few
obstacles, direct paths exist in most directions, reducing the advantage
of heuristic guidance. The primary benefit of A* and JPS derives from
avoiding examination of distant cells, not from clever pathfinding
around obstacles. This suggests that in sparse environments, simpler
algorithms may suffice if execution speed isn't critical.

At 55% density (moderately dense):
Performance differences became more pronounced (Dijkstra: 58.7 ms,
A*: 23.4 ms, JPS: 13.9 ms). With obstacles covering more than half the
space, finding paths requires more complex decision-making. Dijkstra's
uniform exploration becomes increasingly inefficient as it examines
dead-end corridors equally with promising paths. A* and JPS both
leverage knowledge of goal direction, reducing wasted exploration.

At 70% density (very dense):
Largest performance gaps emerged (Dijkstra: 89.3 ms, A*: 28.1 ms,
JPS: 15.2 ms). At this density, the environment transitions to a
maze-like structure where most direct paths are blocked. Here:
- Dijkstra explores vast numbers of cells before finding viable paths
- A* focuses on goal-directed search, reducing exploration
- JPS benefits most from geometric properties—long straight corridors
  between obstacles allow jump points, dramatically reducing cells examined

This progression clearly demonstrates that algorithm selection becomes
increasingly important as environments become more complex.

Map Size Scaling:

[Logarithmic scaling analysis]
Linear regression on log-log plot of map size vs. execution time:
- Dijkstra: slope = 1.78 (approaching O(n²) behavior)
- A*: slope = 1.65 (between linear and quadratic)
- JPS: slope = 1.52 (closer to linear)

These scaling exponents, all between 1 and 2, are consistent with
theoretical complexity of O((V+E) log V) where V scales with area
(n²) and E scales with area times neighborhood size. JPS's lower
slope indicates more favorable scaling—its performance degradation
with larger maps is less severe than other algorithms.

For practical implications: doubling map dimensions increases:
- Dijkstra execution time by ~3.4x (1.78 ≈ 2^1.78)
- A* execution time by ~3.1x
- JPS execution time by ~2.9x

This confirms that while all algorithms face increasing complexity
with larger maps, the impact varies, suggesting JPS provides
proportionally greater benefits for large-scale pathfinding problems.
```

**5. Mini-Conclusions Throughout (100-150 words)**

Synthesis of key findings as you progress

```
The analysis reveals three consistent, statistically significant
findings: First, A* systematically outperforms Dijkstra (46% faster
on average) across all conditions, confirming that heuristic guidance
provides measurable efficiency gains. Second, Jump Point Search
provides additional improvement over A* (44% faster), with the benefit
increasing as obstacle density increases, confirming that geometric
optimization provides context-dependent advantages. Third, these
improvements manifest as reduction in examined nodes rather than faster
per-node processing, indicating that algorithm choice primarily affects
search space size rather than implementation efficiency.
```

**Results & Analysis Checklist:**
- [ ] Key statistics presented (means, standard deviations, ranges)
- [ ] All graphs clearly titled and captioned
- [ ] Graphs are interpreted, not just described
- [ ] ANOVA or similar statistical test results included
- [ ] p-values and effect sizes reported
- [ ] Post-hoc tests (Tukey HSD) results shown
- [ ] Analysis addresses RQ directly
- [ ] Condition-specific patterns identified
- [ ] Unexpected findings discussed
- [ ] Why patterns exist is explained
- [ ] ANALYSIS outweighs description
- [ ] Every finding connects back to RQ
- [ ] 1,500-1,800 words
- [ ] Logical flow through sections
- [ ] Transitions to Discussion/Evaluation

---

### DISCUSSION & EVALUATION (400-600 words)

**Purpose:**
Evaluate methodology, address limitations, contextualize findings

**Structure:**

**1. Methodology Evaluation (150-200 words)**

Critical self-assessment

*Example:*
```
Strengths of Methodology:

The experimental design provided rigorous, systematic comparison. Testing
30,000 algorithm runs across multiple conditions enabled statistical
validation of findings, moving beyond anecdotal observations. The
100-trial repetition per condition provided sufficient replication to
establish reliable mean performance estimates with narrow confidence
intervals. Automated data collection eliminated human measurement error.
Implementation of all three algorithms in identical programming language
and using identical data structures ensured fair comparison, avoiding
confounds from implementation-specific optimizations.

Limitations of Methodology:

Testing focused exclusively on 2D grid-based pathfinding, limiting
generalizability to weighted graphs, continuous spaces, or non-rectangular
structures. A single heuristic function (Manhattan distance) was used,
leaving unanswered questions about whether different heuristics would
change relative algorithm performance. Testing occurred on one hardware
configuration; results may vary on different systems. The synthetic maps,
while systematically varied, may not reflect all real-world pathfinding
scenarios.
```

**2. Source Reliability Assessment (100-150 words)**

Evaluate quality and relevance of sources used

*Example:*
```
Sources employed represented high-quality academic literature. Original
algorithm papers (Hart et al. 1968, Dijkstra 1959, Sturtevant 2012)
provided authoritative foundations for algorithm descriptions. These
peer-reviewed publications in recognized venues (IEEE Transactions,
Numerische Mathematik) indicate substantial community scrutiny.
Contemporary implementation guides (Red Blob Games, 2016) provided
practical guidance while referencing same foundational papers, creating
consistency across sources. The limited sample of sources reflects the
narrow scope of comparative studies in this specific area rather than
source unavailability.
```

**3. Findings in Context (150-200 words)**

How do results relate to theory and existing knowledge?

*Example:*
```
Theoretical Alignment:

Empirical results closely matched theoretical complexity predictions.
Dijkstra's O((V+E) log V) predicted dominance in sparse, unstructured
search spaces appeared in the 10% density results where A* advantage
was minimal. A*'s theoretical advantage through heuristic guidance
manifested in the monotonic performance improvement as obstacle density
increased, with heuristic focus becoming increasingly valuable in
constrained environments. Jump Point Search's geometric optimization
benefits aligned with predictions—improvement was most pronounced where
obstacles create opportunities for jumping across multiple cells.

Practical Implications:

These findings inform algorithm selection in real applications:
- For simple, open environments (few obstacles), simpler algorithms may
  suffice
- For structured pathfinding (game maps, warehouse navigation), A*
  provides excellent performance/complexity trade-off
- For dense, complex environments (urban navigation, dense game worlds),
  Jump Point Search provides substantial additional benefits
```

**4. Unexpected Findings or Anomalies (if applicable)**

```
[If results deviated from expectations, explain why]
Example: "JPS's scaling advantage diminished at the 800×800 map size,
where memory overhead of jump point calculation became significant.
This suggests diminishing returns beyond certain problem sizes, with
implications for very large-scale pathfinding."
```

**Discussion Checklist:**
- [ ] Methodology strengths articulated
- [ ] Limitations honestly acknowledged
- [ ] Findings connected to theoretical predictions
- [ ] Practical implications explained
- [ ] Alternative interpretations considered
- [ ] Unexpected findings addressed (if any)
- [ ] Sources evaluated for reliability
- [ ] Generalizability discussed
- [ ] 400-600 words
- [ ] Transitions smoothly to Conclusion

---

### CONCLUSION (200-400 words)

**Purpose:**
Answer RQ directly, synthesize findings, suggest future directions

**Structure:**

**1. Restatement of RQ (20-40 words)**
Remind reader of central question

```
This investigation addressed the research question: "To what extent do
the pathfinding algorithms Dijkstra's Algorithm, A* (A-star), and Jump
Point Search differ in computational efficiency and path optimality when
navigating 2D grid-based maps with varying obstacle densities?"
```

**2. Direct Answer to RQ (100-150 words)**
Clear, evidence-based response

```
The findings demonstrate that these three algorithms differ substantially
and significantly in computational efficiency. On average across all test
conditions, A* executed 46% faster than Dijkstra's Algorithm, while Jump
Point Search proved 74% faster than Dijkstra and 44% faster than A*.
These differences increased with obstacle density, suggesting that while
all algorithms solve the pathfinding problem optimally (no difference in
path length), they achieve this through different search strategies with
dramatically different computational costs.

All three algorithms maintained path optimality (identical path lengths
discovered), indicating that efficiency differences stem entirely from
algorithmic approach, not solution quality. The data decisively answers
the research question: these algorithms differ significantly in
efficiency, with differences being statistically significant (p < 0.001)
and practically meaningful (2-4x execution time variation).
```

**3. Key Findings Summary (100-150 words)**
Synthesize main conclusions

```
Several conclusions emerge from comprehensive analysis:

First, heuristic guidance (A*'s differentiating feature) provides
consistent, systematic efficiency improvements across all conditions.
The 46% average improvement reflects heuristic-guided focus toward the
goal rather than uniform exploration.

Second, geometric optimization (JPS's contribution) provides additional
benefits that increase with complexity. At low densities, JPS's advantage
over A* was minimal (19% improvement), but at high densities, this
expanded to 46% improvement, indicating context-dependent optimization.

Third, practical implications for algorithm selection are clear: algorithm
choice should consider environmental characteristics. Simple environments
tolerate simpler algorithms; complex environments benefit from sophisticated
algorithms.
```

**4. Significance and Implications (50-100 words)**

Why do these findings matter?

```
These findings contribute to computational understanding of pathfinding
efficiency. For practitioners developing navigation systems, results
provide empirical justification for algorithm selection decisions.
Moreover, the research methodology—systematic comparison across multiple
conditions with statistical validation—provides a template for future
algorithmic comparisons.
```

**5. Limitations Acknowledged (50-75 words)**

Final honest assessment

```
While findings are robust for 2D grid-based pathfinding, generalization
to weighted graphs, continuous spaces, or alternative heuristics remains
unclear. Future research investigating these dimensions would strengthen
understanding of algorithm behavior across broader pathfinding contexts.
```

**6. Future Research Directions (50-75 words)**

Forward-looking conclusion

```
Promising directions for future investigation include: testing
algorithms with alternative heuristic functions; extending analysis to
weighted graphs; investigating bidirectional search variants; and
empirically comparing these algorithms within real game engines or
autonomous navigation systems where environmental conditions and
constraints differ from controlled laboratory conditions.
```

**Conclusion Checklist:**
- [ ] Research question restated
- [ ] Direct answer provided (not hedged)
- [ ] Supported by evidence from results
- [ ] Key findings summarized (3-4 main conclusions)
- [ ] Significance explained
- [ ] Limitations acknowledged
- [ ] Future research suggested
- [ ] No new information introduced
- [ ] 200-400 words
- [ ] Flows naturally from Discussion
- [ ] Professional, conclusive tone

---

## PART 3: CRITICAL WRITING PRINCIPLES

### Avoiding Descriptive Writing

**Problem:** Simply stating facts without interpretation

**Weak (Descriptive):**
```
Algorithm A completed in 25ms while Algorithm B completed in 45ms.
```

**Strong (Analytical):**
```
Algorithm A's 25ms execution time represented 44% improvement over
Algorithm B's 45ms, suggesting that the heuristic guidance component
successfully reduced search space exploration despite identical worst-case
time complexity. This efficiency gain aligns with theoretical predictions
and indicates practical superiority for this problem domain.
```

**Weak (Descriptive):**
```
Jump Point Search showed faster performance at higher obstacle densities.
```

**Strong (Analytical):**
```
Jump Point Search's relative performance advantage increased from 19% at
10% obstacle density to 46% at 70% density. This pattern reflects
geometric properties of constrained environments: higher obstacle
concentrations create longer unobstructed corridors, enabling jump point
detection to skip cells more frequently. The data suggests that
algorithm selection should consider environmental characteristics, with
more sophisticated algorithms providing proportionally greater benefits in
complex environments.
```

### Maintaining Academic Tone

**Avoid:**
- Informal language: "way faster" → "substantially faster"
- First person: "I think..." → Remove or rephrase
- Emotional language: "surprisingly" → "contrary to expectations"
- Absolute claims: "always" → "in all tested conditions"
- Opinions: "obviously" → Support with evidence

**Maintain:**
- Precise, technical terminology
- Measured, evidence-based claims
- Third-person perspective
- Objective, scholarly tone
- Citations for all claims not original to your work

### Proper Source Integration

**Weak Integration (Too quote-heavy):**
```
Hart et al. (1968) state that "A formal basis for the heuristic
determination of minimum cost paths" (Hart et al., 1968). [Examiners
should never see the exact citation twice in one sentence]
```

**Strong Integration:**
```
The A* algorithm, formally introduced by Hart, Nilsson, and Raphael
(1968), combines path cost with heuristic estimation to guide search
toward the goal. This approach leverages domain-specific knowledge to
improve search efficiency while maintaining the optimality guarantee
essential for shortest-path applications.
```

**Weak Integration (No context):**
```
"A* maintains optimality if the heuristic is admissible" (Hart et al.,
1968).
```

**Strong Integration:**
```
A* guarantees optimal solutions when employing an "admissible" heuristic
—one that never overestimates true remaining distance (Hart et al.,
1968). Manhattan distance, commonly used in grid-based applications, is
admissible, making it suitable for this investigation.
```

### Word Count Management Strategy

**Don't:**
- Use padding phrases like "It is important to note" or "In conclusion"
- Include unnecessarily long quotations
- Repeat the same point in different words
- Use passive voice when active is shorter
- Include examples that don't directly support analysis

**Do:**
- Trim unnecessary words: "The results show that" → "Results show"
- Use active voice: "was implemented" → "implemented"
- Include only essential background
- Prioritize analysis over description
- Use tables/figures for complex data

**Sample Trimming:**
```
Original (60 words):
"It is important to note that the algorithm in question was tested
extensively across a wide variety of different testing conditions in
order to ensure that the findings would be comprehensive and would
cover a broad range of scenarios."

Trimmed (25 words):
"Algorithm testing spanned multiple conditions to ensure comprehensive,
broadly applicable findings."

Saved: 35 words (58% reduction)
```

---

## PART 4: REFLECTIONS ON PLANNING & PROGRESS FORM (RPPF)

**Critical for Criterion E (Engagement) - Worth 6 Points**

**Format:**
- Maximum 500 words (examiners won't read beyond)
- Separate document submitted with essay
- Three reflection points required
- Analytical and evaluative, NOT descriptive
- Same language as essay

**Three Required Reflections:**

**Reflection 1: Initial Planning**
*Completed before/early in research*

Questions to address:
- How did you select this topic/RQ?
- Why is it significant to you?
- What initial research did you undertake?
- What challenges did you anticipate?
- How did your thinking evolve?

*Example:*
```
I selected pathfinding algorithm comparison because of my interest in
game development and the role of artificial intelligence in creating
intelligent game behavior. Initial research revealed that while
theoretical complexity analysis is straightforward, empirical comparison
across varying conditions remained limited in accessible sources. This
gap motivated investigating how theory translates to practical
performance.

My initial approach planned only Dijkstra and A* comparison, but further
reading about Jump Point Search revealed recent development (2012) with
claimed significant improvements. Including JPS enriched the investigation
into a three-way comparison showing algorithmic evolution. This evolution
of my research question, from binary to ternary comparison, demonstrated
how deeper literature engagement shaped my investigation.
```

**Reflection 2: Process Reflection**
*Completed mid-way through research*

Questions to address:
- What challenges did you encounter?
- How did you respond to difficulties?
- What revisions to your plan were necessary?
- What have you learned about your topic?
- How has your understanding deepened?

*Example:*
```
The most significant challenge was designing fair algorithm comparison.
Initially, I implemented algorithms using Python's heapq library for
priority queues. However, recognizing that different heap implementations
could bias results, I investigated alternative implementations and
ultimately chose to develop custom priority queue implementations based on
binary heaps. This decision, though time-consuming, ensured genuinely fair
comparison.

Data collection revealed an unexpected pattern: JPS's performance advantage
increased dramatically at high obstacle densities, far exceeding my initial
predictions. Rather than dismissing this as anomalous, I investigated the
theoretical basis for geometric optimization in constrained environments,
discovering that this pattern reflected fundamental properties of how
obstacles create pathfinding opportunities. This unexpected finding
transformed my understanding from expecting uniform improvement to
appreciating context-dependent advantages.

Initially underestimating the importance of proper experimental design,
I learned that generating comparable test conditions required careful
attention to map generation, randomization, and validation procedures.
```

**Reflection 3: Final Reflection/Viva Response**
*Completed after all research done*

Questions to address:
- What have you achieved in this investigation?
- What were key intellectual challenges?
- What would you do differently?
- What limitations do you recognize?
- What have you learned about research methodology?

*Example:*
```
This investigation achieved comprehensive empirical comparison of three
pathfinding algorithms across systematically varied conditions, providing
both theoretical validation and practical insights. The 30,000 data points
collected enabled statistical validation of findings, moving beyond
anecdotal comparison to evidence-based conclusions.

The primary intellectual challenge was maintaining critical analysis
throughout the investigation. It was tempting to present results
descriptively; developing the discipline to interpret every finding in
relation to the research question required constant self-monitoring.
Learning to ask "Why does this matter?" and "What does this reveal about
algorithm selection?" strengthened my analytical thinking.

If repeating this investigation, I would expand testing to weighted graphs
and alternative heuristics earlier, recognizing that comprehensive
comparison requires investigating multiple dimensions. Additionally, I
would integrate application development more closely with data analysis,
using preliminary results to inform subsequent testing conditions.

This research taught me that empirical investigation requires careful
attention to methodology—controlling variables, validating data, and
designing appropriate comparisons. The experience demonstrated that
theoretical knowledge and practical understanding often diverge,
highlighting the importance of empirical verification.
```

**RPPF Checklist:**
- [ ] Three separate reflections completed
- [ ] Each under 250 words (total under 500)
- [ ] Analytical and evaluative tone
- [ ] Personal engagement evident
- [ ] Intellectual challenges discussed
- [ ] Decision-making explained
- [ ] Learning demonstrated
- [ ] Not written as diary/chronology
- [ ] Submitted with main essay
- [ ] Same language as essay

---

## PART 5: FINAL SUBMISSION CHECKLIST

### Before Submitting, Verify:

**Content Completeness:**
- [ ] Title page (with essay title, RQ, subject, word count only)
- [ ] Abstract (max 300 words on separate page)
- [ ] Table of Contents (with accurate page numbers)
- [ ] Introduction (300-500 words)
- [ ] Background (800-1,000 words)
- [ ] Methodology (600-800 words)
- [ ] Results & Analysis (1,500-1,800 words)
- [ ] Discussion/Evaluation (400-600 words)
- [ ] Conclusion (200-400 words)
- [ ] Bibliography (minimum 6-8 sources)
- [ ] Appendices (code, data tables, additional graphs)
- [ ] RPPF completed (500 words max)

**Formatting:**
- [ ] 12-point readable font throughout
- [ ] Double-spaced (2.0 line spacing)
- [ ] 1-inch (2.54cm) margins all sides
- [ ] Page numbers on all pages starting from TOC
- [ ] Professional, consistent appearance
- [ ] No identifying information (name, school, candidate number)

**Word Count:**
- [ ] Total between 3,500-4,000 words
- [ ] Abstract counted separately (max 300)
- [ ] Bibliography/appendices NOT counted
- [ ] Word count stated on title page

**Citations & Bibliography:**
- [ ] All sources cited consistently
- [ ] At least 6-8 academic sources
- [ ] Mix of primary and secondary sources
- [ ] All online sources include access dates
- [ ] Bibliography alphabetically ordered
- [ ] Proper formatting for chosen style (IEEE/Harvard/etc.)
- [ ] No sources cited that aren't used
- [ ] Complete publication information

**Analysis & Argument:**
- [ ] RQ clearly stated in introduction
- [ ] Focus maintained throughout
- [ ] Analysis outweighs description
- [ ] Every claim supported by evidence
- [ ] Results section includes interpretation
- [ ] Conclusions supported by evidence
- [ ] Limitations acknowledged
- [ ] Alternative interpretations considered

**Academic Standards:**
- [ ] No plagiarism (all sources cited)
- [ ] Academic tone throughout
- [ ] Precise technical terminology
- [ ] Clear logical flow
- [ ] Grammar and spelling correct
- [ ] Figures and tables properly labeled
- [ ] Smooth transitions between sections

**IB Assessment Criteria:**
- [ ] **Criterion A:** Sharp RQ, clear methodology → 5-6 points
- [ ] **Criterion B:** Deep CS knowledge, accurate terminology → 5-6 points
- [ ] **Criterion C:** Rigorous analysis, evidence-based conclusions → 10-12 points
- [ ] **Criterion D:** Professional presentation, clear structure → 3-4 points
- [ ] **Criterion E:** RPPF shows engagement and reflection → 5-6 points
- [ ] **Predicted Total:** 28-34 points

---

## QUICK REFERENCE: SECTION LENGTHS

```
Title Page:              1 page
Abstract:               1 page (max 300 words)
TOC:                    1-2 pages
Introduction:           1-2 pages (300-500 words)
Background:             2-4 pages (800-1,000 words)
Methodology:            2-3 pages (600-800 words)
Results & Analysis:     4-6 pages (1,500-1,800 words)
Discussion:             1-2 pages (400-600 words)
Conclusion:             1 page (200-400 words)
Bibliography:           1-3 pages
Appendices:             2-10 pages (not assessed)

TOTAL MAIN TEXT:        ~18-24 pages for 4,000 words
```

---

## SAMPLE OUTLINE FOR YOUR EE

Quick template you can adapt:

```
1. TITLE PAGE
   - Title: To what extent do the pathfinding algorithms Dijkstra's
     Algorithm, A*, and Jump Point Search differ in computational
     efficiency and path optimality...
   - Research Question: [same as title]
   - Subject: Computer Science
   - Word Count: [Your count]

2. ABSTRACT (prepare last, after writing full essay)
   [Summarize entire investigation in 250-300 words]

3. TABLE OF CONTENTS
   [Auto-generated after completing essay]

4. INTRODUCTION (page 1)
   - Hook: Why pathfinding matters
   - Context: GPS, games, robotics
   - RQ statement
   - Scope preview
   - Methodology outline
   [300-500 words]

5. BACKGROUND (pages 2-4)
   - Graph theory and shortest paths (theory)
   - Dijkstra's Algorithm (250 words)
   - A* Algorithm (250 words)
   - Jump Point Search (250 words)
   - Why this investigation matters (research gap)
   [800-1,000 words]

6. METHODOLOGY (pages 4-6)
   - Research design justification
   - Implementation approach (Python, libraries)
   - Testing conditions (map sizes, densities, types)
   - Measurement procedures (time, nodes, paths)
   - Statistical methods (ANOVA)
   - Quality control
   [600-800 words]

7. RESULTS & ANALYSIS (pages 6-10)
   - Descriptive statistics table
   - Execution time graph with interpretation
   - Nodes explored graph with interpretation
   - ANOVA results with significance
   - Obstacle density analysis
   - Map size scaling analysis
   - Mini-conclusion
   [1,500-1,800 words]

8. DISCUSSION (pages 10-11)
   - Methodology evaluation (strengths & limitations)
   - How findings align with theory
   - Practical implications
   - Reliability and generalizability
   [400-600 words]

9. CONCLUSION (page 11-12)
   - RQ restatement
   - Direct answer to RQ
   - Key findings summary (3-4 points)
   - Significance
   - Limitations
   - Future research
   [200-400 words]

10. BIBLIOGRAPHY
    - Hart et al. (1968) - Original A* paper
    - Dijkstra (1959) - Original Dijkstra paper
    - Sturtevant (2012) - JPS and benchmarking
    - Patel (2016) - Red Blob Games A* guide
    - [5-10 more academic sources]

11. APPENDICES
    A. Algorithm Pseudocode
    B. Implementation Code
    C. Raw Data Tables
    D. Statistical Output
    E. Additional Graphs
```

---

**Last Updated**: 2025-11-04
**Status**: Comprehensive Writing Guide Complete
**Next Step**: Begin outlining your essay structure, then start with Introduction
