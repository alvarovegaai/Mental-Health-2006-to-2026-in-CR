import pandas as pd
import os

def run_master_integration(directory_path='data/raw/'):
    # Initialize master dataframe with the year range
    master_df = pd.DataFrame({'year': range(2006, 2027)})
    
    # Iterate through all files and merge into master_df
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            
            # Merge on 'year' to ensure data alignment
            master_df = pd.merge(master_df, df, on='year', how='left')
    
    # Save the integrated matrix for processing
    output_path = 'data/processed/master_health_matrix.csv'
    master_df.to_csv(output_path, index=False)
    return master_df

if __name__ == "__main__":
    print("Executing Master Integration...")
    master_data = run_master_integration()
    print("Success: Integrated matrix saved to /data/processed/master_health_matrix.csv")
