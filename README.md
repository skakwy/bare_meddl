# Bare Meddle - AI/ML Integration in RTOS

## Project Overview

This repository contains the complete deliverables for the research project on **AI/ML Integration: Incorporating machine learning algorithms into RTOS for adaptive scheduling and fault tolerance**.

**Group:** Bare Meddle  
**Due Date:** March 13, 2026  
**Topic:** Challenges and Approaches in integrating AI/ML into Real-Time Operating Systems

## Repository Contents

### 📄 Main Report
- **`AI_ML_Integration_RTOS_Report.tex`** - LaTeX article format (recommended)
  - Professional academic article format
  - Properly formatted citations using BibTeX style
  - Ready for submission and publication
  - Compiled PDF version included
- **`AI_ML_Integration_RTOS_Report.pdf`** - Pre-compiled PDF (7 pages)
  - Generated from LaTeX source
  - Print-ready format
- **`AI_ML_Integration_RTOS_Report.md`** - Markdown version (alternative)
  - Easy to read and edit
  - Can be converted to other formats

**Report Content:**
  - Introduction to AI/ML integration in RTOS
  - Detailed analysis of challenges
  - Various approaches and solutions
  - Real-world applications and case studies
  - 9 academic references with proper citations

### 📊 Comparison Table
- **`comparison_table.csv`** - Detailed comparison of different AI/ML integration approaches
  - Can be opened in Excel or any spreadsheet application
  - Compares 9 different approaches across multiple dimensions
  - Includes advantages, disadvantages, resource requirements, and use cases

### 🎨 Figures
- **`figures/README.md`** - Contains figure descriptions and ASCII visualizations:
  - Figure 1: Execution Time Comparison
  - Figure 2: Temporal Partitioning Architecture
  - Figure 3: Hybrid Architecture Design

### 📽️ Presentation (Optional)
- **`presentation_slides.md`** - Ready-to-use presentation slides (16 slides)
  - Can be converted to PowerPoint or PDF
  - Covers all key points from the report
  - Includes visual diagrams and comparisons

## Key Topics Covered

### Challenges in AI/ML Integration
1. Timing Predictability and Determinism
2. Resource Constraints (memory, power, processing)
3. Real-Time Guarantees
4. Model Validation and Verification
5. Development and Debugging Complexity

### Approaches to AI/ML Integration
1. Model Optimization Techniques (Quantization, Pruning, TinyML)
2. Temporal Partitioning and Scheduling
3. Hardware Acceleration (NPUs, FPGAs, DSPs)
4. Adaptive Scheduling Frameworks (RL-based)
5. Fault Prediction and Tolerance
6. Hybrid Architectures
7. Edge Computing and Distributed Approaches

## How to Use These Materials

### For the Report Submission:
1. **LaTeX Version (Recommended)**: 
   - Use `AI_ML_Integration_RTOS_Report.tex` as the source file
   - Pre-compiled PDF available: `AI_ML_Integration_RTOS_Report.pdf`
   - Professional academic article format
2. **Markdown Version (Alternative)**: 
   - Review `AI_ML_Integration_RTOS_Report.md`
   - Can be converted to PDF or DOCX if needed
3. **Supporting Materials**:
   - Use `comparison_table.csv` as the supplementary Excel sheet
   - Reference `figures/README.md` for figure descriptions

### For the Presentation:
- Option 1: Use the main report as presentation material
- Option 2: Use `presentation_slides.md` and convert to your preferred format
- The slides are structured for a 15-20 minute presentation

## Academic Integrity

All content is based on published research and academic sources. Proper citations are included throughout the report with 9 references from:
- Academic journals
- Conference proceedings
- Authoritative textbooks
- Industry research papers

### Sources that specifically address ML in RTOS (other than `rtos_ml.pdf`)

Of the 8 original bibliography entries, the following three are the ones that actually discuss ML *within* resource-constrained or real-time embedded contexts:

| Key | Citation | Relevance to ML in RTOS |
|-----|----------|-------------------------|
| `warden2019tinyml` | Warden & Situnayake (2019) *TinyML* | **Most directly relevant.** Dedicated to running ML inference on ultra-low-power microcontrollers; covers TensorFlow Lite, model size, and latency constraints directly applicable to RTOS deployments. |
| `han2016deep` | Han, Mao & Dally (2016) *Deep Compression* | Seminal paper on quantization and pruning to shrink neural networks for embedded deployment; underpins Section 3.1 on model-optimization techniques. |
| `chen2017eyeriss` | Chen et al. (2017) *Eyeriss* | Hardware accelerator for deep CNN inference; supports the hardware-acceleration discussion in Section 3.3 and provides deterministic timing analysis for embedded ML. |

The remaining five original sources (`buttazzo2011hard`, `kopetz2011real`, `lee2017introduction`, `burns2017survey`, `goodfellow2016deep`) cover classical RTOS scheduling theory or general deep-learning theory but do not specifically address the intersection of ML and real-time embedded systems.

## File Formats

- **LaTeX**: `AI_ML_Integration_RTOS_Report.tex` - Professional academic article format
- **PDF**: `AI_ML_Integration_RTOS_Report.pdf` - Ready for submission (7 pages)
- **Markdown**: `AI_ML_Integration_RTOS_Report.md` - Easy to read/edit format
- **CSV**: `comparison_table.csv` - Compatible with Excel, Google Sheets
- All text files use UTF-8 encoding for universal compatibility

## Compiling the LaTeX Document

If you need to recompile the LaTeX document:

```bash
# Compile the LaTeX source (run twice for references)
pdflatex AI_ML_Integration_RTOS_Report.tex
pdflatex AI_ML_Integration_RTOS_Report.tex

# Or using latexmk for automatic compilation
latexmk -pdf AI_ML_Integration_RTOS_Report.tex
```

### Required LaTeX Packages:
- inputenc (UTF-8 encoding)
- geometry (page margins)
- graphicx (figures)
- cite (citations)
- hyperref (hyperlinks)
- enumitem (lists)
- booktabs (tables)

All packages are standard and included in major LaTeX distributions (TeX Live, MiKTeX).

## Converting Files

### Markdown to PDF:
```bash
# Using pandoc (if available)
pandoc AI_ML_Integration_RTOS_Report.md -o report.pdf

# Or use online converters like:
# - markdown-to-pdf.com
# - pandoc.org/try
```

### CSV to Excel:
- Open `comparison_table.csv` directly in Microsoft Excel
- Or import into Google Sheets

---

**Prepared by:** Group Bare Meddle  
**Date:** January 30, 2026