# Univariate & Correlation Analysis Report
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

> [!IMPORTANT]
> The Jupyter Notebookk this report relies on can be found in [`notebooks\AmesHousing\univariate_analysis.ipynb`](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/notebooks/AmesHousing/univariate_analysis.ipynb) and [`notebooks\AmesHousing\correlation.ipynb`](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/notebooks/AmesHousing/correlation.ipynb.ipynb).

---

## 1. Univariate Analysis

Univariate analysis was performed on the raw Ames Housing dataset prior to any preprocessing or feature engineering. The goal was to understand the individual behaviour of each variable — its distribution, variability, and potential modelling challenges — before proceeding to multivariate analysis or predictive modelling.

`MS SubClass` was recoded from numeric to categorical at this stage, as it encodes nominal dwelling type classes rather than a true quantitative measure.

---

### 1.1 Numerical Variables

Descriptive statistics were computed for all numerical features, including measures of central tendency (mean, median), dispersion (standard deviation, IQR, coefficient of variation), and distributional shape (skewness, kurtosis).

Variables were then flagged for potential modelling challenges based on the following criteria:

| Flag | Criterion |
|---|---|
| High Variability | Coefficient of Variation ≥ 0.70 |
| Highly Skewed | \|Skewness\| > 1.0 |
| Moderately Skewed | \|Skewness\| ≥ 0.5 |
| Heavy Tails | Kurtosis between 3 and 10 |
| Extreme Outliers | Kurtosis > 10 |

Features that met none of the above criteria were classified as **Statistically Well-Behaved**.

Key findings across the numerical variables:

- **Area and size variables** (`Gr Liv Area`, `Total Bsmt SF`, `1st Flr SF`, `TotalSF`) exhibit right skew and high variability, consistent with the wide range of property sizes in the dataset. A small number of very large properties pull the distributions rightward.
- **Sparse features** such as `Pool Area`, `3Ssn Porch`, `Low Qual Fin SF`, `Misc Val`, and `Screen Porch` are highly skewed and kurtotic, driven by the fact that the vast majority of observations have a value of zero. These variables flag as having extreme outliers, but this is a structural property of near-zero-inflated distributions rather than genuine data errors.
- **Year variables** (`Year Built`, `Year Remod/Add`, `Garage Yr Blt`) are left-skewed, reflecting a concentration of more recently built or remodelled properties in the dataset.
- **Sale price** (`SalePrice`) is right-skewed, as is typical of residential property price distributions. This motivates the log transformation applied during preprocessing.
- **Bathroom and room count variables** (`Full Bath`, `Half Bath`, `Bedroom AbvGr`) are relatively well-behaved, with moderate skewness and limited variability.

---

### 1.2 Categorical Variables

For each categorical variable, the following statistics were computed:

- **Cardinality**: number of unique categories, classified as Low (< 10), Medium (10–30), or High (> 30).
- **Dominant category percentage**: the share of observations held by the most frequent category, used to identify near-constant variables.
- **Rare levels**: categories appearing in fewer than 5% of observations or fewer than 10 total instances, which can cause instability in models that require sufficient support per category.
- **Missing percentage**: proportion of missing values before any imputation.

Key findings across the categorical variables:

- **Near-constant variables** warrant attention. `Street` (paved vs. gravel road access) and `Utilities` have dominant categories covering over 99% of observations, meaning they carry almost no discriminative power and are candidates for removal before modelling.
- **High-cardinality variables** include `Neighborhood` (28 categories), `Exterior 1st` (16), and `Exterior 2nd` (17). These require grouping or encoding strategies to avoid overfitting, and were addressed during preprocessing via neighbourhood tiering.
- **Rare levels** are widespread across quality and condition rating variables (`Pool QC`, `Misc Feature`, `Alley`, `Fence`). Many of these features are absent from the majority of properties, producing heavily imbalanced category distributions.
- **Missing values** are concentrated in structural features — those where absence of the feature, not a data entry error, explains the `NaN`. Variables such as `Pool QC`, `Alley`, `Fence`, `Fireplace Qu`, and the Garage and Basement groupings all have high missing rates that were treated accordingly during preprocessing.
- **Quality rating variables** (`Overall Qual`, `Exter Qual`, `Bsmt Qual`, `Kitchen Qual`, `Garage Qual`, `Fireplace Qu`) share a consistent ordinal scale and were encoded numerically during preprocessing.

---

## 2. Correlation Analysis

Correlation analysis was performed on the raw dataset to identify which variables are most predictive of `SalePrice` and to assess multicollinearity among predictors.

---

### 2.1 Target Variable Distribution

`SalePrice` is right-skewed, with a long tail driven by a small number of high-value properties. The bulk of sales are clustered in the $100,000–$250,000 range, with a mean above the median. This skew motivates the log transformation applied to `SalePrice` before regression modelling.

---

### 2.2 Pearson Correlation with SalePrice

Pearson correlation was computed between all numerical features and `SalePrice`. The top 10 most correlated features were:

| Feature | Pearson r |
|---|---|
| Overall Qual | 0.80 |
| Gr Liv Area | 0.71 |
| Garage Cars | 0.64 |
| Garage Area | 0.62 |
| Total Bsmt SF | 0.61 |
| 1st Flr SF | 0.60 |
| Full Bath | 0.56 |
| TotRms AbvGrd | 0.53 |
| Year Built | 0.52 |
| Year Remod/Add | 0.51 |

`Overall Qual` is the strongest single predictor with r = 0.80, reflecting that perceived quality of finish and materials is the dominant driver of sale price in this dataset. Size-related variables (`Gr Liv Area`, `Total Bsmt SF`, `1st Flr SF`) cluster as the next most predictive group, followed by garage capacity and recency of construction or remodelling.

---

### 2.3 Pearson vs. Spearman Correlation

Both Pearson and Spearman correlation were computed and compared for all numerical features against `SalePrice`. Spearman correlation is rank-based and more robust to outliers and non-linear monotonic relationships.

For most top predictors, Pearson and Spearman values were closely aligned, suggesting that the linear correlation is a reasonable approximation. However, for area-based variables with extreme outliers (`Pool Area`, `Misc Val`, `Low Qual Fin SF`), Spearman correlations diverged or showed weaker signal, consistent with their near-zero-inflated distributions distorting the Pearson coefficient. Where the two measures agreed, confidence in the linear relationship was higher; where they diverged materially, the Spearman value was considered the more reliable guide to the true monotonic association.

---

### 2.4 Categorical Variables vs. SalePrice

Boxplot analysis was used to examine the relationship between low-cardinality categorical variables (≤ 10 unique values) and `SalePrice`. Key observations:

- **Quality and condition ratings** (`Overall Qual`, `Exter Qual`, `Kitchen Qual`, `Bsmt Qual`, `Heating QC`) showed strong monotonic relationships with `SalePrice` — higher ratings consistently corresponded to higher median prices and tighter distributions. These are among the most informative categorical predictors.
- **`MS Zoning`** showed clear price separation between residential zones, with floating village residential and residential low-density properties commanding higher prices than commercial or industrial zones.
- **`Central Air`** showed a pronounced price gap between properties with and without air conditioning, making it a discriminative binary feature despite its low cardinality.
- **`Sale Condition`** exhibited notable price variation, with `Partial` sales (incomplete homes sold before construction) commanding substantially higher median prices — a finding that motivated its inclusion in the final OLS model.
- **`Paved Drive`** showed a moderate price gradient, with fully paved driveways correlating with higher prices.
- Variables such as `Land Slope`, `Utilities`, and `Street` showed minimal price variation across categories, consistent with the near-constant distributions identified in the univariate analysis.

---

### 2.5 Multicollinearity

To assess multicollinearity, Pearson correlation was first computed among all numerical predictors (excluding `SalePrice`). Features with any pairwise correlation above 0.50 in absolute value were isolated for VIF analysis.

VIF was computed on this subset after imputing structural missing values (basement and garage columns filled with 0) and dropping remaining `NaN` rows.

Key findings:

- **Area variables** showed the highest VIF values. `Gr Liv Area`, `TotRms AbvGrd`, `1st Flr SF`, and `Total Bsmt SF` are strongly interrelated — larger homes have more rooms, more floor area, and more basement area simultaneously. Using all of these in a single model without care would inflate standard errors significantly.
- **Garage variables** (`Garage Area`, `Garage Cars`) are highly correlated with each other (r > 0.88), meaning they encode largely redundant information. Only one should typically be used in a model, or they should be combined into a composite feature such as `Garage Score`.
- **Year variables** (`Year Built`, `Year Remod/Add`, `Garage Yr Blt`) are moderately correlated. Homes that were built recently tend to have been remodelled recently and have newer garages, creating a cluster of temporal redundancy.
- **`House Age` and `Years Since Remodel`**, the engineered time features, inherit the moderate correlation of their source variables. Their VIF remained within acceptable bounds in the final models, but the relationship was monitored throughout model iteration.

These findings directly informed feature selection in the modelling phase: composite features (`TotalSF`, `Overall Score`, `Garage Score`) were preferred over their constituent parts to reduce redundancy, and VIF was computed after each model iteration to confirm that multicollinearity did not inflate standard errors.