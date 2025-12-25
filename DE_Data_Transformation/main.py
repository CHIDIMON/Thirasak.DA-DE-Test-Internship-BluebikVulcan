import pandas as pd

#prepare mock data
data = {
    'Column 1': ['A', 'D', 'I', 'X', 'I', 'N', 'Q'],
    'Column 2': ['B', 'E', 'J', 'Y', 'M', 'O', 'S'],
    'Column 3': ['Type A', 'Type A', 'Type A', 'Type B', 'Type B', 'Type B', 'Type B']
}
df = pd.DataFrame(data)

#use groupby and apply to transform Column 2 based on the next row's Column 1 within each group of Column 3
def transform_column(group):
    # pull the next row's Column 1 values using shift(-1)
    shifted_c1 = group['Column 1'].shift(-1)
    
    #replace Column 2 with the shifted Column 1 values
    #only for rows where Column 2 is not null
    group['Column 2'] = shifted_c1.fillna(group['Column 2'])
    
    return group

#run the transformation
output_df = df.groupby('Column 3', group_keys=False).apply(transform_column)

#show the output
print(output_df)