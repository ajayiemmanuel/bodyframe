# BODYFRAME 0.5 Public Release Manifest

This manifest covers the sanitized `public_release/` staging copy. It does not authorize publication or image redistribution.

## Staged files

| Staged file | Source project file | Status | Publication rationale |
|---|---|---|---|
| `.gitignore` | `publication safety requirements` | generated | Prevents common private, raw, temporary, credential, and backup material from being committed. |
| `LICENSE_PENDING.md` | `release governance requirement` | generated | Prevents an unreviewed license or image-redistribution grant. |
| `PUBLICATION_AUDIT.md` | `staged publication scan` | generated | Contains aggregate audit findings only. |
| `README_DRAFT.md` | `validated final dataset card and lab report` | generated | Structural draft only; aggregate validated claims and explicit limitations. |
| `RELEASE_MANIFEST.md` | `staged-file inventory` | generated | Lists staged provenance and safety decisions only. |
| `docs/annotation_manual_v1.1.md` | `03_annotation/annotation_manual_v1.1.md` | copied unchanged | Method documentation only; no image files or private metadata. |
| `docs/architecture.md` | `05_dataset_diagnostics/bodyframe_visual_evaluation_lab_report_v0_5_final.md; registry structure` | generated | Aggregate architecture only; no private rows, paths, images, or raw exports. |
| `docs/dataset_card_v0_5.md` | `05_dataset_diagnostics/bodyframe_dataset_card_v0_5_final.md` | copied unchanged | Validated aggregate dataset documentation without private rows. |
| `docs/id_and_lineage_rules.md` | `00_shared_architecture/id_and_lineage_rules.md; repository governance rules; registry schema` | adapted | The source placeholder was empty; this public version contains validated identifier and relationship rules only. |
| `docs/methodology.md` | `validated Stage 1–5 reports and annotation manual` | generated | Only validated aggregate methods and results are included. |
| `notebooks/intake_validation.ipynb` | `01_file_intake/intake_validation.ipynb` | copied unchanged | Executable notebook wrapper with no embedded outputs, data, or local paths. |
| `outputs/charts/01_file_intake/01_intake_status_counts.png` | `charts/01_file_intake/01_intake_status_counts.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/01_file_intake/02_failure_code_frequency.png` | `charts/01_file_intake/02_failure_code_frequency.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/01_file_intake/03_metadata_completeness.png` | `charts/01_file_intake/03_metadata_completeness.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/01_file_intake/04_original_vs_jpeg_q40_size.png` | `charts/01_file_intake/04_original_vs_jpeg_q40_size.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/02_technical_quality/01_original_vs_variant_scores.png` | `charts/02_technical_quality/01_original_vs_variant_scores.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/02_technical_quality/02_usability_distribution.png` | `charts/02_technical_quality/02_usability_distribution.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/02_technical_quality/03_defect_identification.png` | `charts/02_technical_quality/03_defect_identification.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/02_technical_quality/04_severity_series_response.png` | `charts/02_technical_quality/04_severity_series_response.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/02_technical_quality/05_laplacian_vs_human_sharpness.png` | `charts/02_technical_quality/05_laplacian_vs_human_sharpness.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/02_technical_quality/06_clipping_vs_exposure_score.png` | `charts/02_technical_quality/06_clipping_vs_exposure_score.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/05_dataset_diagnostics/01_asset_pipeline_counts.png` | `charts/05_dataset_diagnostics/01_asset_pipeline_counts.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/05_dataset_diagnostics/02_technical_usability.png` | `charts/05_dataset_diagnostics/02_technical_usability.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/05_dataset_diagnostics/03_original_vs_variant_quality.png` | `charts/05_dataset_diagnostics/03_original_vs_variant_quality.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/05_dataset_diagnostics/04_annotation_field_coverage.png` | `charts/05_dataset_diagnostics/04_annotation_field_coverage.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/05_dataset_diagnostics/05_keypoint_visibility_coverage.png` | `charts/05_dataset_diagnostics/05_keypoint_visibility_coverage.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/05_dataset_diagnostics/06_keypoint_repeatability.png` | `charts/05_dataset_diagnostics/06_keypoint_repeatability.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/charts/05_dataset_diagnostics/07_calibration_agreement.png` | `charts/05_dataset_diagnostics/07_calibration_agreement.png` | copied unchanged | Validated aggregate PNG chart; no source image pixels or private metadata tables. |
| `outputs/sample_reports/README.md` | `publication policy` | generated | Contains no image-level data or private identifiers. |
| `outputs/sample_tables/README.md` | `publication policy` | generated | Prevents accidental publication of complete private annotation tables. |
| `reports/annotation_pilot_qa_report.md` | `03_annotation/annotation_pilot_qa_report.md` | copied unchanged | Validated annotation-pilot QA report; no raw exports or private rows. |
| `reports/bodyframe_visual_evaluation_lab_report_v0_5_final.md` | `05_dataset_diagnostics/bodyframe_visual_evaluation_lab_report_v0_5_final.md` | copied unchanged | Validated aggregate report without image-dependent tables. |
| `reports/calibration_summary.md` | `04_calibration/calibration_summary.md` | copied unchanged | Validated aggregate calibration summary without raw annotations. |
| `reports/technical_quality_qa_report.md` | `02_technical_quality/technical_quality_qa_report.md` | copied unchanged | Validated aggregate technical-quality QA report; no images or private metadata. |
| `requirements.txt` | `imports used by staged src modules` | generated | Minimal dependency list derived from staged reusable Python code. |
| `sample_data/README.md` | `publication policy` | generated | Explicitly documents that zero private or third-party images are staged. |
| `schemas/annotation_taxonomy.csv` | `03_annotation/expansion/bodyframe_annotation_expansion.xlsx (taxonomy sheet)` | adapted | Schema only; expansion-specific asset values were generalized and no annotation rows were copied. |
| `schemas/keypoint_schema.md` | `03_annotation/annotation_manual_v1.1.md` | adapted | Public schema documentation only; no coordinates or image identifiers. |
| `schemas/registry_schema.csv` | `data/raw_tables/bodyframe_master_registry.xlsx (schema only)` | generated | Column definitions only; no registry rows, filenames, paths, or metadata were exported. |
| `src/annotation/README.md` | `03_annotation/annotation_manual_v1.1.md; spatial validation reports` | adapted | Documents the public normalization surface and explicit non-inference boundary. |
| `src/annotation/__init__.py` | `public packaging for validated Stage 3 rules` | generated | Exports public normalization helpers only; no data or paths. |
| `src/annotation/normalize_annotations.py` | `03_annotation/annotation_manual_v1.1.md; 03_annotation/outputs/spatial_annotation_validation.md; validated normalized tables` | adapted | Refactors established visibility, keypoint, and manual-box rules without embedding annotations or raw-export data. |
| `src/calibration/__init__.py` | `public packaging for validated Stage 4 calculations` | generated | Exports repeatability calculations only; no data or paths. |
| `src/calibration/reliability_metrics.py` | `04_calibration/calibration_pilot_report.md; categorical_repeatability.csv; bbox_repeatability.csv; keypoint_repeatability.csv` | adapted | Refactors exact agreement, bbox IoU, and keypoint-distance formulas and preserves the small-N kappa limitation. |
| `src/diagnostics/README.md` | `05_dataset_diagnostics/expansion/expansion_coverage_report.md` | adapted | Documents public coverage calculations without private analysis rows or new thresholds. |
| `src/diagnostics/__init__.py` | `public packaging for validated Stage 5 calculations` | generated | Exports aggregate coverage helpers only; no data or paths. |
| `src/diagnostics/coverage_diagnostics.py` | `05_dataset_diagnostics/outputs/tables/annotation_coverage_v0_5.csv; expansion_coverage_report.md` | adapted | Refactors established categorical and keypoint coverage counts without embedding source rows. |
| `src/intake_validation.py` | `01_file_intake/intake_validation.py` | copied unchanged | Reusable validation code; contains rules only and no private records. |
| `src/technical_quality/README.md` | `02_technical_quality/technical_quality_qa_report.md` | adapted | Documents the public metric surface and its evidence-only boundary. |
| `src/technical_quality/__init__.py` | `public packaging for validated Stage 2 calculations` | generated | Exports public quality-metric helpers only; no data or paths. |
| `src/technical_quality/quality_metrics.py` | `02_technical_quality/quality_evaluation_results.xlsx AssetMetricsTable; technical_quality_qa_report.md` | adapted | Refactors the established metric formulas without images, human scores, or thresholds. |


## Deliberately excluded

- Private original images and processed image derivatives
- Candidate expansion and holdout images
- Raw CVAT, COCO, and other archive exports
- Complete image-dependent annotation tables
- Private registry rows, source-provider filenames, local paths, and EXIF/location metadata
- Workbook backups, temporary inspection helpers, debug files, and scratch code
- Credentials, environment files, tokens, and secrets

The `sample_data/images/` directory is intentionally empty pending redistribution-rights review.
