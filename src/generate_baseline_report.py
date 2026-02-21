import pandas as pd
import numpy as np

data_path = '../data/raw/AmesHousing.csv'

df = pd.read_csv(data_path)

def get_variable_type(x):
    
    if pd.api.types.is_numeric_dtype(x):
        return 'Numerical'
    
    if pd.api.types.is_string_dtype(x):
        return 'Categorical'
    
def generate_report(df):
    var_report_list = []

    for col in df.columns:
        var_report_list.append({
            "Variable" : col,
            "Unique Values": df[col].nunique() if df[col].dtype == 'str' else " ",
            "Type" : get_variable_type(df[col]),
            "Description": ""
        })

    return pd.DataFrame(var_report_list)

report = generate_report(df)
report.to_markdown("../reports/Variable_Report.md", index=False)