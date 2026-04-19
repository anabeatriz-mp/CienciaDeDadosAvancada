# Preprocessing Report

> [!IMPORTANT]
> The Jupyter Notebook this report relies on can be found in [`notebooks\AmesHousing\preprocessing.ipynb`](https://github.com/anabeatriz-mp/CienciaDeDadosAvancada/blob/master/notebooks/AmesHousing/preprocessing.ipynb).


## 1. Dataset & Train/Validation/Test Split

The raw dataset was loaded from `data\raw\AmesHousing.csv`. To ensure all preprocessing parameters (imputation values, encoding maps, target bins) were derived exclusively from training data and applied to the remaining splits, the dataset was divided before any transformation was performed.

The split strategy used was a two-step random split with `random_state=42` for reproducibility:

- **Train:** 70% of the data
- **Validation:** 15% of the data
- **Test:** 15% of the data

This produced approximately 2,051 training rows, 439 validation rows, and 439 test rows.

---

## 2. Missing Value Handling

Missing values were categorised into two groups depending on whether their absence carried semantic meaning.

### 2.1 Structural Missingness

Structural missing values are those where `NaN` reflects the genuine absence of a feature rather than a data entry error — for example, a house with no garage, no pool, or no alley access.

For these features, the imputation strategy was:
- **Categorical features** → filled with the string `"None"`, preserving the absence as an interpretable category.
- **Numerical features** → filled with `0`, representing the absence of a quantity.

The following features were treated as structural:

| Type | Features |
|---|---|
| Categorical | Alley, Bsmt Qual, Bsmt Cond, Bsmt Exposure, BsmtFin Type 1, BsmtFin Type 2, Fireplace Qu, Garage Type, Garage Finish, Garage Qual, Garage Cond, Pool QC, Fence, Misc Feature, Mas Vnr Type |
| Numerical | Garage Yr Blt, Garage Cars, Garage Area, BsmtFin SF 1, BsmtFin SF 2, Bsmt Unf SF, Total Bsmt SF, Bsmt Full Bath, Bsmt Half Bath, Mas Vnr Area |

Two cases required a judgement call:

- **`Mas Vnr Area` / `Mas Vnr Type`**: It could not be confirmed whether missing values represent houses with no masonry veneer or data entry errors. Both were treated as structural for simplification, since their missingness was highly co-occurring.
- **Basement group** (`BsmtFin SF 1`, `BsmtFin SF 2`, `Bsmt Unf SF`, `Total Bsmt SF`, `Bsmt Full Bath`, `Bsmt Half Bath`): Missing values in this group always occurred simultaneously, suggesting a single underlying cause. Treated as structural given the low count and co-occurrence pattern.

### 2.2 Non-Structural Missingness

Two features were considered non-structural, meaning their missingness could not be attributed to the absence of the feature itself.

**`Lot Frontage`** had a meaningful number of missing values that correlated with neighbourhood characteristics. It was imputed using the **median `Lot Frontage` of the corresponding neighbourhood**, computed from the training set only. A global training median was used as a fallback for any unseen neighbourhood in the validation or test sets.

**`Electrical`** had a single missing value, treated as missing completely at random. It was imputed with the **mode of the training set**.

---

## 3. Feature Engineering

Several new features were created to capture domain knowledge about real estate pricing and to improve signal quality for the models.

### 3.1 Binary Presence Flags

Two binary indicators were created to capture whether a desirable feature was present at all, as correlation analysis indicated that presence/absence had a stronger signal than the underlying ordinal values.

- **`Has Fireplace`**: 1 if `Fireplaces > 0`, else 0.
- **`Has Garage`**: 1 if `Garage Area > 0`, else 0.

### 3.2 Bathroom Count

Real estate listings typically present a single bathroom figure. A weighted sum was computed following the industry convention of counting half-bathrooms at 50%:

```
Total Bath = Full Bath + 0.5 × Half Bath + Bsmt Full Bath + 0.5 × Bsmt Half Bath
```

### 3.3 Composite Quality & Condition Scores

Several quality and condition attributes share the same ordinal scale (`Ex=5, Gd=4, TA=3, Fa=2, Po=1, None=0`). Additive composite scores were created to reduce dimensionality while preserving ordinality:

- **`Overall Score`** = `Overall Qual + Overall Cond`
- **`Garage Score`** = `Garage Qual (mapped) + Garage Cond (mapped)`
- **`Kitchen Score`** = `Kitchen Qual (mapped) × Kitchen AbvGr`

An additive formulation was chosen to avoid the symmetry problem of multiplication, where a score of `(1, 5)` would equal `(5, 1)` despite representing meaningfully different conditions.

### 3.4 Age & Modernity Features

Two time-based features were derived to capture the depreciation and renovation effects on pricing:

- **`House Age`** = `Yr Sold − Year Built` (clipped at 0)
- **`Years Since Remodel`** = `Yr Sold − Year Remod/Add` (clipped at 0)

Both were clipped at 0 to prevent negative values arising from data entry inconsistencies.

### 3.5 Total Square Footage

A single area metric was constructed combining above-ground and basement living space, reflecting how listings typically advertise total usable area:

```
TotalSF = Gr Liv Area + Total Bsmt SF
```

### 3.6 Neighbourhood Rank

Neighbourhoods were ranked by their median `SalePrice` in the training set, producing an ordinal numeric variable from 0 (lowest median price) to N−1 (highest).

### 3.7 Target Variable Transformation

`SalePrice` follows a right-skewed distribution, as is typical for property prices. A log transformation was applied to produce `Log_SalePrice`, which approximates a normal distribution and is required for the OLS assumptions to hold.

```
Log_SalePrice = log(SalePrice)
```

---

## 4. Categorical Simplification

### 4.1 Neighbourhood Tiers

With 28 distinct neighbourhoods, using raw neighbourhood dummies would introduce a large number of parameters with limited observations per category. Neighbourhoods were collapsed into three tiers based on their **median price per square foot**, computed from the training set:

- **`Tier_1_Budget`**: bottom 33rd percentile of median price/SF
- **`Tier_2_Mid`**: 33rd–66th percentile
- **`Tier_3_Luxury`**: top 33rd percentile

Any neighbourhood unseen in the validation or test sets defaults to the training median tier.

### 4.2 Proximity Conditions

`Condition 1` and `Condition 2` described proximity to various features (roads, railways, parks). These were merged into a single three-category variable `Condition_Group`:

- **`Positive`**: proximity to a park or positive feature (`PosN`, `PosA`)
- **`Negative`**: proximity to an arterial road or railway (`Artery`, `Feedr`, `RRNn`, `RRAn`, `RRNe`, `RRAe`)
- **`Normal`**: all other cases

The original columns were dropped after encoding.

---

## 5. Classification Target

For the logistic regression task, a binary target `Is High Price` was created by splitting `SalePrice` into terciles. The tercile boundaries were computed **from the training set only** using `pd.qcut`, then applied to the validation and test sets via `pd.cut` with fixed bin edges. This ensures a consistent and leak-free definition of "High Price" across all splits.

```
Is High Price = 1 if Price Tier == "High" (top third of training prices), else 0
```

---

## 6. Final Verification

After all transformations, each split was checked for remaining missing values. All three datasets passed with zero missing values before export.

The processed splits were exported to:
- `data/processed/train.csv`
- `data/processed/val.csv`
- `data/processed/test.csv`