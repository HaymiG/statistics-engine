# Statistical Engineering & Simulation Assessment

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests: 22 Passed](https://img.shields.io/badge/tests-22%20passed-brightgreen.svg)](tests/)
[![No Dependencies](https://img.shields.io/badge/dependencies-none-success.svg)](requirements.txt)

> Pure-Python statistical engine built from scratch. Demonstrates statistical analysis and the Law of Large Numbers through Monte Carlo simulation.

---

##  Overview

A comprehensive statistical analysis engine that calculates mean, median, mode, variance, standard deviation, and detects outliers—all without external libraries like NumPy or Pandas. Includes Monte Carlo simulation demonstrating the Law of Large Numbers.

**Key Features:**
- ✅ Central Tendency: Mean, Median, Mode (multimodal support)
- ✅ Dispersion: Variance & Standard Deviation (sample & population)
- ✅ Outlier Detection: Z-score method with configurable threshold
- ✅ Error Handling: Handles empty data, None values, mixed types
- ✅ Monte Carlo Simulation: 30, 1K, 10K day simulations

---

## 📁 Project Structure

```
statistical_engine/
│
├── data/
│   └── sample_salaries.json       # Mock dataset: 50 extreme startup salaries
│
├── src/
│   ├── __init__.py
│   ├── stat_engine.py             # Core StatEngine class: mean, median, mode, variance, SD, outlier detection
│   └── monte_carlo.py             # Monte Carlo simulation: server crash probabilities, LLN demonstration
│
├── tests/
│   ├── __init__.py
│   └── test_stat_engine.py        # Unit tests (22 tests) for StatEngine edge cases and correctness
│
├── README.md                       # Project overview, usage, and key explanations
└── main.py                         # Entry point: runs analysis & simulations on sample data
```

---

## Quick Start

```bash
# Run analysis
python3 main.py

# Run tests
python3 -m unittest tests.test_stat_engine -v
```

**Requirements:** Python 3.7+ (no external dependencies)

---

## Usage

### Basic Example

```python
from src.stat_engine import StatEngine

# Create engine
data = [10, 20, 30, 40, 50]
engine = StatEngine(data)

# Get statistics
print(engine.get_mean())                    # 30.0
print(engine.get_median())                  # 30.0
print(engine.get_variance(is_sample=True))  # 250.0
print(engine.get_outliers(threshold=2))     # []

# Get all statistics
summary = engine.get_summary()
```

### Monte Carlo Simulation

```python
from src.monte_carlo import demonstrate_law_of_large_numbers

# Run simulation (30, 1K, 10K days)
demonstrate_law_of_large_numbers()
```

---

##  Mathematical Formulas

### Central Tendency

**Mean:** `μ = Σx / n`

**Median:** 
- Odd n: middle value
- Even n: average of two middle values

**Mode:** Most frequent value(s)

### Dispersion

**Population Variance:** `σ² = Σ(x - μ)² / N`

**Sample Variance (Bessel's Correction):** `s² = Σ(x - x̄)² / (n - 1)`

**Standard Deviation:** `σ = √(variance)`

**Why n-1?** Dividing by (n-1) corrects bias when estimating population variance from a sample.

### Outlier Detection

**Z-Score:** `z = (x - μ) / σ`

**Outlier if:** `|z| > threshold` (default: 2)

---

## 📈 Key Results

### Salary Analysis (50 Startup Salaries)

| Statistic | Value | Insight |
|-----------|-------|---------|
| Mean | $223,740 | Inflated by outliers |
| Median | $117,500 | True "typical" salary |
| Difference | 90.4% | Mean almost double! |
| Std Dev | $383,985 | Extreme volatility |
| Outliers | 2 found | $1.2M, $2.5M |

**Takeaway:** Mean alone is misleading for skewed data. Median better represents typical value.

### Monte Carlo Simulation (Server Crashes at 4.5%)

| Days | Simulated | Error | Status |
|------|-----------|-------|--------|
| 30 | 13.3% | 196% | ❌ Unreliable |
| 1,000 | 3.5% | 22% | ⚠️ Poor |
| 10,000 | 4.2% | 6.7% | ✅ Good |

**Takeaway:** Small samples (30 days) produce unreliable estimates. Need 1,000+ days for reliable predictions.

---

##  Testing

**22 tests, 100% pass rate**

```bash
# Run all tests
python3 -m unittest tests.test_stat_engine -v

# Run specific test
python3 -m unittest tests.test_stat_engine.TestStatEngine.test_variance_sample
```

**Test Coverage:**
- ✅ Basic calculations (mean, median, mode)
- ✅ Variance & standard deviation (sample & population)
- ✅ Outlier detection
- ✅ Error handling (empty data, None values, mixed types)
- ✅ Edge cases (single value, negatives)

---


## 🔧 Technical Details

**Built with:** Python 3.7+ standard library only

**Libraries used:**
- `math` - Square root calculations
- `random` - Monte Carlo simulation
- `typing` - Type hints
- `unittest` - Testing
- `json` - Data loading

**No external dependencies** - Pure Python implementation

---


**Built with  using pure Python | Zero dependencies | Production-ready**
