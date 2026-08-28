# BODYFRAME 0.5 — Visual Evaluation Lab

> Structural public-release draft. Final narrative, license, and redistribution-approved samples remain pending.

## Overview

BODYFRAME is a governed pilot workflow for file intake, technical-quality evaluation, visual annotation, calibration, and dataset diagnostics.

## Pipeline

1. File Intake and Metadata QA
2. Technical Image Quality Audit
3. Visual Rubric and Annotation
4. Calibration and Reviewer Reliability
5. Dataset Diagnostics and QA Reporting

## BODYFRAME 0.5 results

- 15 registered and annotated originals across 11 subject groups.
- 15 manual person boxes, 15 skeletons, and 255 normalized keypoint rows.
- Categorical diversity increased from 5/28 to 27/28 fields with more than one observed value.
- Expansion data passed the existing intake and spatial-export validation checks.

These are validated pilot results, not claims of population coverage, model accuracy, fairness, or general reliability.

## Architecture

See `docs/architecture.md` and `docs/id_and_lineage_rules.md`.

## Repository structure

- `docs/`: public methods, manual, architecture, and dataset card
- `src/`: reusable intake, quality, annotation, calibration, and diagnostic code
- `notebooks/`: executable intake walkthrough
- `schemas/`: schema-only, public-safe definitions
- `reports/`: validated aggregate reports
- `outputs/charts/`: validated aggregate PNG charts
- `sample_data/`: redistribution-approved samples, currently empty

## Reproducibility

Install dependencies with `pip install -r requirements.txt`. Run `python src/intake_validation.py --help` to inspect the public intake interface. Data-bearing runs require a registry and files supplied outside this sanitized package.

## Limitations

- 15 originals and one annotation practitioner.
- Calibration covers only the original three-image pilot; expansion Round 2 and inter-annotator reliability are absent.
- Some lower-body keypoints have partial rather than universal coordinate coverage.
- No private or redistribution-unreviewed images are included.

## Roadmap

- Select reviewed code and documentation licenses.
- Add redistribution-approved sample images and matching sample annotations.
- Add public regression fixtures when redistribution-approved samples exist.
- Expand multi-annotator calibration and coverage strata.
