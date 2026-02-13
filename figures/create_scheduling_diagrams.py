#!/usr/bin/env python3
"""
Generate scheduling diagrams for AI/ML Integration in RTOS Report
- Figure 1: Traditional RTOS Task Scheduling (predictable execution)
- Figure 2: ML-enabled RTOS with Temporal Partitioning
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np
import os

def create_figure1_traditional_scheduling():
    """
    Figure 1: Traditional RTOS Task Scheduling
    Shows predictable, consistent execution times for traditional tasks
    
    Side effects:
        Creates figure1_traditional_vs_ml_scheduling.pdf and .png in the script directory
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
    
    # Traditional RTOS Task Execution (Top)
    ax1.set_xlim(0, 20)
    ax1.set_ylim(0, 3)
    ax1.set_xlabel('Time (ms)', fontsize=11)
    ax1.set_title('Traditional RTOS Task Scheduling', fontsize=13, fontweight='bold')
    ax1.set_yticks([0.5, 1.5, 2.5])
    ax1.set_yticklabels(['Task 3\n(Low)', 'Task 2\n(Medium)', 'Task 1\n(High)'])
    ax1.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Task 1 (High Priority) - Red, consistent execution
    task1_times = [0, 5, 10, 15]
    task1_duration = 2
    for t in task1_times:
        rect = FancyBboxPatch((t, 2.2), task1_duration, 0.6, 
                              boxstyle="round,pad=0.05", 
                              facecolor='#e74c3c', edgecolor='black', linewidth=1.5)
        ax1.add_patch(rect)
        ax1.text(t + task1_duration/2, 2.5, f'{task1_duration}ms', 
                ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Task 2 (Medium Priority) - Orange, consistent execution  
    task2_times = [2.5, 7.5, 12.5, 17.5]
    task2_duration = 1.5
    for t in task2_times:
        rect = FancyBboxPatch((t, 1.2), task2_duration, 0.6,
                              boxstyle="round,pad=0.05",
                              facecolor='#f39c12', edgecolor='black', linewidth=1.5)
        ax1.add_patch(rect)
        ax1.text(t + task2_duration/2, 1.5, f'{task2_duration}ms',
                ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Task 3 (Low Priority) - Blue, consistent execution
    task3_times = [4.5, 9.5, 14.5, 19.5]
    task3_duration = 0.5
    for t in task3_times:
        if t + task3_duration <= 20:
            rect = FancyBboxPatch((t, 0.2), task3_duration, 0.6,
                                  boxstyle="round,pad=0.05",
                                  facecolor='#3498db', edgecolor='black', linewidth=1.5)
            ax1.add_patch(rect)
            ax1.text(t + task3_duration/2, 0.5, f'{task3_duration}ms',
                    ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Add characteristics box
    ax1.text(0.5, -0.7, '[+] Predictable execution times\n[+] Deterministic behavior\n[+] Easy schedulability analysis',
             fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5),
             verticalalignment='top')
    
    # ML-enabled RTOS Task Execution (Bottom) - showing unpredictability
    ax2.set_xlim(0, 20)
    ax2.set_ylim(0, 3)
    ax2.set_xlabel('Time (ms)', fontsize=11)
    ax2.set_title('ML-enabled RTOS Task Scheduling (Without Proper Partitioning)', 
                  fontsize=13, fontweight='bold')
    ax2.set_yticks([0.5, 1.5, 2.5])
    ax2.set_yticklabels(['RT Task 2\n(Medium)', 'RT Task 1\n(High)', 'ML Task\n(Variable)'])
    ax2.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # ML Task - Purple, VARIABLE execution times
    ml_times = [0, 4.5, 11, 16]
    ml_durations = [3.5, 4, 3, 2.5]  # Variable durations!
    for t, duration in zip(ml_times, ml_durations):
        if t + duration <= 20:
            rect = FancyBboxPatch((t, 2.2), duration, 0.6,
                                  boxstyle="round,pad=0.05",
                                  facecolor='#9b59b6', edgecolor='black', linewidth=1.5,
                                  linestyle='--')  # Dashed to show unpredictability
            ax2.add_patch(rect)
            ax2.text(t + duration/2, 2.5, f'{duration}ms',
                    ha='center', va='center', fontsize=9, fontweight='bold')
    
    # RT Task 1 - Red, tries to maintain consistency but may be delayed
    rt1_times = [4, 9, 15, 19]
    rt1_duration = 1.5
    for i, t in enumerate(rt1_times):
        if t + rt1_duration <= 20:
            color = '#e74c3c' if i < 2 else '#ff6b6b'  # Lighter color indicates issues
            rect = FancyBboxPatch((t, 1.2), rt1_duration, 0.6,
                                  boxstyle="round,pad=0.05",
                                  facecolor=color, edgecolor='black', linewidth=1.5)
            ax2.add_patch(rect)
            if i >= 2:  # Add warning indicator
                ax2.text(t + rt1_duration/2, 1.8, '!', fontsize=16, ha='center', 
                        fontweight='bold', color='red')
    
    # RT Task 2 - Orange, also affected
    rt2_times = [6, 13, 18]
    rt2_duration = 1
    for i, t in enumerate(rt2_times):
        if t + rt2_duration <= 20:
            rect = FancyBboxPatch((t, 0.2), rt2_duration, 0.6,
                                  boxstyle="round,pad=0.05",
                                  facecolor='#f39c12', edgecolor='black', linewidth=1.5)
            ax2.add_patch(rect)
    
    # Add warning box
    ax2.text(0.5, -0.7, '[X] Variable ML execution times\n[X] Potential deadline misses\n[X] Difficult timing guarantees',
             fontsize=10, bbox=dict(boxstyle='round', facecolor='#ffcccc', alpha=0.7),
             verticalalignment='top')
    
    plt.tight_layout()
    
    # Use relative paths from script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, 'figure1_traditional_vs_ml_scheduling.pdf')
    png_path = os.path.join(script_dir, 'figure1_traditional_vs_ml_scheduling.png')
    
    plt.savefig(pdf_path, bbox_inches='tight', dpi=300)
    plt.savefig(png_path, bbox_inches='tight', dpi=300)
    print("Created Figure 1: Traditional vs ML Scheduling")
    plt.close()


def create_figure2_temporal_partitioning():
    """
    Figure 2: Temporal Partitioning Architecture
    Shows how ML tasks are isolated in slack time slots
    
    Side effects:
        Creates figure2_temporal_partitioning.pdf and .png in the script directory
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 7))
    
    ax.set_xlim(0, 28)  # Extended to accommodate benefits text box
    ax.set_ylim(0, 5)
    ax.set_xlabel('Time (ms)', fontsize=12)
    ax.set_title('Temporal Partitioning: Isolating ML Tasks from Critical Real-Time Operations',
                 fontsize=14, fontweight='bold')
    ax.set_yticks([])
    ax.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Define time slots
    slots = [
        {'start': 0, 'duration': 3, 'type': 'critical', 'label': 'Critical\nTask 1', 'priority': 'High'},
        {'start': 3, 'duration': 2, 'type': 'slack', 'label': 'ML Inference\n(Optional)', 'priority': 'Low'},
        {'start': 5, 'duration': 3, 'type': 'critical', 'label': 'Critical\nTask 2', 'priority': 'High'},
        {'start': 8, 'duration': 2.5, 'type': 'slack', 'label': 'ML Training\n(Optional)', 'priority': 'Low'},
        {'start': 10.5, 'duration': 2.5, 'type': 'critical', 'label': 'Critical\nTask 3', 'priority': 'High'},
        {'start': 13, 'duration': 2, 'type': 'slack', 'label': 'ML Predict\n(Optional)', 'priority': 'Low'},
        {'start': 15, 'duration': 3, 'type': 'critical', 'label': 'Critical\nTask 4', 'priority': 'High'},
        {'start': 18, 'duration': 2, 'type': 'slack', 'label': 'Idle/ML\n(Optional)', 'priority': 'Low'},
        {'start': 20, 'duration': 2.5, 'type': 'critical', 'label': 'Critical\nTask 5', 'priority': 'High'},
        {'start': 22.5, 'duration': 2.5, 'type': 'slack', 'label': 'ML Adapt\n(Optional)', 'priority': 'Low'},
    ]
    
    # Draw time slots
    y_pos = 3.5
    for slot in slots:
        if slot['type'] == 'critical':
            color = '#27ae60'  # Green for guaranteed critical tasks
            edge_style = 'solid'
            edge_width = 2.5
            pattern = None
        else:
            color = '#9b59b6'  # Purple for ML/slack time
            edge_style = 'dashed'
            edge_width = 2
            pattern = '///'
        
        rect = Rectangle((slot['start'], y_pos - 0.4), slot['duration'], 0.8,
                         facecolor=color, edgecolor='black', linewidth=edge_width,
                         linestyle=edge_style, hatch=pattern, alpha=0.8)
        ax.add_patch(rect)
        
        # Add label
        ax.text(slot['start'] + slot['duration']/2, y_pos, slot['label'],
               ha='center', va='center', fontsize=9, fontweight='bold',
               color='white')
    
    # Add annotations
    # Guaranteed execution annotation
    ax.annotate('', xy=(1.5, 2.8), xytext=(1.5, 2.2),
               arrowprops=dict(arrowstyle='->', lw=2, color='green'))
    ax.text(1.5, 2.0, 'Guaranteed\nExecution', ha='center', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # Optional execution annotation  
    ax.annotate('', xy=(4, 2.8), xytext=(4, 2.2),
               arrowprops=dict(arrowstyle='->', lw=2, color='purple'))
    ax.text(4, 2.0, 'Optional\n(Can be preempted)', ha='center', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='#e8daef', alpha=0.7))
    
    # Safety monitor layer
    ax.add_patch(Rectangle((0, 4.3), 25, 0.4, facecolor='#34495e', 
                           edgecolor='black', linewidth=2, alpha=0.9))
    ax.text(12.5, 4.5, 'Safety Monitor & Fallback Layer (Oversees All Tasks)', 
           ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # Timeline markers
    for t in range(0, 26, 5):
        ax.axvline(x=t, color='gray', linestyle=':', alpha=0.5, linewidth=1)
        ax.text(t, 0.2, f'{t}', ha='center', fontsize=9)
    
    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#27ae60', edgecolor='black', linewidth=2, 
                      label='Critical Real-Time Tasks (Hard Deadlines)'),
        mpatches.Patch(facecolor='#9b59b6', edgecolor='black', linewidth=2, 
                      linestyle='--', hatch='///', label='ML Tasks in Slack Time (Soft Deadlines)'),
        mpatches.Patch(facecolor='#34495e', edgecolor='black', linewidth=2,
                      label='Safety Monitor Layer')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.08),
             ncol=2, fontsize=10, framealpha=0.9)
    
    # Add benefits text box
    benefits_text = ('Benefits of Temporal Partitioning:\n'
                    '• Critical tasks have guaranteed time slots\n'
                    '• ML tasks execute in slack/idle periods\n'
                    '• Safety monitor ensures no interference\n'
                    '• Maintains real-time guarantees')
    ax.text(25.5, 2.5, benefits_text, fontsize=9, 
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
           verticalalignment='center')
    
    ax.set_ylim(0, 5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.tight_layout()
    
    # Use relative paths from script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, 'figure2_temporal_partitioning.pdf')
    png_path = os.path.join(script_dir, 'figure2_temporal_partitioning.png')
    
    plt.savefig(pdf_path, bbox_inches='tight', dpi=300)
    plt.savefig(png_path, bbox_inches='tight', dpi=300)
    print("Created Figure 2: Temporal Partitioning")
    plt.close()


if __name__ == '__main__':
    print("Generating scheduling diagrams for RTOS report...")
    create_figure1_traditional_scheduling()
    create_figure2_temporal_partitioning()
    print("All diagrams generated successfully!")
