# BODYFRAME Architecture

BODYFRAME is organized as a connected five-stage visual-evaluation workflow supported by a shared registry and immutable identifiers.

1. **File Intake and Metadata QA** validates registry linkage, file integrity, format, dimensions, hashes, naming, folders, duplicates, and required metadata.
2. **Technical Image Quality Audit** combines controlled technical variants, automated evidence, and blinded human review without turning metrics into automatic quality decisions.
3. **Visual Rubric and Annotation** records image-level categorical evidence, one authoritative manual person box, and a named 17-keypoint skeleton.
4. **Calibration and Reviewer Reliability** measures repeat annotation. The v0.5 calibration applies only to the original three-image pilot.
5. **Dataset Diagnostics** reconciles scopes and reports categorical, spatial, and release-gate coverage.

The data model follows `subject → capture session → source image → asset → evaluation`. Original files are protected outside this public staging package. Derivatives retain their source and parent lineage. Canonical native spatial annotations are normalized into analysis tables; interoperability exports do not replace canonical sources.
