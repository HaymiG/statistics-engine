"""
StatEngine: A pure-Python statistical analysis engine
Implements core statistical methods from scratch using only built-in libraries.
"""

from typing import List, Union, Optional
import math


class StatEngine:
    """
    A statistical engine for analyzing 1D numerical data.
    
    Attributes:
        data (List[float]): Cleaned numerical data
        raw_data: Original input data
    """
    
    def __init__(self, data: Union[List, tuple]):
        """
        Initialize the StatEngine with data.
        
        Args:
            data: Input data (list or tuple)
            
        Raises:
            TypeError: If data contains non-numeric values after cleaning
            ValueError: If data is empty after cleaning
        """
        self.raw_data = data
        self.data = self._clean_data(data)
        
        if len(self.data) == 0:
            raise ValueError("Cannot initialize StatEngine with empty data after cleaning")
    
    def _clean_data(self, data: Union[List, tuple]) -> List[float]:
        """
        Clean data by removing None values and converting to float.
        
        Args:
            data: Raw input data
            
        Returns:
            List of cleaned float values
            
        Raises:
            TypeError: If non-numeric values are encountered
        """
        cleaned = []
        for item in data:
            if item is None:
                continue
            try:
                cleaned.append(float(item))
            except (ValueError, TypeError):
                raise TypeError(
                    f"Invalid data type encountered: {type(item).__name__}. "
                    f"All values must be numeric or None."
                )
        return cleaned
    
    def get_mean(self) -> float:
        """
        Calculate the arithmetic mean (average).
        
        Formula: μ = (Σx) / n
        Where:
            Σx = sum of all values
            n = number of values
        
        Returns:
            The mean value
        """
        return sum(self.data) / len(self.data)
    
    def get_median(self) -> float:
        """
        Calculate the median (middle value).
        
        Logic:
            - For odd n: median = middle value
            - For even n: median = average of two middle values
        
        Returns:
            The median value
        """
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 0:  # Even number of elements
            # Average of two middle values
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:  # Odd number of elements
            return sorted_data[mid]
    
    def get_mode(self) -> Union[List[float], str]:
        """
        Calculate the mode(s) - most frequently occurring value(s).
        
        Handles multimodal distributions by returning all modes.
        
        Returns:
            List of mode values, or message if all values are unique
        """
        # Count frequency of each value
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        
        # Find maximum frequency
        max_freq = max(frequency.values())
        
        # If all values appear only once
        if max_freq == 1:
            return "No mode: all values are unique"
        
        # Return all values with maximum frequency
        modes = [value for value, freq in frequency.items() if freq == max_freq]
        return sorted(modes)
    
    def get_variance(self, is_sample: bool = True) -> float:
        """
        Calculate variance (measure of spread).
        
        Formulas:
            Population Variance: σ² = Σ(x - μ)² / N
            Sample Variance: s² = Σ(x - x̄)² / (n - 1)  [Bessel's correction]
        
        Where:
            x = individual values
            μ or x̄ = mean
            N or n = number of values
            (n - 1) = Bessel's correction for sample variance
        
        Args:
            is_sample: If True, use sample variance (n-1); if False, use population variance (n)
        
        Returns:
            The variance value
        """
        mean = self.get_mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        sum_squared_diffs = sum(squared_diffs)
        
        if is_sample:
            # Sample variance with Bessel's correction
            return sum_squared_diffs / (len(self.data) - 1)
        else:
            # Population variance
            return sum_squared_diffs / len(self.data)
    
    def get_standard_deviation(self, is_sample: bool = True) -> float:
        """
        Calculate standard deviation (square root of variance).
        
        Formulas:
            Population SD: σ = √(σ²)
            Sample SD: s = √(s²)
        
        Args:
            is_sample: If True, use sample SD; if False, use population SD
        
        Returns:
            The standard deviation value
        """
        variance = self.get_variance(is_sample=is_sample)
        return math.sqrt(variance)
    
    def get_outliers(self, threshold: float = 2) -> List[float]:
        """
        Detect outliers using standard deviation method.
        
        Logic:
            An outlier is a value that is more than 'threshold' standard
            deviations away from the mean.
            
            |x - μ| > threshold × σ
        
        Args:
            threshold: Number of standard deviations (default: 2)
        
        Returns:
            List of outlier values
        """
        mean = self.get_mean()
        std_dev = self.get_standard_deviation(is_sample=True)
        
        outliers = []
        for value in self.data:
            # Calculate how many standard deviations away from mean
            z_score = abs(value - mean) / std_dev
            if z_score > threshold:
                outliers.append(value)
        
        return sorted(outliers)
    
    def get_summary(self) -> dict:
        """
        Get a comprehensive statistical summary.
        
        Returns:
            Dictionary containing all statistical measures
        """
        return {
            'count': len(self.data),
            'mean': self.get_mean(),
            'median': self.get_median(),
            'mode': self.get_mode(),
            'variance_sample': self.get_variance(is_sample=True),
            'variance_population': self.get_variance(is_sample=False),
            'std_dev_sample': self.get_standard_deviation(is_sample=True),
            'std_dev_population': self.get_standard_deviation(is_sample=False),
            'outliers_2sd': self.get_outliers(threshold=2),
            'min': min(self.data),
            'max': max(self.data)
        }
