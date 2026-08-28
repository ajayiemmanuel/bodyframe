# BODYFRAME Technical Image Quality Audit

## 1. Objective

This subproject tests a complete technical-quality evaluation workflow using controlled image degradations, automated image measurements, and blinded human review. Its purpose is to determine whether the pipeline is sensitive to meaningful technical deterioration while keeping automated evidence, human quality judgement, and defect diagnosis methodologically distinct.

## 2. Dataset and controlled variants

The pilot contains three source originals and 15 technical variants, for 18 reviewed assets in total. Controlled transformations covered JPEG compression, resizing, Gaussian blur, synthetic noise, exposure reduction and increase, warm and cool colour shifts, and high or extreme oversharpening. Every derivative retained its source-image lineage and was registered separately from the original asset.

## 3. Automated technical measurements

The automated audit recorded image dimensions, file size, luminance mean and standard deviation, shadow and highlight clipping, Laplacian variance, and red, green, and blue channel means. These metrics supplied reproducible evidence about resolution, tonal distribution, clipping, high-frequency response, and colour balance. They were not converted into automatic human quality scores or standalone pass/fail decisions.

## 4. Blind human review methodology

All 18 assets were randomized with a deterministic seed, copied under neutral identifiers, and reviewed in a locked Round 1 packet. The reviewer scored exposure, sharpness, colour, artifacts, framing, and overall technical quality on the rubric’s 1–5 scale. The decision rules classify severe required-dimension failures as fail, an overall score or required dimension of 3 as conditional pass, and technically usable images meeting the required minima as pass. Asset identities and controlled transformations were revealed only after scores were locked. No review timestamp was captured.

## 5. Results

Round 1 produced 7 pass, 7 conditional-pass, and 4 fail decisions. Mean scores were: exposure 4.06, sharpness 4.06, colour 3.61, artifact 4.00, framing 4.83, and overall technical quality 3.72.

Originals outscored controlled variants across every dimension: exposure 5.00 versus 3.87; sharpness 5.00 versus 3.87; colour 5.00 versus 3.33; artifact 5.00 versus 3.80; framing 5.00 versus 4.80; and overall 5.00 versus 3.47.

![Original versus controlled-variant scores](../charts/02_technical_quality/01_original_vs_variant_scores.png)

![Technical usability distribution](../charts/02_technical_quality/02_usability_distribution.png)

## 6. Defect sensitivity versus diagnostic specificity

Quality sensitivity and defect diagnosis are related but different tasks. Exact expected primary-defect identification was 6/15 (40%); the expected defect was recorded as a secondary defect in 0/15 cases; and the expected defect was not explicitly named in 9/15 cases (60%). The latter cases should not simply be described as missed defects when the relevant human dimension score still deteriorated.

All controlled severity series showed an equal-or-worse relevant human score as degradation increased: JPEG Q70 → Q40 → Q15 on artifact score, resize 1024 → 512 on artifact score, blur G01 → G03 on sharpness, noise L01 → L03 on artifact score, and oversharpen high → extreme on sharpness.

![Expected-defect identification](../charts/02_technical_quality/03_defect_identification.png)

![Controlled severity-series response](../charts/02_technical_quality/04_severity_series_response.png)

## 7. Automated metric versus human judgement

Laplacian variance and human sharpness score had a Spearman association of approximately -0.435. Total clipping—shadow clipping plus highlight clipping—and exposure score had a Spearman association of approximately -0.530.

Laplacian variance tracked blur severity successfully: stronger blur reduced both the automated response and perceived sharpness. However, resizing, noise, and oversharpening introduced high-frequency responses that increased Laplacian variance even when human sharpness or technical quality declined. Laplacian variance should therefore be treated as supporting evidence, not as a universal perceived-sharpness score.

![Laplacian variance versus human sharpness](../charts/02_technical_quality/05_laplacian_vs_human_sharpness.png)

![Total clipping versus exposure score](../charts/02_technical_quality/06_clipping_vs_exposure_score.png)

## 8. Important observations

- JPEG Q70 and Q40 remained visually acceptable on artifact scoring, while Q15 deteriorated.
- Warm and cool casts reduced colour scores even though the colour-cast defect code was not explicitly named.
- Stronger blur reduced visual sharpness.
- Stronger noise reduced artifact quality.
- Stronger oversharpening reduced human sharpness despite increased Laplacian variance.
- Exposure manipulations caused strong exposure-score deterioration.
- The small framing-score movement—from 5.00 for originals to 4.80 for variants—suggests possible dimension leakage because the controlled transformations did not intentionally alter framing.
- Reviewer-recorded defect frequency had a three-way tie at two observations each: ART_RESIZE, EXP_HIGHLIGHT_CLIP, and SHARP_HALO.

## 9. Limitations

This is a small pilot comprising three source images from one subject, one reviewer, one blind review round, and synthetic technical defects. All reviewer-confidence values were 4, there were no adjudication cases, and no review timestamp was captured. The automated metrics are intentionally simple baseline measurements and should not be interpreted as comprehensive perceptual models.

## 10. Conclusion

The pilot demonstrates a functioning technical-quality evaluation pipeline with strong sensitivity to controlled degradation. It also shows that defect diagnosis and automated metric interpretation require calibration and should remain separate from human quality judgement. The combined registry, controlled-variant plan, automated evidence, blind review, and canonical persistence provide a reproducible basis for expanding the audit to more subjects, reviewers, and review rounds.
