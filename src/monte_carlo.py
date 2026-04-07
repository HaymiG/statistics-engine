"""
Monte Carlo Simulation for Server Crash Probability
Demonstrates the Law of Large Numbers through simulation.
"""

import random
from typing import Dict, List


def simulate_crashes(days: int, crash_probability: float = 0.045) -> Dict:
    """
    Simulate server crashes over a given number of days.
    
    The Law of Large Numbers states that as the number of trials increases,
    the experimental probability converges to the theoretical probability.
    
    Args:
        days: Number of days to simulate
        crash_probability: Theoretical probability of crash per day (default: 0.045 = 4.5%)
    
    Returns:
        Dictionary containing simulation results:
            - days: Number of days simulated
            - crashes: Total number of crashes
            - simulated_probability: Observed crash rate
            - theoretical_probability: Expected crash rate
            - error: Absolute difference from theoretical
            - error_percentage: Percentage error
    """
    crashes = 0
    
    # Simulate each day
    for _ in range(days):
        # Generate random number between 0 and 1
        # If it's less than crash_probability, a crash occurs
        if random.random() < crash_probability:
            crashes += 1
    
    # Calculate simulated probability
    simulated_prob = crashes / days
    
    # Calculate error metrics
    error = abs(simulated_prob - crash_probability)
    error_percentage = (error / crash_probability) * 100
    
    return {
        'days': days,
        'crashes': crashes,
        'simulated_probability': simulated_prob,
        'theoretical_probability': crash_probability,
        'error': error,
        'error_percentage': error_percentage
    }


def run_multiple_simulations(days_list: List[int], crash_probability: float = 0.045) -> List[Dict]:
    """
    Run simulations for multiple day counts.
    
    Args:
        days_list: List of day counts to simulate
        crash_probability: Theoretical crash probability
    
    Returns:
        List of simulation results
    """
    results = []
    for days in days_list:
        result = simulate_crashes(days, crash_probability)
        results.append(result)
    return results


def print_simulation_results(results: List[Dict]):
    """
    Print formatted simulation results.
    
    Args:
        results: List of simulation result dictionaries
    """
    print("\n" + "="*80)
    print("MONTE CARLO SIMULATION: SERVER CRASH PROBABILITY")
    print("="*80)
    print(f"\nTheoretical Crash Probability: 4.5% (0.045)")
    print("\n" + "-"*80)
    
    for result in results:
        print(f"\nSimulation: {result['days']:,} days")
        print(f"  Total Crashes: {result['crashes']:,}")
        print(f"  Simulated Probability: {result['simulated_probability']:.6f} ({result['simulated_probability']*100:.3f}%)")
        print(f"  Error from Theoretical: {result['error']:.6f} ({result['error_percentage']:.2f}%)")
        print(f"  Convergence: {'GOOD' if result['error_percentage'] < 10 else 'POOR'}")
    
    print("\n" + "="*80)
    print("LAW OF LARGE NUMBERS INTERPRETATION")
    print("="*80)
    print("""
As the number of days increases, the simulated probability converges toward
the theoretical probability of 4.5%. This demonstrates the Law of Large Numbers:

- Small samples (30 days): High variance, unreliable for predictions
- Medium samples (1,000 days): Better convergence, but still some error
- Large samples (10,000 days): Very close to theoretical value

DANGER FOR STARTUP:
Using only 30 days of data to predict yearly maintenance budget is EXTREMELY
RISKY because:
1. Small sample size leads to high variance in estimates
2. Could underestimate (e.g., 2% observed) or overestimate (e.g., 7% observed)
3. Budget could be off by 50-100% or more
4. Need at least 1,000+ days of data for reliable predictions
    """)
    print("="*80 + "\n")


def demonstrate_law_of_large_numbers():
    """
    Demonstrate the Law of Large Numbers with server crash simulations.
    """
    # Set random seed for reproducibility (optional)
    random.seed(42)
    
    # Run simulations for different sample sizes
    days_to_simulate = [30, 1000, 10000]
    results = run_multiple_simulations(days_to_simulate)
    
    # Print results
    print_simulation_results(results)
    
    return results
