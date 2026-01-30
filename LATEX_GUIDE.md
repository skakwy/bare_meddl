# LaTeX Report Guide

## Overview

The main report has been generated in **LaTeX article format** for professional academic submission.

## Files

- **`AI_ML_Integration_RTOS_Report.tex`** - LaTeX source file
- **`AI_ML_Integration_RTOS_Report.pdf`** - Compiled PDF (7 pages)

## PDF Report Details

- **Pages:** 7 (including title page and references)
- **Format:** Standard A4, 11pt font
- **Margins:** 1 inch on all sides
- **Structure:**
  - Title page with group name and date
  - Abstract
  - Main content (sections 1-4)
  - Bibliography (18 references)

## Viewing the PDF

Simply open `AI_ML_Integration_RTOS_Report.pdf` with any PDF reader:
- Adobe Acrobat Reader
- Preview (macOS)
- Evince (Linux)
- Web browser (Chrome, Firefox, etc.)

## Editing the LaTeX Source

If you need to modify the report:

1. Open `AI_ML_Integration_RTOS_Report.tex` in any text editor or LaTeX IDE:
   - **Overleaf** (online, recommended for beginners)
   - **TeXstudio** (cross-platform desktop application)
   - **Visual Studio Code** with LaTeX Workshop extension
   - Any text editor (Vim, Emacs, Sublime Text, etc.)

2. Make your changes to the .tex file

3. Recompile the PDF:
   ```bash
   pdflatex AI_ML_Integration_RTOS_Report.tex
   pdflatex AI_ML_Integration_RTOS_Report.tex
   ```
   (Run twice to resolve cross-references)

## LaTeX Document Structure

```latex
\documentclass[11pt,a4paper]{article}
% Packages and setup
\begin{document}
\maketitle              % Title page
\begin{abstract}        % Abstract section
...
\end{abstract}

\section{...}           % Main sections
\subsection{...}        % Subsections

\begin{thebibliography} % References
\bibitem{...}
...
\end{thebibliography}
\end{document}
```

## Key LaTeX Features Used

### Citations
```latex
\cite{buttazzo2011hard}  % Inline citation
```

### Lists
```latex
\begin{itemize}
  \item First item
  \item Second item
\end{itemize}
```

### Bold Text
```latex
\textbf{Bold text}
```

### Italics
```latex
\textit{Italic text}
```

### Sections
```latex
\section{Section Title}
\subsection{Subsection Title}
```

## Required LaTeX Packages

All standard packages included in TeX Live and MiKTeX:

- **inputenc**: UTF-8 encoding support
- **geometry**: Page layout and margins
- **graphicx**: Include figures (prepared for future use)
- **amsmath**: Mathematical symbols and equations
- **cite**: Citation management
- **hyperref**: Clickable links and references in PDF
- **enumitem**: Enhanced list formatting
- **titlesec**: Section title formatting
- **abstract**: Abstract environment
- **booktabs**: Professional table formatting
- **float**: Float positioning for figures and tables

## Converting to Other Formats

### LaTeX to Word (DOCX)
```bash
pandoc AI_ML_Integration_RTOS_Report.tex -o report.docx
```

### LaTeX to HTML
```bash
pandoc AI_ML_Integration_RTOS_Report.tex -o report.html
```

Note: Pandoc must be installed for these conversions.

## Troubleshooting

### "File not found" errors
- Make sure all required packages are installed
- Run: `sudo apt install texlive-latex-extra texlive-fonts-recommended`

### References not showing
- Compile twice: citations and references need two passes to resolve

### PDF not updating
- Delete auxiliary files: `rm *.aux *.out *.log`
- Recompile from scratch

## Online Compilation (No Installation Required)

Upload `AI_ML_Integration_RTOS_Report.tex` to **Overleaf**:
1. Go to https://www.overleaf.com
2. Create free account
3. New Project → Upload Project
4. Upload the .tex file
5. Click "Recompile" to generate PDF

## Submission Ready

The compiled PDF (`AI_ML_Integration_RTOS_Report.pdf`) is:
- ✅ Print-ready quality
- ✅ Properly formatted citations
- ✅ Professional academic appearance
- ✅ 7 pages including references
- ✅ Ready for submission by March 13, 2026

## Academic Writing Standards

The LaTeX version ensures:
- Consistent formatting throughout
- Proper citation style
- Professional typography
- Standard academic document structure
- High-quality PDF output suitable for publication

---

**Note:** The PDF file is already compiled and ready to use. You only need to edit the LaTeX source if you want to make changes to the content.
