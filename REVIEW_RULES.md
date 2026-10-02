# Illustrative Smear-Review Logic

The purpose of this file is to make the assumptions of the demo explicit.

## Conceptual model

A manual peripheral blood smear review may be triggered by a combination of numerical abnormalities, analyzer-generated flags, scattergram abnormalities, previous patient results, clinical context, and local laboratory rules.

The demo script uses only a small subset of these factors because it is intended to demonstrate coding logic rather than reproduce a validated laboratory SOP.

## Illustrative numerical triggers used in the script

The Python example labels a sample for review when one or more of the following demo conditions are met:

- WBC < 2.0 or > 30.0 ×10^9/L
- hemoglobin < 8.0 g/dL
- platelet count < 80 or > 800 ×10^9/L
- absolute neutrophil count < 1.0 ×10^9/L
- presence of an analyzer flag for blasts, atypical lymphocytes, immature granulocytes, or platelet clumps

These thresholds are **not presented as universal clinical criteria**.

## Why this matters

A reviewer should be able to distinguish:

- **observed data:** CBC values and analyzer flags;
- **rule-based interpretation:** whether a predefined trigger is met;
- **morphological interpretation:** what is actually seen on the blood smear;
- **clinical conclusion:** which requires integration with the patient's clinical context.

## Limitations

This demonstration does not include age-specific reference intervals, pregnancy-specific ranges, neonatal/pediatric rules, delta checks, previous morphology, scattergram images, instrument-specific Q-flags, duplicate or repeat analysis, pre-analytical quality indicators, clinical diagnosis, or validated local smear-review criteria.

For real laboratory use, rules must be validated against the local population, analyzer configuration, microscopy workflow, and clinical requirements.
