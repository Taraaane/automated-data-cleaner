#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

def clean_data(input_file, output_file):
    print(f"📥 Reading data from '{input_file}'...")
    
    try:
        # 1. Load the messy dataset
        df = pd.read_csv(input_file)
        initial_rows = df.shape[0]
        
        # 2. Remove duplicate rows
        df.drop_duplicates(inplace=True)
        duplicates_removed = initial_rows - df.shape[0]
        print(f"🧹 Removed {duplicates_removed} duplicate row(s).")
        
        # 3. Handle missing values
        # Fill missing numerical values with the column mean
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
        
        # Fill missing text values with 'Unknown'
        string_cols = df.select_dtypes(include=['object']).columns
        for col in string_cols:
            df[col] = df[col].fillna('Unknown')
            
        # 4. Normalize data formats
        # Standardize column names (lowercase and replace spaces with underscores)
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        
        # Strip extra whitespace and convert all text values to lowercase
        for col in string_cols:
            df[col] = df[col].astype(str).str.strip().str.lower()
            
        # 5. Save the cleaned dataset
        df.to_csv(output_file, index=False)
        print(f"✅ Cleaned data successfully saved to '{output_file}'!")
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found. Please check the path.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Define input and output file paths
    input_csv = "messy_data.csv"
    output_csv = "clean_data.csv"
    
    clean_data(input_csv, output_csv)

