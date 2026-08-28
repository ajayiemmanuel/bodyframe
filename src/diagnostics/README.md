# Diagnostics implementation

`coverage_diagnostics.py` packages the categorical diversity and keypoint
visibility/coordinate-coverage summaries already used by Stage 5. Functions
accept caller-supplied DataFrames and return new summary DataFrames without
mutating source data or applying new underrepresentation thresholds.
