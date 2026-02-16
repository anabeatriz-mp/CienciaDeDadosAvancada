# Ames Housing Prices Analysis

This project simulates a professional data science workflow using the Ames Housing dataset. 

The primary objective is to move beyond simple model fitting by focusing **project structure, reproducibility, and documentation**, which are essential skills for advanced data science practice in both academic and industry settings.

The goal of the analysis is to understand the factors affecting residential property prices in Ames, Iowa, and to prepare a clean, well-documented pipeline for future predictive modeling.

## Project Scafolding

```
project/
├── data/
│   ├── raw/            # Original, immutable datasets
├── notebooks/          # EDA, prototyping, and experimentation
├── reports/
├── README.md           # Project overview and instructions
├── requirements.txt    # Python dependencies
└── .gitignore          # Files ignored by Git
```

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

## Usage
1. Place the AmesHousing.csv file inside `data/raw/`.

2. Run the notebooks in the `notebooks/` directory to reproduce the exploratory data analysis and summary table generation.

## Data Source

The dataset used is the Ames Housing Dataset, which contains 2,930 observations and 82 variables describing residential property sales in Ames, Iowa, from 2006 to 2010.

- Source: [Kaggle - Ames Housing Dataset](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset)
- Format: CSV
- Key Features: Includes nominal, ordinal, discrete, and continuous variables ranging from soil type to sale price.

## Initial Data Inspection

The dataset contains 2,930 observations across 82 variables.

### Key Findings from Initial Profiling:

- The following variables show significant missing data:
    - `Alley` - 93.24%
    - `Mas Vnr Type` - 60.58%
    - `Fireplace Qu` - 48.53%
    - `Pool QC` - 99.56%
    - `Fence` - 80.48%
    - `Misc Feature` - 96.38%
- The dataset is diverse - it includes a mix of 43 categorical variables and 39 numerical variables.

## Summary Table of Key Variables

A full diagnostic table can be found in `reports/SummaryProfilingTable.md`. Below is a snapshot of critical features:

|   Variable   | Num of Values | % of Missing Values | Unique Values | Mean / Mode | Python Type |
|:------------:|:-------------:|:-------------------:|:-------------:|:-----------:|:-----------:|
|   SalePrice  |      2930     |        0.00%        |      N/A      |  180796.06 |    int64    |
|    Pool QC   |       13      |        99.56%       |       4       |      Ex     |     str     |
|     Alley    |      198      |        93.24%       |       2       |     Grvl    |     str     |
| Lot Frontage |      2440     |        16.72%       |      N/A      |    69.23    |   float64   |

## Interpretation and Preliminary Insights

Based on the initial profiling of the Ames Housing dataset, the following insights guide the transition from exploration to data preparation:

- The missing values in this dataset are often "informative" rather than accidental. For variables like `Pool QC` and `Alley`, the high percentage of null values indicates the absence of that feature.
- Unlike the variables mentioned above `Lot Frontage` has a genuine data quality challenge with a 16.72% missing rate. Since a property must have a physical lot frontage, it's likely that these nulls are true missing values.

The proposed next steps are:
- `NaN` values should be filled with a category like `"None"` to preserve information about the property.
- For other variables like `Lot Frontage` we should apply an imputation method to maintain data integrity.

