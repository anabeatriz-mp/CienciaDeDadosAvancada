# Missing Values Report

In this document we can see the Missingness Classification of each of the features in our dataset and the explanation as to why.

To see how I've reached these conclusions in more detail check the jupyter notebook in `notebooks\AmesHousing\missing_analysis.ipynb`.



> [!NOTE]
> On the [Documentation<sup>[1]</sup>](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt) it is said that most features have missing values because the characteristic simply doesn't exist on the property, i.e most of the variables have **structural missing data**.
> For example: 
>- Property doesn't have Pool
>- Property doesn't have Fireplace
>- Property doesn't have Garages
>- Property doesn't have Basement

## Missingness Table


|   **Column**   | **Missingness Classification** |                                                                                         **Justification**                                                                                        |
|:--------------:|:------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  Lot Frontage  |               MAR              | By running statistical tests we can verify that the missing values of Lot Frontage are related to other features.                                                                                |
|      Alley     |           Structural           | Documentation<sup>[1]</sup> - NA = No alley access                                                                                                                                               |
|  Mas Vnr Type  |        Structural / MCAR       | Most of Type values are missing when Mas Vnr Area = 0. Rest of missing values happen when Area is also missing.                                                                                  |
|  Mas Vnr Area  |        Structural / MCAR       | All missing values happen when Type is missing. `NaN` values might be input errors or simply Area = 0, there is no way of confirming that.                                                       |
|    Bsmt Qual   |           Structural           | Documentation<sup>[1]</sup> - NA = No Basement                                                                                                                                                   |
|    Bsmt Cond   |           Structural           | Documentation<sup>[1]</sup> - NA = No Basement                                                                                                                                                   |
|  Bsmt Exposure |           Structural           | Documentation<sup>[1]</sup> - NA = No Basement                                                                                                                                                   |
| BsmtFin Type 1 |           Structural           | Documentation<sup>[1]</sup> - NA = No Basement                                                                                                                                                   |
|  BsmtFin SF 1  |        Structural / MCAR       | Analyzing the missing values heatmap there is a group with only 1 missing value that happen at the same time.  Might be an input error on the whole row or simply no Basement.                   |
| BsmtFin Type 2 |           Structural           | Documentation<sup>[1]</sup> - NA = No Basement                                                                                                                                                   |
|  BsmtFin SF 2  |        Structural / MCAR       | Analyzing the missing values heatmap there is a group with only 1 missing value that happen at the same time.  Might be an input error on the whole row or simply no Basement.                   |
|   Bsmt Unf SF  |        Structural / MCAR       | Analyzing the missing values heatmap there is a group with only 1 missing value that happen at the same time.  Might be an input error on the whole row or simply no Basement.                   |
|  Total Bsmt SF |        Structural / MCAR       | Analyzing the missing values heatmap there is a group with only 1 missing value that happen at the same time.  Might be an input error on the whole row or simply no Basement.                   |
|   Electrical   |              MCAR              | A single missing value which has no apparent correlation to anything.                                                                                                                            |
| Bsmt Full Bath |        Structural / MCAR       | Altough this column has 2 missing values, it is part on the "1 missing value Basement group" and the other one happens when Half Bath is missing as well. Might be input errors or no basements. |
| Bsmt Half Bath |        Structural / MCAR       | Altough this column has 2 missing values, it is part on the "1 missing value Basement group" and the other one happens when Full Bath is missing as well. Might be input errors or no basements. |
|  Fireplace Qu  |           Structural           | Documentation<sup>[1]</sup> - NA = No Fireplace                                                                                                                                                  |
|   Garage Type  |           Structural           | Documentation<sup>[1]</sup> - NA = No Garage                                                                                                                                                     |
|  Garage Yr Blt |           Structural           | Not mentioned on documentation but by analyzing the missing value heatmap, seems missing when other garage variables are missing                                                                 |
|  Garage Finish |           Structural           | Documentation<sup>[1]</sup> - NA = No Garage                                                                                                                                                     |
|   Garage Cars  |           Structural           | Only one missing value, and it is missing when there is no Garage on other Garage group variables.                                                                                               |
|   Garage Area  |           Structural           | Only one missing value, and it is missing when there is no Garage on other Garage group variables.                                                                                               |
|   Garage Qual  |           Structural           | Documentation<sup>[1]</sup> - NA = No Garage                                                                                                                                                     |
|   Garage Cond  |           Structural           | Documentation<sup>[1]</sup> - NA = No Garage                                                                                                                                                     |
|     Pool QC    |           Structural           | Documentation<sup>[1]</sup> - NA = No Pool                                                                                                                                                       |
|      Fence     |           Structural           | Documentation<sup>[1]</sup> - NA = No Fence                                                                                                                                                      |
|  Misc Feature  |           Structural           | Documentation<sup>[1]</sup> - NA = None                                                                                                                                                          |