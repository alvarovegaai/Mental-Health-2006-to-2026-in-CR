import pandas as pd

def compute_gap_analysis(input_path='data/processed/master_health_matrix.csv'):
    # Load the integrated master matrix
    df = pd.read_csv(input_path)
    
    # Calculate the Residual Gap
    # Using academic prevalence baseline (normalized 0.1-0.3 range)
    # vs CCSS treated counts
    df['estimated_untreated'] = (df['prevalence_study_index'] * 1000000) - df['treated_count']
    
    # Export the analytical findings
    output_path = 'data/processed/analytical_gap_results.csv'
    df.to_csv(output_path, index=False)
    print(f"Analytical gap results saved to {output_path}")

if __name__ == "__main__":
    compute_gap_analysis()
