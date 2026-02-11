import pandas as pd

grades=pd.Series([85,None,92,45,None,78,55])
original_series=grades.isnull()
filled_series=grades.fillna(0)
filtered_results = filled_series[filled_series > 60]
print(grades)
print(original_series)
print(filled_series)
print(filtered_results)