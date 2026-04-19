# Modelling Report
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
> The Jupyter Notebook this report relies on can be found in [`notebooks\AmesHousing\modeling.ipynb`](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/notebooks/AmesHousing/modeling.ipynb).

---

## 1. Overview

Two statistical models were developed using the processed Ames Housing dataset:

- **OLS Linear Regression** (`statsmodels.formula.api.ols`) to predict `Log_SalePrice`
- **Logistic Regression** (`statsmodels.formula.api.logit`) to predict `Is High Price` (binary: top tercile of sale price vs. the rest)

Both models were built iteratively, adding features one at a time and evaluating each on the validation set before proceeding. The final selected models were evaluated once on a held-out test set.

Multicollinearity was monitored throughout using the **Variance Inflation Factor (VIF)**.

---

## 2. OLS Linear Regression

### 2.1 Model Progression

All models predict `Log_SalePrice`. RMSE values on the validation set are reported on the original dollar scale for interpretability.

| Model | Features Added                                                         | R²        |
|-------|------------------------------------------------------------------------|-----------|
| 1     | Overall Score, House Age, TotalSF                                      | 0.8081    |
| 2     | + log(TotalSF) replaces TotalSF, + Years Since Remodel, + Garage Score | 0.8338    |
| 3     | + Neighborhood_Simplified, + Condition_Group                           | 0.8403    |
| 4     | + Has Fireplace, + Total Bath                                          | 0.8563    |
| 5     | + Mas Vnr Area, + Mas Vnr Type                                         | 0.8594    |
| 6     | + MS SubClass, + MS Zoning (Mas Vnr Type retained)                     | 0.8623    |
| **7** | **+ Sale Condition (MS Zoning dropped)**                               | **0.838** |
| 8     | + Bedroom AbvGr                                                        | 0.8638    |


> **Model 7 was selected as the final OLS model.**

### 2.2 Model-by-Model Rationale

**Model 1 — Baseline.** Three numerical features with the highest Pearson correlation to `SalePrice` were used: `Overall Score` (quality × condition), `House Age`, and `TotalSF`. The model achieved a strong baseline Adj. R² of 0.803, confirming that size, quality, and age are the primary price drivers. `TotalSF` showed a very large standard error, indicating scale instability that was corrected in Model 2.

**Model 2 — Log transform and garage.** `TotalSF` was replaced by `log(TotalSF)` to stabilise its coefficient. `Years Since Remodel` and `Garage Score` were added. The negative coefficient on both age features confirmed that older and less recently renovated houses command lower prices. Adj. R² improved by 3.1 points.

**Model 3 — Neighbourhood and proximity.** `Neighborhood_Simplified` (3-tier) and `Condition_Group` were introduced. Being in a higher-priced neighbourhood or near a positive proximity feature had significant positive coefficients, consistent with real estate theory. Adj. R² improved by 0.6 points.

**Model 4 — Bathroom count and fireplace.** Both `Has Fireplace` and `Total Bath` were statistically significant (p < 0.001) with positive coefficients, confirming that amenity count is a meaningful price predictor. Adj. R² improved by 1.6 points.

**Model 5 — Masonry veneer.** `Mas Vnr Area` and `Mas Vnr Type` were tested. Although Adj. R² improved marginally (+0.1 points), `Mas Vnr Area` showed a high standard error and a p-value of 0.696, making it statistically insignificant. The features were retained only briefly for further testing.

**Model 6 — Dwelling type and zoning.** `MS SubClass` (dwelling type) and `MS Zoning` (zoning classification) were added. Both had highly significant coefficients and produced the largest single-step gain since Model 1 (+0.5 points), reflecting that the type and legal classification of a property meaningfully affect price. `MS Zoning` ended up not being kept due to its high VIF.

**Model 7 — Sale condition (final model).** `Sale Condition` was added, with `Partial` (sale of an uncompleted house) emerging as the category with the largest positive coefficient. This produced the best Adj. R² of 0.864 and a validation RMSE of approximately $27,000 on the original scale.

**Model 8 — Bedroom count (rejected).** Adding `Bedroom AbvGr` produced a negligible R² gain while Adj. R² decreased slightly, indicating the added parameter did not justify its cost. Model 7 was retained.

### 2.3 Multicollinearity (VIF)

VIF was computed at each step. No feature in the final model exhibited a VIF above the conventional threshold of 10, indicating that multicollinearity was not a material concern. `House Age` and `Years Since Remodel` were the most correlated pair but remained within acceptable bounds.

### 2.4 Test Set Results

|         Metric        |   Value  |
|:---------------------:|:--------:|
|    RMSE (log scale)   |  0.1436  |
| RMSE (original scale) | ~$36,000 |

The test RMSE was notably higher than the validation RMSE (~$27,000). This gap is most likely attributable to the small size of each evaluation split (~439 rows), which makes RMSE on the original dollar scale sensitive to the distribution of high-priced houses in each split. 

A random excess of expensive properties in the test set amplifies errors non-linearly after the `exp()` back-transformation. Stratified splitting by price quantile is recommended to reduce this variance in future work.

---

## 3. Logistic Regression

### 3.1 Model Progression

All models predict the binary target `Is High Price` (1 = top price tercile, defined by training-set bins). Performance is reported on the validation set using Accuracy, F1 Score, and ROC-AUC.

| Model | Features Added                                                        | Accuracy        | F1              | ROC-AUC               |
|-------|-----------------------------------------------------------------------|-----------------|-----------------|-----------------------|
| 1     | Overall Score, House Age, log(TotalSF)                                | 0.9408          | 0.9182          | 0.9887                |
| 2     | + Has Garage, + Has Fireplace                                         | 0.9317          | 0.9057          | 0.9878                |
| 3     | + Has Fireplace (Garage removed), + Total Bath, + Years Since Remodel | 0.9362          | 0.9114          | 0.9910                |
| **4** | **+ Neighborhood Rank**                                               | 0.9499 **best** | 0.9308 **best** | 0.9906 **slightly ↓** |
| 5     | + Bedroom AbvGr                                                       | 0.9476          | 0.9274          | 0.9906                |

**Model 4 was selected as the final Logit model.**

### 3.2 Model-by-Model Rationale

**Model 1 — Baseline.** The same three baseline features from OLS were used, with `TotalSF` log-transformed for consistency. The baseline was remarkably strong: accuracy of 94.1%, F1 of 0.918, and a ROC-AUC of 0.989. This confirms that size, quality, and age are highly discriminative for the binary classification task.

**Model 2 — Binary flags.** `Has Garage` and `Has Fireplace` were added. Performance decreased overall. `Has Garage` had a p-value of 0.117 with a large standard error (1.064), indicating the model was not confident in its coefficient despite it being large in magnitude. This is characteristic of a near-collinear or low-variance binary predictor. `Has Fireplace` was significant (p < 0.001) and was retained.

**Model 3 — Bathrooms and recency.** `Has Garage` was removed. `Total Bath` and `Years Since Remodel` were added. `Total Bath` produced a coefficient of 0.649 (the strongest of any added feature), confirming that bathroom count is a major tier-breaker for high-price classification. This became the best model up to this point.

**Model 4 — Neighbourhood rank (final model).** Adding `Neighborhood Rank` produced the best Accuracy and F1 on the validation set. ROC-AUC decreased slightly, which was flagged as a potential early sign of overfitting, but overall discriminative performance was at its peak.

**Model 5 — Bedroom count (rejected).** Adding `Bedroom AbvGr` continued the downward trend in all metrics, consistent with overfitting as the model complexity increased beyond what the data could support.

### 3.3 Multicollinearity (VIF)

VIF was computed for each logistic model. No feature exceeded the threshold of 10. `House Age` and `Years Since Remodel` showed moderate correlation, consistent with the OLS findings, but remained acceptable.

### 3.4 Test Set Results

| Metric   | Value  |
|----------|--------|
| Accuracy | 0.9159 |
| F1 Score | 0.8869 |
| ROC-AUC  | 0.9757 |


The test results are 2–3 points lower than validation across all metrics. The most likely explanation is a combination of split sensitivity and feature fragility.

With approximately 439 rows per evaluation set, validation and test results are susceptible to distributional differences between splits. If the validation set happened to contain high-price houses that were more cleanly separable, Model 4 would appear stronger on validation than it truly generalises — and the test set reveals the more honest performance.

The specific feature that introduces fragility is Neighborhood Rank, which is what distinguishes Model 4 from Model 3. This rank is derived from training-set median prices, meaning neighbourhoods close to a tier boundary may not rank consistently with how houses actually sold in the test set. This introduces noise at the classification boundary and is reflected most clearly in the ROC-AUC drop, since ROC-AUC measures ranking quality across all thresholds rather than just at the 0.5 cutoff.

---

## 4. Conclusions

### 4.1 Overall Findings

Both models confirmed that residential sale prices are driven by a consistent and interpretable set of factors. Across OLS and Logit alike, the same core predictors dominated: **overall quality, total living area, house age, bathroom count, and neighbourhood tier**. This consistency across two fundamentally different modelling tasks strengthens confidence in those features as genuine drivers of value rather than statistical artefacts.

The log transformation of `SalePrice` was essential for OLS — without it, the skewed target distribution would have violated the normality and homoskedasticity assumptions underpinning inference. The same transformation applied to `TotalSF` in Model 2 further stabilised coefficients and improved model fit, demonstrating that scale matters as much as feature selection in linear modelling.

### 4.2 OLS Linear Regression

The final OLS model (Model 7) achieved an Adjusted R² of 0.864 on the training set and a validation RMSE of approximately $27,000, which is acceptable given the price range of the dataset. The iterative feature selection process was effective — each addition was justified by a meaningful gain in Adjusted R², and features that failed to justify their complexity (Model 5's `Mas Vnr Area`, Model 8's `Bedroom AbvGr`) were either dropped or rejected based on statistical insignificance or declining Adjusted R².

The test RMSE of ~$36,000 was higher than expected given validation performance, attributed primarily to the small split sizes and the non-linear amplification of errors on expensive properties after the `exp()` back-transformation. This is a limitation of the evaluation setup rather than a failure of the model itself.

### 4.3 Logistic Regression

The Logit models performed remarkably well from the very first iteration, with Model 1 already achieving a ROC-AUC of 0.989 on validation. This suggests that the binary classification boundary between high-price and non-high-price properties is relatively well-defined in the feature space — the three baseline features alone are sufficient to separate the top price tercile with high confidence.

The best model (Model 4) achieved a validation F1 of 0.931 and a test F1 of 0.887. The modest performance drop on the test set is largely attributable to the fragility of `Neighborhood Rank` across different sample distributions, rather than a structural overfitting problem. Model 3 — without neighbourhood — generalises more conservatively and may be the more robust choice in production.

### 4.4 Limitations

- **Small evaluation splits.** With approximately 439 rows each in validation and test, metric estimates carry meaningful variance. A single split can be lucky or unlucky with respect to the distribution of high-value properties, as evidenced by the OLS test gap. Stratified splitting by price quantile and k-fold cross-validation on the training set would produce more reliable performance estimates.

- **Neighbourhood encoding fragility.** `Neighborhood Rank` and `Neighborhood_Simplified` are both derived from training-set price statistics, making them sensitive to how neighbourhoods are represented in each split. In a real deployment scenario with new data, unseen or borderline neighbourhoods would fall back to default values that may not reflect actual price positioning.