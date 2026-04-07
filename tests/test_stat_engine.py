"""
Unit tests for StatEngine class.
Tests all statistical methods and edge cases.
"""

import unittest
import math
from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):
    """Test suite for StatEngine class."""
    
    def test_mean_basic(self):
        """Test mean calculation with simple data."""
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.get_mean(), 3.0)
    
    def test_mean_decimals(self):
        """Test mean with decimal values."""
        engine = StatEngine([1.5, 2.5, 3.5])
        self.assertAlmostEqual(engine.get_mean(), 2.5, places=5)
    
    def test_median_odd_length(self):
        """Test median with odd number of elements."""
        engine = StatEngine([1, 3, 5, 7, 9])
        self.assertEqual(engine.get_median(), 5.0)
    
    def test_median_even_length(self):
        """Test median with even number of elements."""
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)
    
    def test_median_unsorted(self):
        """Test median with unsorted data."""
        engine = StatEngine([9, 1, 5, 3, 7])
        self.assertEqual(engine.get_median(), 5.0)
    
    def test_mode_single(self):
        """Test mode with single mode."""
        engine = StatEngine([1, 2, 2, 3, 4])
        self.assertEqual(engine.get_mode(), [2.0])
    
    def test_mode_multimodal(self):
        """Test mode with multiple modes."""
        engine = StatEngine([1, 1, 2, 2, 3])
        self.assertEqual(engine.get_mode(), [1.0, 2.0])
    
    def test_mode_all_unique(self):
        """Test mode when all values are unique."""
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.get_mode(), "No mode: all values are unique")
    
    def test_variance_population(self):
        """Test population variance calculation."""
        engine = StatEngine([2, 4, 6, 8, 10])
        # Mean = 6, squared diffs = [16, 4, 0, 4, 16], sum = 40, variance = 40/5 = 8
        self.assertAlmostEqual(engine.get_variance(is_sample=False), 8.0, places=5)
    
    def test_variance_sample(self):
        """Test sample variance with Bessel's correction."""
        engine = StatEngine([2, 4, 6, 8, 10])
        # Same as above but divide by n-1: 40/4 = 10
        self.assertAlmostEqual(engine.get_variance(is_sample=True), 10.0, places=5)
    
    def test_standard_deviation_population(self):
        """Test population standard deviation."""
        engine = StatEngine([2, 4, 6, 8, 10])
        # sqrt(8) ≈ 2.828
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=False), 
                              math.sqrt(8), places=5)
    
    def test_standard_deviation_sample(self):
        """Test sample standard deviation."""
        engine = StatEngine([2, 4, 6, 8, 10])
        # sqrt(10) ≈ 3.162
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=True), 
                              math.sqrt(10), places=5)
    
    def test_outliers_detection(self):
        """Test outlier detection."""
        # Data with clear outliers
        engine = StatEngine([10, 12, 11, 13, 12, 100, 11, 10])
        outliers = engine.get_outliers(threshold=2)
        self.assertIn(100.0, outliers)
    
    def test_outliers_no_outliers(self):
        """Test outlier detection with no outliers."""
        engine = StatEngine([10, 11, 12, 13, 14])
        outliers = engine.get_outliers(threshold=2)
        self.assertEqual(len(outliers), 0)
    
    def test_empty_data_raises_error(self):
        """Test that empty data raises ValueError."""
        with self.assertRaises(ValueError):
            StatEngine([])
    
    def test_none_values_cleaned(self):
        """Test that None values are removed during cleaning."""
        engine = StatEngine([1, 2, None, 3, None, 4])
        self.assertEqual(len(engine.data), 4)
        self.assertEqual(engine.get_mean(), 2.5)
    
    def test_mixed_types_raises_error(self):
        """Test that mixed non-numeric types raise TypeError."""
        with self.assertRaises(TypeError):
            StatEngine([1, 2, 'abc', 4])
    
    def test_string_numbers_converted(self):
        """Test that string numbers are converted to float."""
        engine = StatEngine(['1', '2', '3'])
        self.assertEqual(engine.get_mean(), 2.0)
    
    def test_all_none_raises_error(self):
        """Test that all None values raise ValueError."""
        with self.assertRaises(ValueError):
            StatEngine([None, None, None])
    
    def test_single_value(self):
        """Test with single value."""
        engine = StatEngine([5])
        self.assertEqual(engine.get_mean(), 5.0)
        self.assertEqual(engine.get_median(), 5.0)
        self.assertEqual(engine.get_variance(is_sample=False), 0.0)
    
    def test_negative_values(self):
        """Test with negative values."""
        engine = StatEngine([-5, -3, -1, 1, 3, 5])
        self.assertEqual(engine.get_mean(), 0.0)
        self.assertEqual(engine.get_median(), 0.0)
    
    def test_summary_method(self):
        """Test the summary method returns all statistics."""
        engine = StatEngine([1, 2, 3, 4, 5])
        summary = engine.get_summary()
        
        self.assertIn('mean', summary)
        self.assertIn('median', summary)
        self.assertIn('mode', summary)
        self.assertIn('variance_sample', summary)
        self.assertIn('variance_population', summary)
        self.assertIn('std_dev_sample', summary)
        self.assertIn('std_dev_population', summary)
        self.assertIn('outliers_2sd', summary)
        self.assertIn('min', summary)
        self.assertIn('max', summary)


if __name__ == '__main__':
    unittest.main()
