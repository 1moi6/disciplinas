# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Course materials for **Modelagem Matemática** (Mathematical Modeling), taught at UFMT by Prof. Moiseis Cecconello. The course applies mathematical modeling to ecology (population dynamics). Each `aulaX/` folder contains one lecture's slides and assets.

## Slide Formats

- **aula1, aula2**: Beamer (LaTeX) — `.tex` files compiled with `pdflatex` or `lualatex`.
- **aula3+**: Quarto Reveal.js — `.qmd` files compiled with `quarto render`.

## Build Commands

```bash
# Compile a Beamer slide deck
pdflatex ecologia_modelagem.tex        # from inside aula1/
pdflatex ecologia_aula2.tex            # from inside aula2/

# Render a Quarto presentation (HTML + optionally PDF)
quarto render ecologia_aula_captura.qmd               # from inside aula3/
quarto render ecologia_aula_captura.qmd --to beamer   # export PDF via Beamer
```

## Quarto Slide Architecture (aula3+)

Each Quarto lecture folder contains:

| File | Purpose |
|------|---------|
| `*.qmd` | Main slide source (YAML front-matter + Markdown + math) |
| `_defaults.yml` | Shared Reveal.js/Beamer defaults — copy to new lecture folders |
| `_theme.scss` | Custom visual theme (colors, typography, `.eq-card`, `.slide-topbar`, etc.) |

The `_defaults.yml` defines reusable YAML for both `revealjs` and `beamer` outputs, including MathJax macros (`\dd`, `\pp`, `\R`, `\N`, greek shortcuts). Copy both `_defaults.yml` and `_theme.scss` when creating a new lecture folder and reference them in the new `.qmd`.

## Conventions

- Slide topobar pattern: `<div class="slide-topbar"><span class="tb-sec">...</span><span class="tb-crs">...</span></div>` — section label left, course+lecture right.
- Highlighted equations use `<div class="eq-card"><span class="eq-label">...</span> ... </div>`.
- MathJax macros defined per-lecture in `include-in-header` (or via `_defaults.yml`).
- Figures placed alongside `.qmd` and referenced by filename (no subdirectory).
- Language: slides are written in **Brazilian Portuguese**.

## Skills Available

Use the `math-teaching:math-teaching-sequence` skill when generating new lecture material — it applies the project's epistemological teaching sequence. Use `math-teaching:edo-teaching` for ODE-focused lectures.
