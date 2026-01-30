# Figures for AI/ML Integration in RTOS Report

This directory contains figures and diagrams referenced in the main report.

## Figure 1: Execution Time Comparison - Traditional vs ML Tasks

This figure illustrates the difference in execution time predictability between traditional RTOS tasks and ML-based tasks.

**Description:**
- Traditional RTOS tasks show consistent, predictable execution times with minimal variation
- ML tasks exhibit variable execution times that can exceed worst-case bounds
- The figure demonstrates why timing analysis becomes challenging with ML integration

**Visualization:**
```
Traditional RTOS Task Execution:
Time →
|====|====|====|====|====|  (Consistent execution periods)
 T1   T1   T1   T1   T1

ML Task Execution:
Time →
|======|===|==========|=====|====|  (Variable execution times)
 ML1   ML1    ML1      ML1   ML1
```

## Figure 2: Temporal Partitioning Architecture

This figure shows how ML tasks can be temporally isolated from critical real-time tasks.

**Description:**
- Time slots are allocated for critical real-time tasks (guaranteed execution)
- Slack time slots are used for ML inference
- Safety monitors ensure ML tasks do not interfere with critical operations
- Diagram shows the separation of concerns in mixed-criticality systems

**Visualization:**
```
Time Slots:
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│Critical │ Slack   │Critical │ Slack   │Critical │
│Task 1   │ (ML)    │Task 2   │ (ML)    │Task 3   │
└─────────┴─────────┴─────────┴─────────┴─────────┘
     ↓         ↓         ↓         ↓         ↓
  Guaranteed  Optional  Guaranteed Optional Guaranteed
```

## Figure 3: Hybrid Architecture for ML-RTOS Integration

This figure depicts a layered architecture approach for integrating ML into RTOS.

**Description:**
- Layer 1: Hardware abstraction and RTOS kernel (deterministic)
- Layer 2: Real-time critical tasks with hard deadlines
- Layer 3: ML-based adaptive components (soft real-time)
- Layer 4: Safety monitors and fallback mechanisms
- Shows data flow and control interactions between layers

**Visualization:**
```
┌─────────────────────────────────────────────┐
│   Safety Monitors & Fallback Mechanisms    │ Layer 4
├─────────────────────────────────────────────┤
│   ML-Based Adaptive Components              │ Layer 3
│   (Scheduling, Fault Detection, Adaptation) │
├─────────────────────────────────────────────┤
│   Real-Time Critical Tasks                  │ Layer 2
│   (Hard Deadline Guarantees)                │
├─────────────────────────────────────────────┤
│   RTOS Kernel & Hardware Abstraction        │ Layer 1
│   (Deterministic Core)                      │
└─────────────────────────────────────────────┘
         ↕                    ↕
    [Hardware]          [Sensors/Actuators]
```
