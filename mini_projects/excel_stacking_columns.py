

import pandas as pd
def format_other_columns(row):
    # Convert the row to a dictionary without dropping any columns
    row_dict = row.to_dict()
    
    # Exclude the 'Project Name' and 'ID' columns from the dictionary
    excluded_keys = {'Project Name', 'ID'}
    filtered_dict = {k: v for k, v in row_dict.items() if k not in excluded_keys}
    
    formatted_items = []
    for k, v in filtered_dict.items():
        # Check if v is a list and join its elements into a string
        if isinstance(v, list):
            v = ', '.join(map(str, v))  # Use ',' as a separator, adjust if needed
        formatted_items.append(f'{k}: & {v} & ')
    
    # Join the formatted key-value pairs with a space and add a newline character between each pair
    return ' & '.join(formatted_items)

# ... rest of the script remains the same
# Read the Excel file
file_path = r'C:\Users\svilen.mitev\Desktop\New folder\mini_projects\test.xlsx'  # Updated file path
df = pd.read_excel(file_path, engine='openpyxl')  # Using the updated file path

# Apply the formatting function to each row, excluding the 'Project Name' column
df['Other Columns'] = df.apply(format_other_columns, axis=1)

# Keep only the 'Project Name' and 'Other Columns' columns
df = df[['ID', 'Project Name', 'Other Columns']]

# Write the DataFrame with the new columns to a new sheet in the same Excel file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:  # Using the updated file path
    df.to_excel(writer, sheet_name='Stacked Columns', index=False)
