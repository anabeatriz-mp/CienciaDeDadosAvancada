# Ames Housing Prices Analysis
---
This project simulates a professional data science workflow using the Ames Housing dataset. 

The primary objective is to move beyond simple model fitting by focusing **project structure, reproducibility, and documentation**, which are essential skills for advanced data science practice in both academic and industry settings.

The goal of the analysis is to understand the factors affecting residential property prices in Ames, Iowa, and to prepare a clean, well-documented pipeline for future predictive modeling.

---

## Report of Ames Housing Analysis

### Table of Contents 
- [Dataset Variables Report](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/reports/DatasetVariableReport.md)
- [Initial Data Inspection](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/reports/InitialDataInspection.md)
- [Missing Analysis](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/reports/Missing_Values_Report.md)
- [Univariate and Correlation Analysis](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/reports/Univariate_Correlation_Report.md)
- [Preprocessing of the Dataset](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/reports/Preprocessing_Report.md)
- [Modelling and Conclusions](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/reports/Modelling_Report.md)

---
## Project Scafolding

```
project/
├── data/
│   ├── raw/            # Original, immutable datasets
│   ├── processed/      # Processed dataset
├── notebooks/          # EDA, prototyping, and experimentation
│   ├── AmesHousing/    # Supporting Jupyter Notebooks for the AmesHousing Dataset analysis
│   ├── classes/        # Jupyter Notebooks from class
├── reports/
├── README.md           # Project overview and instructions
├── requirements.txt    # Python dependencies
└── .gitignore          # Files ignored by Git
```
---
## Installation & Setup

This project uses [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) for high-performance dependency management.

### 1. Clone the Repository
```
git clone https://https://github.com/anabeatriz-mp/CienciaDeDadosAvancada
cd CienciaDeDadosAvancada
```

### 2. Initialize the Environment
```
uv venv
uv pip install -r requirements.txt
```

### 3. Activate the Environment
```
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

---

## Usage
1. Place the AmesHousing.csv file inside `data/raw/`.

2. Run the notebooks in the `notebooks/` directory to reproduce contents of this analysis.
