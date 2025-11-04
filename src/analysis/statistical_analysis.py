"""
Statistical Analysis Module
Performs ANOVA, effect size calculations, and hypothesis testing
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import f_oneway
import os

class StatisticalAnalyzer:
    """Performs statistical analysis on pathfinding algorithm data"""

    def __init__(self, results_file):
        """
        Initialize analyzer

        Args:
            results_file: Path to CSV file with results
        """
        self.results_file = results_file
        self.df = pd.read_csv(results_file)

    def get_summary_statistics(self):
        """
        Calculate summary statistics for each algorithm

        Returns:
            DataFrame with summary statistics
        """
        summary = self.df.groupby('algorithm').agg({
            'nodes_explored': ['mean', 'std', 'min', 'max'],
            'path_length': ['mean', 'std', 'min', 'max'],
            'time_ms': ['mean', 'std', 'min', 'max']
        }).round(3)

        return summary

    def perform_anova(self, metric='time_ms'):
        """
        Perform one-way ANOVA test

        Args:
            metric: Metric to test ('time_ms', 'nodes_explored', 'path_length')

        Returns:
            Dictionary with ANOVA results
        """
        # Get data for each algorithm
        groups = []
        for algo in self.df['algorithm'].unique():
            group_data = self.df[self.df['algorithm'] == algo][metric].values
            groups.append(group_data)

        # Perform ANOVA
        f_statistic, p_value = f_oneway(*groups)

        # Calculate effect size (eta-squared)
        # η² = SS_between / SS_total
        grand_mean = self.df[metric].mean()
        ss_total = np.sum((self.df[metric] - grand_mean) ** 2)

        ss_between = 0
        for algo in self.df['algorithm'].unique():
            group_data = self.df[self.df['algorithm'] == algo][metric].values
            group_mean = group_data.mean()
            ss_between += len(group_data) * (group_mean - grand_mean) ** 2

        eta_squared = ss_between / ss_total if ss_total > 0 else 0

        return {
            'metric': metric,
            'f_statistic': f_statistic,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'eta_squared': eta_squared,
            'effect_size_interpretation': self._interpret_effect_size(eta_squared)
        }

    def _interpret_effect_size(self, eta_squared):
        """Interpret effect size based on Cohen's guidelines"""
        if eta_squared < 0.01:
            return "negligible"
        elif eta_squared < 0.06:
            return "small"
        elif eta_squared < 0.14:
            return "medium"
        else:
            return "large"

    def perform_posthoc_tests(self, metric='time_ms'):
        """
        Perform pairwise t-tests between algorithms (Bonferroni corrected)

        Args:
            metric: Metric to test

        Returns:
            DataFrame with pairwise comparison results
        """
        algorithms = self.df['algorithm'].unique()
        results = []

        # Number of comparisons for Bonferroni correction
        n_comparisons = len(algorithms) * (len(algorithms) - 1) / 2
        alpha = 0.05 / n_comparisons  # Bonferroni correction

        for i, algo1 in enumerate(algorithms):
            for algo2 in algorithms[i+1:]:
                data1 = self.df[self.df['algorithm'] == algo1][metric].values
                data2 = self.df[self.df['algorithm'] == algo2][metric].values

                # Perform independent t-test
                t_stat, p_value = stats.ttest_ind(data1, data2)

                # Calculate Cohen's d (effect size)
                mean_diff = data1.mean() - data2.mean()
                pooled_std = np.sqrt((data1.std()**2 + data2.std()**2) / 2)
                cohens_d = mean_diff / pooled_std if pooled_std > 0 else 0

                # Percent difference
                percent_diff = ((data1.mean() - data2.mean()) / data2.mean() * 100) if data2.mean() != 0 else 0

                results.append({
                    'comparison': f"{algo1} vs {algo2}",
                    'mean_diff': mean_diff,
                    'percent_diff': percent_diff,
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'significant': p_value < alpha,
                    'cohens_d': cohens_d,
                    'effect_size': self._interpret_cohens_d(cohens_d)
                })

        return pd.DataFrame(results)

    def _interpret_cohens_d(self, d):
        """Interpret Cohen's d effect size"""
        d_abs = abs(d)
        if d_abs < 0.2:
            return "negligible"
        elif d_abs < 0.5:
            return "small"
        elif d_abs < 0.8:
            return "medium"
        else:
            return "large"

    def analyze_by_condition(self, metric='time_ms'):
        """
        Analyze performance by different conditions

        Args:
            metric: Metric to analyze

        Returns:
            Dictionary with analysis by condition
        """
        results = {}

        # By obstacle density
        results['by_density'] = self.df.groupby(['algorithm', 'obstacle_density'])[metric].agg(['mean', 'std']).round(3)

        # By map size
        results['by_map_size'] = self.df.groupby(['algorithm', 'map_size'])[metric].agg(['mean', 'std']).round(3)

        # By map type
        results['by_map_type'] = self.df.groupby(['algorithm', 'map_type'])[metric].agg(['mean', 'std']).round(3)

        return results

    def calculate_confidence_intervals(self, confidence=0.95, metric='time_ms'):
        """
        Calculate confidence intervals for each algorithm

        Args:
            confidence: Confidence level (default 0.95)
            metric: Metric to analyze

        Returns:
            DataFrame with confidence intervals
        """
        results = []

        for algo in self.df['algorithm'].unique():
            data = self.df[self.df['algorithm'] == algo][metric].values

            mean = data.mean()
            std_err = stats.sem(data)
            ci = stats.t.interval(confidence, len(data) - 1, mean, std_err)

            results.append({
                'algorithm': algo,
                'mean': mean,
                'std_error': std_err,
                'ci_lower': ci[0],
                'ci_upper': ci[1],
                'ci_range': ci[1] - ci[0]
            })

        return pd.DataFrame(results)

    def generate_full_report(self, output_file=None):
        """
        Generate comprehensive statistical report

        Args:
            output_file: Optional path to save report

        Returns:
            String with full report
        """
        report = []
        report.append("=" * 80)
        report.append("STATISTICAL ANALYSIS REPORT")
        report.append("Pathfinding Algorithm Comparison")
        report.append("=" * 80)
        report.append("")

        # Summary statistics
        report.append("SUMMARY STATISTICS")
        report.append("-" * 80)
        report.append(str(self.get_summary_statistics()))
        report.append("")

        # ANOVA for each metric
        for metric in ['time_ms', 'nodes_explored', 'path_length']:
            report.append(f"\nANOVA TEST - {metric.upper()}")
            report.append("-" * 80)
            anova_results = self.perform_anova(metric)
            report.append(f"F-statistic: {anova_results['f_statistic']:.4f}")
            report.append(f"p-value: {anova_results['p_value']:.6f}")
            report.append(f"Significant: {'YES' if anova_results['significant'] else 'NO'}")
            report.append(f"Effect size (η²): {anova_results['eta_squared']:.4f} ({anova_results['effect_size_interpretation']})")
            report.append("")

            # Post-hoc tests
            report.append(f"POST-HOC TESTS - {metric.upper()}")
            report.append("-" * 80)
            posthoc = self.perform_posthoc_tests(metric)
            report.append(str(posthoc.to_string(index=False)))
            report.append("")

        # Confidence intervals
        report.append("\nCONFIDENCE INTERVALS (95%)")
        report.append("-" * 80)
        ci = self.calculate_confidence_intervals()
        report.append(str(ci.to_string(index=False)))
        report.append("")

        report_text = "\n".join(report)

        # Save to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_text)

        return report_text

    def get_performance_comparison(self, baseline='Dijkstra'):
        """
        Calculate performance improvements relative to baseline

        Args:
            baseline: Algorithm to use as baseline

        Returns:
            DataFrame with performance comparisons
        """
        baseline_data = self.df[self.df['algorithm'] == baseline]

        results = []

        for algo in self.df['algorithm'].unique():
            if algo == baseline:
                continue

            algo_data = self.df[self.df['algorithm'] == algo]

            for metric in ['time_ms', 'nodes_explored']:
                baseline_mean = baseline_data[metric].mean()
                algo_mean = algo_data[metric].mean()

                improvement = ((baseline_mean - algo_mean) / baseline_mean * 100) if baseline_mean != 0 else 0

                results.append({
                    'algorithm': algo,
                    'metric': metric,
                    'baseline_mean': baseline_mean,
                    'algorithm_mean': algo_mean,
                    'improvement_percent': improvement
                })

        return pd.DataFrame(results)
