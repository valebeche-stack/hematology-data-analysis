# Hematology Data Analysis

Educational Python examples for laboratory hematology data analysis, CBC interpretation, analyzer flags, and smear-review workflows.

This repository is designed as a small scientific portfolio project. It illustrates how laboratory data can be structured, screened, summarized, and visualized while keeping analytical interpretation separate from clinical diagnosis.

## What this project demonstrates

- loading and cleaning CBC data
- basic descriptive statistics
- identification of selected analytical abnormalities
- handling analyzer-generated flags
- creation of an illustrative smear-review trigger
- visualization of WBC, hemoglobin, platelet count, and differential counts
- separation between **instrument result**, **screening rule**, and **expert morphological review**

## Files

- `synthetic_cbc_data.csv` — synthetic CBC dataset with no patient information
- `hematology_analysis.py` — Python workflow for summary statistics, screening, and visualization
- `REVIEW_RULES.md` — explanation of the illustrative review logic and its limitations
- `requirements.txt` — Python dependencies

## Important laboratory principle

Automated hematology results and analyzer flags are screening tools. A flag is not a diagnosis, and a numerical threshold alone does not establish the need for microscopic review in every laboratory setting. Smear-review criteria should be locally validated and should consider analyzer platform and software configuration, patient population, clinical setting, previous results and delta checks, analytical flags and scattergram patterns, local SOPs, and published consensus recommendations.

The rules used in this repository are intentionally simplified and are provided only to demonstrate programming logic.

## Scientific scope

This project reflects interests in laboratory hematology, peripheral blood morphology, automated hematology analyzer interpretation, analytical validation, diagnostic workflow design, and data-driven laboratory decision support.

## Author

**Valentina Becherucci**  
Clinical Laboratory Biologist  
Laboratory Medicine | Clinical Pathology | Hematology | Biomedical Research | AI in Laboratory Medicine

Google Scholar: https://scholar.google.com/citations?user=14LEcucAAAAJ&hl=en

## Disclaimer

All data are synthetic. No patient data are included. The code is educational and must not be used for clinical decision-making without appropriate validation.
