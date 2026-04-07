"""
Main entry point for Statistical Engineering & Simulation Assessment
Demonstrates StatEngine capabilities and Monte Carlo simulation.
"""

import json
from src.stat_engine import StatEngine
from src.monte_carlo import demonstrate_law_of_large_numbers


def load_salary_data():
    """Load salary data from JSON file."""
    with open('data/sample_salaries.json', 'r') as f:
        data = json.load(f)
    return data['salaries']


def analyze_salaries():
    """Analyze startup salary data and demonstrate statistical concepts."""
    print("\n" + "="*80)
    print("PART 1: STATISTICAL ENGINE ANALYSIS - STARTUP SALARIES")
    print("="*80 + "\n")
    
    # Load data
    salaries = load_salary_data()
    print(f"Loaded {len(salaries)} salary records\n")
    
    # Create StatEngine instance
    engine = StatEngine(salaries)
    
    # Get comprehensive summary
    summary = engine.get_summary()
    
    # Display results
    print("CENTRAL TENDENCY MEASURES:")
    print("-" * 40)
    print(f"Mean (Average):        ${summary['mean']:,.2f}")
    print(f"Median (Middle):       ${summary['median']:,.2f}")
    print(f"Mode (Most Common):    {summary['mode']}")
    
    print("\n\nDISPERSION MEASURES:")
    print("-" * 40)
    print(f"Sample Variance:       ${summary['variance_sample']:,.2f}")
    print(f"Population Variance:   ${summary['variance_population']:,.2f}")
    print(f"Sample Std Dev:        ${summary['std_dev_sample']:,.2f}")
    print(f"Population Std Dev:    ${summary['std_dev_population']:,.2f}")
    
    print("\n\nRANGE:")
    print("-" * 40)
    print(f"Minimum Salary:        ${summary['min']:,.2f}")
    print(f"Maximum Salary:        ${summary['max']:,.2f}")
    print(f"Range:                 ${summary['max'] - summary['min']:,.2f}")
    
    print("\n\nOUTLIER DETECTION (2 Standard Deviations):")
    print("-" * 40)
    if summary['outliers_2sd']:
        print(f"Found {len(summary['outliers_2sd'])} outlier(s):")
        for outlier in summary['outliers_2sd']:
            print(f"  ${outlier:,.2f}")
    else:
        print("No outliers detected")
    
    # Calculate additional insights
    mean_median_diff = summary['mean'] - summary['median']
    mean_median_diff_pct = (mean_median_diff / summary['median']) * 100
    
    print("\n\n" + "="*80)
    print("STATISTICAL INTERPRETATION & INSIGHTS")
    print("="*80)
    
    print(f"""
1. MEAN vs MEDIAN DISCREPANCY:
   - Mean:   ${summary['mean']:,.2f}
   - Median: ${summary['median']:,.2f}
   - Difference: ${mean_median_diff:,.2f} ({mean_median_diff_pct:.1f}%)
   
   The mean is {mean_median_diff_pct:.1f}% HIGHER than the median, indicating a
   RIGHT-SKEWED distribution. This means a few extremely high salaries are
   pulling the average up.

2. WHY MEAN ALONE IS DANGEROUS:
   - If you only look at the mean (${summary['mean']:,.2f}), you might think
     this is the "typical" salary
   - But 50% of employees earn LESS than ${summary['median']:,.2f} (the median)
   - The mean is inflated by executive/founder salaries
   
3. STANDARD DEVIATION REVEALS VOLATILITY:
   - Sample SD: ${summary['std_dev_sample']:,.2f}
   - This massive standard deviation shows EXTREME salary variation
   - About 68% of salaries fall within ±${summary['std_dev_sample']:,.2f} of the mean
   - Range: ${summary['mean'] - summary['std_dev_sample']:,.2f} to ${summary['mean'] + summary['std_dev_sample']:,.2f}
   
4. OUTLIERS IDENTIFIED:
   - {len(summary['outliers_2sd'])} salaries are statistical outliers (>2 SD from mean)
   - These are likely C-suite executives or founders with equity compensation
   - Removing outliers would give a more realistic picture for typical employees

5. SAMPLE vs POPULATION VARIANCE:
   - Sample Variance: ${summary['variance_sample']:,.2f} (uses n-1, Bessel's correction)
   - Population Variance: ${summary['variance_population']:,.2f} (uses n)
   - We use SAMPLE variance because this is a sample of startup salaries,
     not the entire population of all startup employees
    """)
    
    print("="*80 + "\n")


def main():
    """Run the complete analysis."""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "  STATISTICAL ENGINEERING & SIMULATION ASSESSMENT".center(78) + "║")
    print("║" + "  Pure Python Implementation".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝")
    
    # Part 1: Statistical Engine Analysis
    analyze_salaries()
    
    # Part 2: Monte Carlo Simulation - Law of Large Numbers
    print("\n" + "="*80)
    print("PART 2: MONTE CARLO SIMULATION - LAW OF LARGE NUMBERS")
    print("="*80 + "\n")
    
    demonstrate_law_of_large_numbers()
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print("\nTo run unit tests, execute: python -m unittest tests.test_stat_engine")
    print("\n")


if __name__ == "__main__":
    main()
