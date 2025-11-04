"""
Pathfinding Algorithm Comparison - ALL-IN-ONE APPLICATION
IB Computer Science Extended Essay

Single unified application with all features:
- Single Algorithm View
- Triple Comparison View
- Batch Testing & Analysis

Just run: python app.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import threading
import sys
import os

sys.path.insert(0, 'src')

from algorithms.dijkstra import DijkstraVisualizer
from algorithms.astar import AStarVisualizer
from algorithms.greedy import GreedyVisualizer
from utils.batch_tester import BatchTester
from analysis.statistical_analysis import StatisticalAnalyzer
from analysis.graph_generator import GraphGenerator


class UnifiedPathfindingApp:
    """One application with all features in tabs"""

    def __init__(self, root):
        self.root = root
        self.root.title("Pathfinding Algorithms - IB CS Extended Essay")
        self.root.geometry("1400x900")

        # Algorithm map
        self.algorithm_map = {
            "Dijkstra": DijkstraVisualizer,
            "A*": AStarVisualizer,
            "Greedy": GreedyVisualizer
        }

        # Batch tester
        self.batch_tester = BatchTester()
        self.current_results_file = None

        # Create tabbed interface
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create tabs
        self.setup_single_view_tab()
        self.setup_triple_view_tab()
        self.setup_batch_test_tab()

    # ==================== TAB 1: SINGLE ALGORITHM VIEW ====================
    def setup_single_view_tab(self):
        """Single algorithm visualization"""
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Single Algorithm")

        # Grid config
        self.single_grid_size = tk.IntVar(value=40)
        self.single_cell_size = 15
        self.single_density = tk.DoubleVar(value=0.25)

        # State
        grid_size = self.single_grid_size.get()
        self.single_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.single_start = (2, 2)
        self.single_end = (grid_size-3, grid_size-3)
        self.single_grid[self.single_start[0]][self.single_start[1]] = 2
        self.single_grid[self.single_end[0]][self.single_end[1]] = 3
        self.single_visited = set()
        self.single_path = []
        self.single_running = False
        self.single_paused = False
        self.single_dragging = None
        self.single_algorithm = tk.StringVar(value="Dijkstra")
        self.single_speed = tk.IntVar(value=1)

        # Layout
        main = tk.Frame(tab)
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left: Controls
        left = tk.Frame(main, width=250)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left.pack_propagate(False)

        tk.Label(left, text="Algorithm", font=("Arial", 12, "bold")).pack(pady=5)
        for algo in ["Dijkstra", "A*", "Greedy"]:
            tk.Radiobutton(left, text=algo, variable=self.single_algorithm, value=algo).pack(anchor=tk.W, padx=20)

        tk.Label(left, text="Grid Size", font=("Arial", 10, "bold")).pack(pady=(15, 5))
        tk.Scale(left, from_=20, to=100, resolution=10, orient=tk.HORIZONTAL,
                variable=self.single_grid_size, length=200, label="20 = Small, 100 = Large").pack()

        tk.Label(left, text="Obstacle Density", font=("Arial", 10, "bold")).pack(pady=(15, 5))
        tk.Scale(left, from_=0.0, to=0.7, resolution=0.05, orient=tk.HORIZONTAL,
                variable=self.single_density, length=200).pack()

        tk.Label(left, text="Animation Speed", font=("Arial", 10, "bold")).pack(pady=(15, 5))
        tk.Scale(left, from_=1, to=50, resolution=1, orient=tk.HORIZONTAL,
                variable=self.single_speed, length=200, label="1x = Normal, 50x = Max").pack()

        tk.Button(left, text="Run Algorithm", command=self.run_single,
                 bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=18, height=2).pack(pady=10)

        # Control buttons frame
        ctrl_frame = tk.Frame(left)
        ctrl_frame.pack(fill=tk.X, pady=5)

        self.single_pause_btn = tk.Button(ctrl_frame, text="Pause", command=self.toggle_single_pause,
                                          bg="#FFC107", fg="black", font=("Arial", 10, "bold"), width=8, state="disabled")
        self.single_pause_btn.pack(side=tk.LEFT, padx=2)

        tk.Button(ctrl_frame, text="Stop", command=self.stop_single,
                 bg="#D32F2F", fg="white", font=("Arial", 10, "bold"), width=8).pack(side=tk.LEFT, padx=2)

        tk.Button(left, text="Reset", command=self.reset_single,
                 bg="#2196F3", fg="white", font=("Arial", 11, "bold"), width=18).pack(pady=5)
        tk.Button(left, text="New Map", command=self.regen_single,
                 bg="#FF9800", fg="white", font=("Arial", 11, "bold"), width=18).pack(pady=5)

        self.single_stats = tk.Label(left, text="Ready", font=("Courier", 9), justify=tk.LEFT, wraplength=220)
        self.single_stats.pack(pady=15, fill=tk.BOTH, expand=True)

        # Right: Canvas
        right = tk.Frame(main)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.single_canvas_title = tk.Label(right, text="Dijkstra's Algorithm", font=("Arial", 14, "bold"))
        self.single_canvas_title.pack(pady=5)

        # Fixed canvas size - cell size will adjust based on grid size
        self.single_canvas_width = 600
        self.single_canvas_height = 600
        self.single_canvas = tk.Canvas(right, width=self.single_canvas_width,
                                       height=self.single_canvas_height,
                                       bg="white", highlightthickness=1)
        self.single_canvas.pack()

        # Legend
        legend = tk.Frame(right)
        legend.pack(pady=10)
        for i, (color, text) in enumerate([("#4CAF50", "Start"), ("#F44336", "End"),
                                            ("#424242", "Obstacle"), ("#BBDEFB", "Explored"), ("#FFD700", "Path")]):
            f = tk.Frame(legend)
            f.grid(row=0, column=i, padx=10)
            c = tk.Canvas(f, width=20, height=20, bg="white", highlightthickness=1)
            c.pack()
            c.create_rectangle(2, 2, 18, 18, fill=color, outline="")
            tk.Label(f, text=text, font=("Arial", 9)).pack()

        tk.Label(right, text="Drag start/end points • Change algorithm • Run and compare!",
                font=("Arial", 9, "italic"), fg="#666").pack()

        self.generate_single_obstacles()
        self.draw_single_grid()
        self.single_canvas.bind("<Button-1>", self.single_mouse_down)
        self.single_canvas.bind("<B1-Motion>", self.single_mouse_drag)
        self.single_canvas.bind("<ButtonRelease-1>", self.single_mouse_up)

    def generate_single_obstacles(self):
        grid_size = self.single_grid_size.get()
        for i in range(grid_size):
            for j in range(grid_size):
                if (i, j) == self.single_start or (i, j) == self.single_end:
                    continue
                if random.random() < self.single_density.get():
                    self.single_grid[i][j] = 1

    def draw_single_grid(self):
        self.single_canvas.delete("all")
        grid_size = self.single_grid_size.get()
        cell_size = self.single_canvas_width // grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                if (i, j) == self.single_start:
                    color = "#4CAF50"
                elif (i, j) == self.single_end:
                    color = "#F44336"
                elif (i, j) in self.single_path:
                    color = "#FFD700"
                elif (i, j) in self.single_visited:
                    color = "#BBDEFB"
                elif self.single_grid[i][j] == 1:
                    color = "#424242"
                else:
                    color = "white"
                self.single_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#E0E0E0")

    def run_single(self):
        if self.single_running:
            return
        self.single_running = True
        self.single_paused = False
        self.single_visited = set()
        self.single_path = []
        algo_name = self.single_algorithm.get()
        self.single_canvas_title.config(text=f"{algo_name} Algorithm")
        self.single_stats.config(text="Computing...")
        self.root.update()

        # Run algorithm to completion FIRST (get true performance data)
        self.single_visualizer = self.algorithm_map[algo_name](self.single_grid, self.single_start, self.single_end)

        # Record execution history
        self.single_execution_history = []
        while self.single_visualizer.step():
            self.single_execution_history.append(self.single_visualizer.get_visited().copy())

        # Get final state
        self.single_execution_history.append(self.single_visualizer.get_visited().copy())
        self.single_path = self.single_visualizer.get_path()
        stats = self.single_visualizer.get_stats()

        # Display final stats
        if self.single_path:
            text = f"✓ COMPLETE\n\n"
            text += f"Nodes: {stats['nodes_explored']}\n"
            text += f"Path: {stats['path_length']} cells\n"
            text += f"Time: {stats['time_ms']:.3f} ms"
            self.single_stats.config(text=text)
        else:
            self.single_stats.config(text="No path found!")

        # Now replay the execution as animation
        self.single_replay_index = 0
        self.single_pause_btn.config(state="normal")
        self.animate_single_replay()

    def animate_single_replay(self):
        """Replay pre-computed algorithm execution"""
        # Check if stopped
        if not self.single_running:
            return

        if self.single_paused:
            self.root.after(10, self.animate_single_replay)
            return

        speed = self.single_speed.get()

        # Advance replay by 'speed' steps
        self.single_replay_index += speed

        # Update visited set based on replay index
        if self.single_replay_index < len(self.single_execution_history):
            self.single_visited = self.single_execution_history[self.single_replay_index]
            # Don't show path during replay - only exploration
            saved_path = self.single_path
            self.single_path = []
            self.draw_single_grid()
            self.single_path = saved_path
        else:
            # Replay finished - NOW show final state with path
            self.single_visited = self.single_execution_history[-1]
            self.draw_single_grid()
            self.single_running = False
            self.single_paused = False
            self.single_pause_btn.config(state="disabled", text="Pause")
            return

        # Continue replay
        delay = 10
        self.root.after(delay, self.animate_single_replay)

    def toggle_single_pause(self):
        """Toggle pause/resume"""
        self.single_paused = not self.single_paused
        if self.single_paused:
            self.single_pause_btn.config(text="Resume", bg="#4CAF50")
            self.single_stats.config(text="⏸ PAUSED")
        else:
            self.single_pause_btn.config(text="Pause", bg="#FFC107")

    def stop_single(self):
        """Stop algorithm"""
        if self.single_running or self.single_paused:
            self.single_running = False
            self.single_paused = False
            self.single_pause_btn.config(state="disabled", text="Pause")
            self.single_stats.config(text="⏹ STOPPED")
            self.single_visited = set()
            self.single_path = []
            self.draw_single_grid()

    def reset_single(self):
        self.single_visited = set()
        self.single_path = []
        self.single_running = False
        self.single_paused = False
        self.single_pause_btn.config(state="disabled", text="Pause")
        self.single_stats.config(text="Ready")
        self.draw_single_grid()

    def regen_single(self):
        if self.single_running:
            return
        # Regenerate grid with new size
        grid_size = self.single_grid_size.get()
        self.single_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.single_start = (2, 2)
        self.single_end = (grid_size-3, grid_size-3)
        self.single_grid[self.single_start[0]][self.single_start[1]] = 2
        self.single_grid[self.single_end[0]][self.single_end[1]] = 3
        self.generate_single_obstacles()
        self.reset_single()

    def single_mouse_down(self, event):
        if self.single_running:
            return
        grid_size = self.single_grid_size.get()
        cell_size = self.single_canvas_width // grid_size
        cell = self.get_cell(event.x, event.y, cell_size, grid_size)
        if cell and cell == self.single_start:
            self.single_dragging = 'start'
        elif cell and cell == self.single_end:
            self.single_dragging = 'end'

    def single_mouse_drag(self, event):
        if not self.single_dragging:
            return
        grid_size = self.single_grid_size.get()
        cell_size = self.single_canvas_width // grid_size
        cell = self.get_cell(event.x, event.y, cell_size, grid_size)
        if not cell or self.single_grid[cell[0]][cell[1]] == 1:
            return
        if self.single_dragging == 'start' and cell != self.single_end:
            self.single_grid[self.single_start[0]][self.single_start[1]] = 0
            self.single_start = cell
            self.single_grid[cell[0]][cell[1]] = 2
        elif self.single_dragging == 'end' and cell != self.single_start:
            self.single_grid[self.single_end[0]][self.single_end[1]] = 0
            self.single_end = cell
            self.single_grid[cell[0]][cell[1]] = 3
        self.single_visited = set()
        self.single_path = []
        self.draw_single_grid()

    def single_mouse_up(self, event):
        self.single_dragging = None

    # ==================== TAB 2: TRIPLE VIEW ====================
    def setup_triple_view_tab(self):
        """Side-by-side three algorithm comparison"""
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Triple Comparison")

        # Grid config
        self.triple_grid_size = tk.IntVar(value=30)
        self.triple_density = tk.DoubleVar(value=0.25)

        # State
        grid_size = self.triple_grid_size.get()
        self.triple_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.triple_start = (2, 2)
        self.triple_end = (grid_size-3, grid_size-3)
        self.triple_grid[self.triple_start[0]][self.triple_start[1]] = 2
        self.triple_grid[self.triple_end[0]][self.triple_end[1]] = 3
        self.triple_visited = {'Dijkstra': set(), 'A*': set(), 'Greedy': set()}
        self.triple_path = {'Dijkstra': [], 'A*': [], 'Greedy': []}
        self.triple_running = False
        self.triple_paused = False
        self.triple_finished = {'Dijkstra': False, 'A*': False, 'Greedy': False}
        self.triple_dragging = None
        self.triple_visualizers = {}
        self.triple_speed = tk.IntVar(value=1)

        # Layout
        main = tk.Frame(tab)
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(main, text="Side-by-Side Algorithm Comparison", font=("Arial", 16, "bold")).pack(pady=10)

        # Three canvases
        canvas_frame = tk.Frame(main)
        canvas_frame.pack()

        self.triple_canvases = {}
        self.triple_stats_labels = {}

        algorithms = ['Dijkstra', 'A*', 'Greedy']
        colors = ['#1976D2', '#388E3C', '#9C27B0']

        for i, (algo, color) in enumerate(zip(algorithms, colors)):
            panel = tk.Frame(canvas_frame, relief=tk.RIDGE, borderwidth=2)
            panel.grid(row=0, column=i, padx=5, pady=5)

            tk.Label(panel, text=algo, font=("Arial", 14, "bold"), bg=color, fg="white", pady=5).pack(fill=tk.X)

            # Fixed canvas size - cells will scale based on grid size
            canvas = tk.Canvas(panel, width=540, height=540, bg="white", highlightthickness=0)
            canvas.pack(padx=5, pady=5)
            self.triple_canvases[algo] = canvas
            canvas.bind("<Button-1>", self.triple_mouse_down)
            canvas.bind("<B1-Motion>", self.triple_mouse_drag)
            canvas.bind("<ButtonRelease-1>", self.triple_mouse_up)

            stats = tk.Label(panel, text="Ready", font=("Courier", 9), height=6, justify=tk.LEFT, wraplength=150)
            stats.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            self.triple_stats_labels[algo] = stats

        # Controls
        controls = tk.Frame(main)
        controls.pack(pady=10)

        tk.Label(controls, text="Grid Size:", font=("Arial", 9)).pack(side=tk.LEFT, padx=2)
        tk.Scale(controls, from_=20, to=80, resolution=10, orient=tk.HORIZONTAL,
                variable=self.triple_grid_size, length=100).pack(side=tk.LEFT, padx=2)

        tk.Label(controls, text="Density:", font=("Arial", 9)).pack(side=tk.LEFT, padx=2)
        tk.Scale(controls, from_=0.0, to=0.7, resolution=0.05, orient=tk.HORIZONTAL,
                variable=self.triple_density, length=100).pack(side=tk.LEFT, padx=2)

        tk.Label(controls, text="Speed:", font=("Arial", 9)).pack(side=tk.LEFT, padx=2)
        tk.Scale(controls, from_=1, to=50, resolution=1, orient=tk.HORIZONTAL,
                variable=self.triple_speed, length=80).pack(side=tk.LEFT, padx=2)

        tk.Button(controls, text="Run All Algorithms", command=self.run_triple,
                 bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20, height=2).pack(side=tk.LEFT, padx=5)

        self.triple_pause_btn = tk.Button(controls, text="Pause", command=self.toggle_triple_pause,
                                          bg="#FFC107", fg="black", font=("Arial", 11, "bold"), width=8, state="disabled")
        self.triple_pause_btn.pack(side=tk.LEFT, padx=2)

        tk.Button(controls, text="Stop", command=self.stop_triple,
                 bg="#D32F2F", fg="white", font=("Arial", 11, "bold"), width=8).pack(side=tk.LEFT, padx=2)

        tk.Button(controls, text="Reset", command=self.reset_triple,
                 bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(controls, text="New Map", command=self.regen_triple,
                 bg="#FF9800", fg="white", font=("Arial", 12, "bold"), width=12).pack(side=tk.LEFT, padx=5)

        self.generate_triple_obstacles()
        self.draw_triple_grids()

    def generate_triple_obstacles(self):
        grid_size = self.triple_grid_size.get()
        for i in range(grid_size):
            for j in range(grid_size):
                if (i, j) == self.triple_start or (i, j) == self.triple_end:
                    continue
                if random.random() < self.triple_density.get():
                    self.triple_grid[i][j] = 1

    def draw_triple_grid(self, canvas, algo):
        canvas.delete("all")
        visited = self.triple_visited[algo]
        path = self.triple_path[algo]
        grid_size = self.triple_grid_size.get()
        cell_size = 540 // grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                if (i, j) == self.triple_start:
                    color = "#4CAF50"
                elif (i, j) == self.triple_end:
                    color = "#F44336"
                elif (i, j) in path:
                    color = "#FFD700"
                elif (i, j) in visited:
                    color = "#BBDEFB"
                elif self.triple_grid[i][j] == 1:
                    color = "#424242"
                else:
                    color = "white"
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#E0E0E0")

    def draw_triple_grids(self):
        for algo, canvas in self.triple_canvases.items():
            self.draw_triple_grid(canvas, algo)

    def run_triple(self):
        if self.triple_running:
            return
        self.triple_running = True
        self.triple_paused = False
        self.triple_visited = {'Dijkstra': set(), 'A*': set(), 'Greedy': set()}
        self.triple_path = {'Dijkstra': [], 'A*': [], 'Greedy': []}
        self.triple_finished = {'Dijkstra': False, 'A*': False, 'Greedy': False}

        # Show "Computing..." message
        for label in self.triple_stats_labels.values():
            label.config(text="Computing...")
        self.root.update()

        # Run algorithms to completion FIRST (get true performance data)
        self.triple_execution_history = {}
        self.triple_stats = {}

        for algo_name in ['Dijkstra', 'A*', 'Greedy']:
            if algo_name == 'Dijkstra':
                viz = DijkstraVisualizer(self.triple_grid, self.triple_start, self.triple_end)
            elif algo_name == 'A*':
                viz = AStarVisualizer(self.triple_grid, self.triple_start, self.triple_end)
            else:
                viz = GreedyVisualizer(self.triple_grid, self.triple_start, self.triple_end)

            # Record execution history (every visited cell in order)
            history = []
            while viz.step():
                history.append(viz.get_visited().copy())

            # Get final state
            history.append(viz.get_visited().copy())
            self.triple_execution_history[algo_name] = history
            self.triple_path[algo_name] = viz.get_path()
            self.triple_stats[algo_name] = viz.get_stats()

        # Store paths separately for showing at end
        self.triple_final_paths = self.triple_path.copy()

        # Clear paths for replay (will restore when each finishes)
        self.triple_path = {'Dijkstra': [], 'A*': [], 'Greedy': []}

        # Now replay the execution as animation
        self.triple_replay_index = 0
        self.triple_pause_btn.config(state="normal")
        for algo_name, stats in self.triple_stats.items():
            text = f"✓ DONE\nNodes: {stats['nodes_explored']}\nPath: {stats['path_length']}\nTime: {stats['time_ms']:.3f}ms"
            self.triple_stats_labels[algo_name].config(text=text)
        self.animate_triple_replay()

    def animate_triple_replay(self):
        """Replay pre-computed algorithm execution"""
        # Check if stopped
        if not self.triple_running:
            return

        if self.triple_paused:
            self.root.after(10, self.animate_triple_replay)
            return

        speed = self.triple_speed.get()

        # Advance replay by 'speed' steps
        self.triple_replay_index += speed

        # Update visited sets for each algorithm based on replay index
        for algo_name, history in self.triple_execution_history.items():
            if self.triple_replay_index < len(history):
                self.triple_visited[algo_name] = history[self.triple_replay_index]
                self.triple_finished[algo_name] = False
                # Keep path hidden during replay
                self.triple_path[algo_name] = []
            else:
                # Algorithm finished replay - NOW show final state with path
                self.triple_visited[algo_name] = history[-1]
                self.triple_finished[algo_name] = True
                # Restore the path for this algorithm
                self.triple_path[algo_name] = self.triple_final_paths[algo_name]

        self.draw_triple_grids()

        # Check if all algorithms have finished replay
        max_history_length = max(len(h) for h in self.triple_execution_history.values())
        if self.triple_replay_index >= max_history_length:
            self.triple_running = False
            self.triple_paused = False
            self.triple_pause_btn.config(state="disabled", text="Pause")
            return

        # Continue replay
        delay = 10
        self.root.after(delay, self.animate_triple_replay)

    def toggle_triple_pause(self):
        """Toggle pause/resume for triple view"""
        self.triple_paused = not self.triple_paused
        if self.triple_paused:
            self.triple_pause_btn.config(text="Resume", bg="#4CAF50")
        else:
            self.triple_pause_btn.config(text="Pause", bg="#FFC107")

    def stop_triple(self):
        """Stop all algorithms"""
        if self.triple_running or self.triple_paused:
            self.triple_running = False
            self.triple_paused = False
            self.triple_pause_btn.config(state="disabled", text="Pause")
            self.triple_visited = {'Dijkstra': set(), 'A*': set(), 'Greedy': set()}
            self.triple_path = {'Dijkstra': [], 'A*': [], 'Greedy': []}
            for label in self.triple_stats_labels.values():
                label.config(text="⏹ STOPPED")
            self.draw_triple_grids()

    def reset_triple(self):
        self.triple_visited = {'Dijkstra': set(), 'A*': set(), 'Greedy': set()}
        self.triple_path = {'Dijkstra': [], 'A*': [], 'Greedy': []}
        self.triple_running = False
        self.triple_paused = False
        self.triple_pause_btn.config(state="disabled", text="Pause")
        for label in self.triple_stats_labels.values():
            label.config(text="Ready")
        self.draw_triple_grids()

    def regen_triple(self):
        if self.triple_running:
            return
        # Regenerate grid with new size
        grid_size = self.triple_grid_size.get()
        self.triple_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.triple_start = (2, 2)
        self.triple_end = (grid_size-3, grid_size-3)
        self.triple_grid[self.triple_start[0]][self.triple_start[1]] = 2
        self.triple_grid[self.triple_end[0]][self.triple_end[1]] = 3
        self.generate_triple_obstacles()
        self.reset_triple()

    def triple_mouse_down(self, event):
        if self.triple_running:
            return
        grid_size = self.triple_grid_size.get()
        cell_size = 540 // grid_size
        cell = self.get_cell(event.x, event.y, cell_size, grid_size)
        if cell and cell == self.triple_start:
            self.triple_dragging = 'start'
        elif cell and cell == self.triple_end:
            self.triple_dragging = 'end'

    def triple_mouse_drag(self, event):
        if not self.triple_dragging:
            return
        grid_size = self.triple_grid_size.get()
        cell_size = 540 // grid_size
        cell = self.get_cell(event.x, event.y, cell_size, grid_size)
        if not cell or self.triple_grid[cell[0]][cell[1]] == 1:
            return
        if self.triple_dragging == 'start' and cell != self.triple_end:
            self.triple_grid[self.triple_start[0]][self.triple_start[1]] = 0
            self.triple_start = cell
            self.triple_grid[cell[0]][cell[1]] = 2
        elif self.triple_dragging == 'end' and cell != self.triple_start:
            self.triple_grid[self.triple_end[0]][self.triple_end[1]] = 0
            self.triple_end = cell
            self.triple_grid[cell[0]][cell[1]] = 3
        self.triple_visited = {'Dijkstra': set(), 'A*': set(), 'Greedy': set()}
        self.triple_path = {'Dijkstra': [], 'A*': [], 'Greedy': []}
        self.draw_triple_grids()

    def triple_mouse_up(self, event):
        self.triple_dragging = None

    # ==================== TAB 3: BATCH TESTING ====================
    def setup_batch_test_tab(self):
        """Batch testing and analysis"""
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Batch Testing")

        # Main container
        main = tk.Frame(tab)
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Title
        title_frame = tk.Frame(main)
        title_frame.pack(fill=tk.X, pady=(0, 15))
        tk.Label(title_frame, text="Batch Testing & Analysis", font=("Arial", 18, "bold")).pack(side=tk.LEFT)
        tk.Label(title_frame, text="Run multiple algorithm tests and analyze results", font=("Arial", 10, "italic"), fg="#666").pack(side=tk.LEFT, padx=10)

        # Left: Test selection
        left_panel = tk.Frame(main)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))

        tk.Label(left_panel, text="STEP 1: Choose Test Size", font=("Arial", 12, "bold"), fg="#333").pack(anchor=tk.W, pady=(0, 10))

        # Test options with descriptions
        test_options = [
            ("Quick Test\n✓ Fast (5 min)\n✓ Small dataset\n✓ Good for testing",
             self.run_quick_test, "#4CAF50"),
            ("Medium Test\n✓ Moderate (30 min)\n✓ Decent data\n✓ Good balance",
             self.run_medium_test, "#2196F3"),
            ("Full Test\n✓ Complete (1-2 hrs)\n✓ Large dataset\n✓ Best accuracy",
             self.run_full_test, "#D32F2F")
        ]

        for text, cmd, color in test_options:
            tk.Button(left_panel, text=text, command=cmd, bg=color, fg="white",
                     font=("Arial", 10, "bold"), width=24, height=5, justify=tk.LEFT).pack(pady=5, fill=tk.X)

        tk.Label(left_panel, text="", height=2).pack()  # Spacer

        tk.Label(left_panel, text="STEP 2: Analyze & Visualize", font=("Arial", 12, "bold"), fg="#333").pack(anchor=tk.W, pady=(0, 10))

        tk.Button(left_panel, text="📊 Analyze Results", command=self.analyze_results,
                 bg="#9C27B0", fg="white", font=("Arial", 11, "bold"), width=24).pack(pady=5, fill=tk.X)
        tk.Button(left_panel, text="📈 Generate Graphs", command=self.generate_graphs,
                 bg="#FF9800", fg="white", font=("Arial", 11, "bold"), width=24).pack(pady=5, fill=tk.X)

        # Right: Progress and results
        right_panel = tk.Frame(main)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(right_panel, text="Progress & Results", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))

        # Progress bar with label
        progress_frame = tk.Frame(right_panel)
        progress_frame.pack(fill=tk.X, pady=(0, 5))

        self.batch_progress_label = tk.Label(progress_frame, text="Ready to run tests", font=("Arial", 11, "bold"))
        self.batch_progress_label.pack(anchor=tk.W)

        self.batch_progress_var = tk.DoubleVar()
        self.batch_progress = ttk.Progressbar(progress_frame, variable=self.batch_progress_var, maximum=100, length=400, mode='determinate')
        self.batch_progress.pack(fill=tk.X, pady=5)

        # Log
        log_label = tk.Label(right_panel, text="Log Output", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 5))
        self.batch_log = scrolledtext.ScrolledText(right_panel, height=25, font=("Courier", 9), wrap=tk.WORD)
        self.batch_log.pack(fill=tk.BOTH, expand=True)

        # Initial message
        self.batch_log_msg("Welcome to Batch Testing!")
        self.batch_log_msg("Choose a test size on the left to begin.")
        self.batch_log_msg("")
        self.batch_log_msg("Quick Test: Best for quick validation (5 min)")
        self.batch_log_msg("Medium Test: Good balance of speed and data (30 min)")
        self.batch_log_msg("Full Test: Complete dataset for essay (1-2 hours)")
        self.batch_log_msg("")
        self.batch_log_msg("After testing, use 'Analyze Results' and 'Generate Graphs'.")

    def batch_log_msg(self, msg):
        self.batch_log.insert(tk.END, msg + "\n")
        self.batch_log.see(tk.END)
        self.root.update()

    def batch_progress_update(self, current, total):
        progress = (current / total) * 100
        self.batch_progress_var.set(progress)
        self.batch_progress_label.config(text=f"Testing: {current}/{total} ({progress:.1f}%)")
        self.root.update()

    def run_quick_test(self):
        if not messagebox.askyesno("Confirm", "Run Quick Test (360 trials, ~5 min)?"):
            return
        self.batch_log.delete(1.0, tk.END)
        self.batch_log_msg("Starting Quick Test...")

        def run():
            try:
                results = self.batch_tester.run_test_suite(
                    map_sizes=[50, 100],
                    obstacle_densities=[0.1, 0.25, 0.4],
                    map_types=['random', 'clustered'],
                    trials_per_config=10,
                    progress_callback=self.batch_progress_update
                )
                self.current_results_file = results
                self.batch_log_msg(f"\n✓ Test complete! Results: {results}")
                messagebox.showinfo("Success", f"Quick test complete!\n\n{results}")
            except Exception as e:
                self.batch_log_msg(f"\n✗ Error: {e}")
                messagebox.showerror("Error", str(e))

        threading.Thread(target=run, daemon=True).start()

    def run_medium_test(self):
        if not messagebox.askyesno("Confirm", "Run Medium Test (3,000 trials, ~30 min)?"):
            return
        self.batch_log.delete(1.0, tk.END)
        self.batch_log_msg("Starting Medium Test...")

        def run():
            try:
                results = self.batch_tester.run_test_suite(
                    map_sizes=[50, 100, 200],
                    obstacle_densities=[0.1, 0.25, 0.4, 0.55],
                    map_types=['random', 'clustered', 'maze', 'mixed'],
                    trials_per_config=25,
                    progress_callback=self.batch_progress_update
                )
                self.current_results_file = results
                self.batch_log_msg(f"\n✓ Test complete! Results: {results}")
                messagebox.showinfo("Success", f"Medium test complete!\n\n{results}")
            except Exception as e:
                self.batch_log_msg(f"\n✗ Error: {e}")
                messagebox.showerror("Error", str(e))

        threading.Thread(target=run, daemon=True).start()

    def run_full_test(self):
        if not messagebox.askyesno("Confirm", "Run Full Test (30,000+ trials, 1-2 hrs)?\n\nThis will take a long time!"):
            return
        self.batch_log.delete(1.0, tk.END)
        self.batch_log_msg("Starting Full Test (30,000+ trials)...")

        def run():
            try:
                results = self.batch_tester.run_full_test(progress_callback=self.batch_progress_update)
                self.current_results_file = results
                self.batch_log_msg(f"\n✓ Test complete! Results: {results}")
                messagebox.showinfo("Success", f"Full test complete!\n\n{results}")
            except Exception as e:
                self.batch_log_msg(f"\n✗ Error: {e}")
                messagebox.showerror("Error", str(e))

        threading.Thread(target=run, daemon=True).start()

    def analyze_results(self):
        if not self.current_results_file:
            messagebox.showwarning("No Results", "Run a test first!")
            return
        try:
            analyzer = StatisticalAnalyzer(self.current_results_file)
            report = analyzer.generate_full_report(
                os.path.join("data/analysis", f"report_{os.path.basename(self.current_results_file)}.txt")
            )
            self.batch_log.delete(1.0, tk.END)
            self.batch_log.insert(1.0, report)
            messagebox.showinfo("Success", "Analysis complete! Check data/analysis/ folder.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_graphs(self):
        if not self.current_results_file:
            messagebox.showwarning("No Results", "Run a test first!")
            return
        try:
            generator = GraphGenerator(self.current_results_file)
            generator.generate_all_graphs()
            summary = generator.generate_summary_report()
            self.batch_log.delete(1.0, tk.END)
            self.batch_log.insert(1.0, summary)
            messagebox.showinfo("Success", "Graphs generated! Check graphs/ folder.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ==================== HELPER ====================
    def get_cell(self, x, y, cell_size, grid_size):
        col, row = x // cell_size, y // cell_size
        if 0 <= row < grid_size and 0 <= col < grid_size:
            return (row, col)
        return None


def main():
    root = tk.Tk()
    app = UnifiedPathfindingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
