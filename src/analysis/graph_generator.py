"""
Graph Generator
Creates publication-quality graphs for Extended Essay
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import pandas as pd
import numpy as np
import seaborn as sns
import os

# Set style for academic papers
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10

class GraphGenerator:
    """Generates publication-quality graphs for Extended Essay"""

    def __init__(self, results_file, output_dir="graphs"):
        """
        Initialize graph generator

        Args:
            results_file: Path to CSV results file
            output_dir: Directory to save graphs
        """
        self.df = pd.read_csv(results_file)
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_all_graphs(self):
        """Generate all graphs for Extended Essay"""
        self.plot_execution_time_comparison()
        self.plot_nodes_explored_comparison()
        self.plot_density_impact()
        self.plot_map_size_scaling()
        self.plot_map_type_comparison()
        self.plot_algorithm_efficiency()
        self.plot_combined_metrics()
        self.plot_performance_improvement()

    def plot_execution_time_comparison(self):
        """Bar chart comparing average execution times"""
        fig, ax = plt.subplots(figsize=(10, 6))

        data = self.df.groupby('algorithm')['time_ms'].mean().sort_values()

        colors = ['#1976D2', '#388E3C', '#D32F2F']
        bars = ax.bar(data.index, data.values, color=colors, alpha=0.8, edgecolor='black')

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f} ms',
                   ha='center', va='bottom', fontweight='bold')

        ax.set_ylabel('Average Execution Time (ms)', fontweight='bold')
        ax.set_xlabel('Algorithm', fontweight='bold')
        ax.set_title('Algorithm Execution Time Comparison', fontweight='bold', fontsize=14)
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'execution_time_comparison.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def plot_nodes_explored_comparison(self):
        """Bar chart comparing nodes explored"""
        fig, ax = plt.subplots(figsize=(10, 6))

        data = self.df.groupby('algorithm')['nodes_explored'].mean().sort_values()

        colors = ['#1976D2', '#388E3C', '#D32F2F']
        bars = ax.bar(data.index, data.values, color=colors, alpha=0.8, edgecolor='black')

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold')

        ax.set_ylabel('Average Nodes Explored', fontweight='bold')
        ax.set_xlabel('Algorithm', fontweight='bold')
        ax.set_title('Algorithm Search Space Comparison', fontweight='bold', fontsize=14)
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'nodes_explored_comparison.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def plot_density_impact(self):
        """Line plot showing impact of obstacle density"""
        fig, ax = plt.subplots(figsize=(12, 6))

        for algo in self.df['algorithm'].unique():
            algo_data = self.df[self.df['algorithm'] == algo]
            density_means = algo_data.groupby('obstacle_density')['time_ms'].mean()

            ax.plot(density_means.index, density_means.values,
                   marker='o', linewidth=2, markersize=8, label=algo)

        ax.set_xlabel('Obstacle Density', fontweight='bold')
        ax.set_ylabel('Average Execution Time (ms)', fontweight='bold')
        ax.set_title('Impact of Obstacle Density on Algorithm Performance', fontweight='bold', fontsize=14)
        ax.legend(frameon=True, shadow=True)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'density_impact.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def plot_map_size_scaling(self):
        """Log-log plot showing algorithm scaling"""
        fig, ax = plt.subplots(figsize=(12, 6))

        for algo in self.df['algorithm'].unique():
            algo_data = self.df[self.df['algorithm'] == algo]
            size_means = algo_data.groupby('map_size')['time_ms'].mean()

            ax.loglog(size_means.index, size_means.values,
                     marker='s', linewidth=2, markersize=8, label=algo)

        ax.set_xlabel('Map Size (cells per side)', fontweight='bold')
        ax.set_ylabel('Average Execution Time (ms)', fontweight='bold')
        ax.set_title('Algorithm Scaling with Map Size (Log-Log)', fontweight='bold', fontsize=14)
        ax.legend(frameon=True, shadow=True)
        ax.grid(True, alpha=0.3, which='both')

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'map_size_scaling.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def plot_map_type_comparison(self):
        """Grouped bar chart by map type"""
        fig, ax = plt.subplots(figsize=(12, 6))

        map_types = self.df['map_type'].unique()
        algorithms = self.df['algorithm'].unique()

        x = np.arange(len(map_types))
        width = 0.25

        for i, algo in enumerate(algorithms):
            means = []
            for map_type in map_types:
                data = self.df[(self.df['algorithm'] == algo) & (self.df['map_type'] == map_type)]
                means.append(data['time_ms'].mean())

            ax.bar(x + i*width, means, width, label=algo, alpha=0.8, edgecolor='black')

        ax.set_xlabel('Map Type', fontweight='bold')
        ax.set_ylabel('Average Execution Time (ms)', fontweight='bold')
        ax.set_title('Algorithm Performance by Map Type', fontweight='bold', fontsize=14)
        ax.set_xticks(x + width)
        ax.set_xticklabels(map_types)
        ax.legend(frameon=True, shadow=True)
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'map_type_comparison.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def plot_algorithm_efficiency(self):
        """Scatter plot: execution time vs nodes explored"""
        fig, ax = plt.subplots(figsize=(10, 8))

        colors = {'Dijkstra': '#1976D2', 'A*': '#388E3C', 'Greedy': '#9C27B0'}

        for algo in self.df['algorithm'].unique():
            algo_data = self.df[self.df['algorithm'] == algo]
            ax.scatter(algo_data['nodes_explored'], algo_data['time_ms'],
                      c=colors[algo], label=algo, alpha=0.6, s=30, edgecolor='black', linewidth=0.5)

        ax.set_xlabel('Nodes Explored', fontweight='bold')
        ax.set_ylabel('Execution Time (ms)', fontweight='bold')
        ax.set_title('Algorithm Efficiency: Time vs Search Space', fontweight='bold', fontsize=14)
        ax.legend(frameon=True, shadow=True)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'algorithm_efficiency.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def plot_combined_metrics(self):
        """Combined subplot showing multiple metrics"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # Time comparison
        data = self.df.groupby('algorithm')['time_ms'].mean()
        axes[0, 0].bar(data.index, data.values, color=['#1976D2', '#388E3C', '#D32F2F'], alpha=0.8, edgecolor='black')
        axes[0, 0].set_title('Execution Time', fontweight='bold')
        axes[0, 0].set_ylabel('Time (ms)', fontweight='bold')
        axes[0, 0].grid(axis='y', alpha=0.3)

        # Nodes explored
        data = self.df.groupby('algorithm')['nodes_explored'].mean()
        axes[0, 1].bar(data.index, data.values, color=['#1976D2', '#388E3C', '#D32F2F'], alpha=0.8, edgecolor='black')
        axes[0, 1].set_title('Nodes Explored', fontweight='bold')
        axes[0, 1].set_ylabel('Nodes', fontweight='bold')
        axes[0, 1].grid(axis='y', alpha=0.3)

        # Density impact
        for algo in self.df['algorithm'].unique():
            algo_data = self.df[self.df['algorithm'] == algo]
            density_means = algo_data.groupby('obstacle_density')['time_ms'].mean()
            axes[1, 0].plot(density_means.index, density_means.values, marker='o', label=algo, linewidth=2)
        axes[1, 0].set_title('Density Impact', fontweight='bold')
        axes[1, 0].set_xlabel('Obstacle Density', fontweight='bold')
        axes[1, 0].set_ylabel('Time (ms)', fontweight='bold')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)

        # Map size scaling
        for algo in self.df['algorithm'].unique():
            algo_data = self.df[self.df['algorithm'] == algo]
            size_means = algo_data.groupby('map_size')['time_ms'].mean()
            axes[1, 1].plot(size_means.index, size_means.values, marker='s', label=algo, linewidth=2)
        axes[1, 1].set_title('Map Size Scaling', fontweight='bold')
        axes[1, 1].set_xlabel('Map Size', fontweight='bold')
        axes[1, 1].set_ylabel('Time (ms)', fontweight='bold')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)

        plt.suptitle('Comprehensive Algorithm Comparison', fontsize=16, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'combined_metrics.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def plot_performance_improvement(self):
        """Bar chart showing performance improvement over Dijkstra"""
        fig, ax = plt.subplots(figsize=(10, 6))

        dijkstra_mean = self.df[self.df['algorithm'] == 'Dijkstra']['time_ms'].mean()

        improvements = []
        algos = []

        for algo in ['A*', 'Greedy']:
            algo_mean = self.df[self.df['algorithm'] == algo]['time_ms'].mean()
            improvement = ((dijkstra_mean - algo_mean) / dijkstra_mean) * 100
            improvements.append(improvement)
            algos.append(algo)

        colors = ['#388E3C', '#D32F2F']
        bars = ax.bar(algos, improvements, color=colors, alpha=0.8, edgecolor='black')

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'+{height:.1f}%',
                   ha='center', va='bottom', fontweight='bold', fontsize=12)

        ax.set_ylabel('Performance Improvement (%)', fontweight='bold')
        ax.set_xlabel('Algorithm', fontweight='bold')
        ax.set_title('Performance Improvement Relative to Dijkstra', fontweight='bold', fontsize=14)
        ax.grid(axis='y', alpha=0.3)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'performance_improvement.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def generate_summary_report(self):
        """Generate text summary of graph insights"""
        report = []
        report.append("GRAPH GENERATION SUMMARY")
        report.append("=" * 80)
        report.append("")

        # Calculate key statistics
        dijkstra_time = self.df[self.df['algorithm'] == 'Dijkstra']['time_ms'].mean()
        astar_time = self.df[self.df['algorithm'] == 'A*']['time_ms'].mean()
        greedy_time = self.df[self.df['algorithm'] == 'Greedy']['time_ms'].mean()

        astar_improvement = ((dijkstra_time - astar_time) / dijkstra_time) * 100
        greedy_improvement = ((dijkstra_time - greedy_time) / dijkstra_time) * 100

        report.append("KEY FINDINGS:")
        report.append(f"  - A* is {astar_improvement:.1f}% faster than Dijkstra")
        report.append(f"  - Greedy is {greedy_improvement:.1f}% faster than Dijkstra")
        report.append("")

        report.append("GRAPHS GENERATED:")
        report.append("  1. execution_time_comparison.png - Bar chart of average execution times")
        report.append("  2. nodes_explored_comparison.png - Bar chart of search space size")
        report.append("  3. density_impact.png - Line plot showing density effects")
        report.append("  4. map_size_scaling.png - Log-log plot of scalability")
        report.append("  5. map_type_comparison.png - Performance across map types")
        report.append("  6. algorithm_efficiency.png - Scatter plot of efficiency")
        report.append("  7. combined_metrics.png - 4-panel comprehensive view")
        report.append("  8. performance_improvement.png - Improvement percentages")
        report.append("")

        return "\n".join(report)
