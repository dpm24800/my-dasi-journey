import pandas as pd

# Create a sample DataFrame
data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
df = pd.DataFrame(data, index=['row_a', 'row_b', 'row_c'])
print("Original DataFrame:")
print(df)

# Rename specific row labels using a dictionary
new_df = df.rename(index={'row_a': 'new_row_1', 'row_c': 'new_row_3'})
print("\nDataFrame after renaming specific rows:")
print(new_df)

# Rename row labels using a function or lambda expression
# This example converts all index labels to uppercase
new_df_func = df.rename(index=lambda x: x.upper())
print("\nDataFrame after renaming rows using a function:")
print(new_df_func)

# Rename row labels in place
df.rename(index={'row_b': 'updated_row_b'}, inplace=True)
print("\nDataFrame after in-place renaming:")
print(df)


'''
# Explanation:
- df.rename(index={'old_label': 'new_label'})
    This is the most common way to rename specific row labels. You pass a dictionary to the index parameter, where keys are the current row labels and values are the new desired labels.
- df.rename(index=lambda x: x.upper())
    You can also provide a function (including lambda functions) to the index parameter. This function will be applied to each existing index label to generate the new label.
- inplace=True: 
    If you want to modify the DataFrame directly without creating a new one, set inplace=True. Otherwise, the rename() method returns a new DataFrame with the updated index labels.
'''