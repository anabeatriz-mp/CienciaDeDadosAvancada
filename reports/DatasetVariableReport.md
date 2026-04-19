# Dataset Variables Report
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
> The descriptions of each variable were obtained from the [Ames Housing Dataset Documentation]("https://jse.amstat.org/v19n3/decock/DataDocumentation.txt) by Dean De Cock,
Truman State University.


## Data Source

The dataset used is the Ames Housing Dataset, which contains **2,930 observations** and **82 variables** describing residential property sales in Ames, Iowa, from 2006 to 2010.

- Source: [Kaggle - Ames Housing Dataset](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset)
- Format: CSV
- Key Features: Includes nominal, ordinal, discrete, and continuous variables ranging from soil type to sale price.

---
## Variable Description Table

|     Variable    | Unique Values |     Type    |                           Description                           |
|:---------------:|:-------------:|:-----------:|:---------------------------------------------------------------:|
|      Order      |               |  Numerical  | Observation number                                              |
|       PID       |               | Categorical | Parcel identification number                                    |
|   MS SubClass   |               | Categorical | Identifies the type of dwelling involved in the sale            |
|    MS Zoning    |       7       | Categorical | Identifies the general zoning classification of the sale        |
|   Lot Frontage  |               |  Numerical  | Linear feet of street connected to property                     |
|     Lot Area    |               |  Numerical  | Lot size in square feet                                         |
|      Street     |       2       | Categorical | Type of road access to property                                 |
|      Alley      |       2       | Categorical | Type of alley access to property                                |
|    Lot Shape    |       4       | Categorical | General shape of property                                       |
|   Land Contour  |       4       | Categorical | Flatness of the property                                        |
|    Utilities    |       3       | Categorical | Type of utilities available                                     |
|    Lot Config   |       5       | Categorical | Lot configuration                                               |
|    Land Slope   |       3       | Categorical | Slope of property                                               |
|   Neighborhood  |       28      | Categorical | Physical locations within Ames city limits                      |
|   Condition 1   |       9       | Categorical | Proximity to various conditions                                 |
|   Condition 2   |       8       | Categorical | Proximity to various conditions (if more than one is present)   |
|    Bldg Type    |       5       | Categorical | Type of dwelling                                                |
|   House Style   |       8       | Categorical | Style of dwelling                                               |
|   Overall Qual  |               | Categorical  | Rates the overall material and finish of the house              |
|   Overall Cond  |               |  Numerical  | Rates the overall condition of the house                        |
|    Year Built   |               |  Numerical  | Original construction date                                      |
|  Year Remod/Add |               |  Numerical  | Remodel date                                                    |
|    Roof Style   |       6       | Categorical | Type of roof                                                    |
|    Roof Matl    |       8       | Categorical | Roof material                                                   |
|   Exterior 1st  |       16      | Categorical | Exterior covering on house                                      |
|   Exterior 2nd  |       17      | Categorical | Exterior covering on house (if more than one material)          |
|   Mas Vnr Type  |       4       | Categorical | Masonry veneer type                                             |
|   Mas Vnr Area  |               |  Numerical  | Masonry veneer area in square feet                              |
|    Exter Qual   |       4       | Categorical | Evaluates the quality of the material on the exterior           |
|    Exter Cond   |       5       | Categorical | Evaluates the present condition of the material on the exterior |
|    Foundation   |       6       | Categorical | Type of foundation                                              |
|    Bsmt Qual    |       5       | Categorical | Evaluates the height of the basement                            |
|    Bsmt Cond    |       5       | Categorical | Evaluates the general condition of the basement                 |
|  Bsmt Exposure  |       4       | Categorical | Refers to walkout or garden level walls                         |
|  BsmtFin Type 1 |       6       | Categorical | Rating of basement finished area                                |
|   BsmtFin SF 1  |               |  Numerical  | Type 1 finished square feet                                     |
|  BsmtFin Type 2 |       6       | Categorical | Rating of basement finished area (if multiple types)            |
|   BsmtFin SF 2  |               |  Numerical  | Type 2 finished square feet                                     |
|   Bsmt Unf SF   |               |  Numerical  | Unfinished square feet of basement area                         |
|  Total Bsmt SF  |               |  Numerical  | Total square feet of basement area                              |
|     Heating     |       6       | Categorical | Type of heating                                                 |
|    Heating QC   |       5       | Categorical | Heating quality and condition                                   |
|   Central Air   |       2       | Categorical | Central air conditioning                                        |
|    Electrical   |       5       | Categorical | Electrical system                                               |
|    1st Flr SF   |               |  Numerical  | First Floor square feet                                         |
|    2nd Flr SF   |               |  Numerical  | Second floor square feet                                        |
| Low Qual Fin SF |               |  Numerical  | Low quality finished square feet (all floors)                   |
|   Gr Liv Area   |               |  Numerical  | Above grade (ground) living area square feet                    |
|  Bsmt Full Bath |               |  Numerical  | Basement full bathrooms                                         |
|  Bsmt Half Bath |               |  Numerical  | Basement half bathrooms                                         |
|    Full Bath    |               |  Numerical  | Full bathrooms above grade                                      |
|    Half Bath    |               |  Numerical  | Half baths above grade                                          |
|  Bedroom AbvGr  |               |  Numerical  | Bedrooms above grade (does NOT include basement bedrooms)       |
|  Kitchen AbvGr  |               |  Numerical  | Kitchens above grade                                            |
|   Kitchen Qual  |       5       | Categorical | Kitchen quality                                                 |
|  TotRms AbvGrd  |               |  Numerical  | Total rooms above grade (does not include bathrooms)            |
|    Functional   |       8       | Categorical | Home functionality                                              |
|    Fireplaces   |               |  Numerical  | Number of fireplaces                                            |
|   Fireplace Qu  |       5       | Categorical | Fireplace quality                                               |
|   Garage Type   |       6       | Categorical | Garage location                                                 |
|  Garage Yr Blt  |               |  Numerical  | Year garage was built                                           |
|  Garage Finish  |       3       | Categorical | Interior finish of the garage                                   |
|   Garage Cars   |               |  Numerical  | Size of garage in car capacity                                  |
|   Garage Area   |               |  Numerical  | Size of garage in square feet                                   |
|   Garage Qual   |       5       | Categorical | Garage quality                                                  |
|   Garage Cond   |       5       | Categorical | Garage condition                                                |
|   Paved Drive   |       3       | Categorical | Paved driveway                                                  |
|   Wood Deck SF  |               |  Numerical  | Wood deck area in square feet                                   |
|  Open Porch SF  |               |  Numerical  | Open porch area in square feet                                  |
|  Enclosed Porch |               |  Numerical  | Enclosed porch area in square feet                              |
|    3Ssn Porch   |               |  Numerical  | Three season porch area in square feet                          |
|   Screen Porch  |               |  Numerical  | Screen porch area in square feet                                |
|    Pool Area    |               |  Numerical  | Pool area in square feet                                        |
|     Pool QC     |       4       | Categorical | Pool quality                                                    |
|      Fence      |       4       | Categorical | Fence quality                                                   |
|   Misc Feature  |       5       | Categorical | Miscellaneous feature not covered in other categories           |
|     Misc Val    |               |  Numerical  | $Value of miscellaneous feature                                 |
|     Mo Sold     |               |  Numerical  | Month Sold (MM)                                                 |
|     Yr Sold     |               |  Numerical  | Year Sold (YYYY)                                                |
|    Sale Type    |       10      | Categorical | Type of sale                                                    |
|  Sale Condition |       6       | Categorical | Condition of sale                                               |
|    SalePrice    |               |  Numerical  | Sale price $$                                                   |