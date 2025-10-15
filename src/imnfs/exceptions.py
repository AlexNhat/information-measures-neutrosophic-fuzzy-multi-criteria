"""
Custom exception definitions for the IMNFS computational framework.

These exceptions cover invalid indices, empty data, division errors,
type mismatches, and domain-specific issues in NF-based computations.
"""

# =====================================================================
# Base Exception
# =====================================================================

class IMNFSException(Exception):
    """Base class for all custom exceptions in the IMNFS framework."""
    pass


# =====================================================================
# Input / Index Errors
# =====================================================================

class InvalidIndexError(IMNFSException):
    """Raised when an invalid index (e.g., outside [0, 3]) is used."""
    def __init__(self, index=None, message=None):
        msg = message or (
            f"Invalid component index '{index}'. Expected a value between 0 and 3 (Mu, T, I, F)."
            if index is not None else
            "Invalid component index. Expected value between 0 and 3 (Mu, T, I, F)."
        )
        super().__init__(msg)


class EmptyDataError(IMNFSException):
    """Raised when attempting to compute with empty or None data."""
    def __init__(self, message=None):
        msg = message or "Input data is empty or None. Computation cannot proceed."
        super().__init__(msg)


class DataTypeError(IMNFSException):
    """Raised when data type is invalid (not list/ndarray or mismatched element types)."""
    def __init__(self, received_type=None, expected_type=None, message=None):
        msg = message or (
            f"Invalid data type: {received_type}. Expected: {expected_type or 'NumPy array or list'}."
        )
        super().__init__(msg)


class InvalidTypeError(IMNFSException):
    """Raised when a parameter has an invalid or unexpected Python type."""
    def __init__(self, var_name=None, expected_type=None, received_type=None, message=None):
        msg = message or (
            f"Invalid type for '{var_name}'. "
            f"Expected {expected_type or 'valid type'}, got {received_type}."
        )
        super().__init__(msg)


# =====================================================================
# Shape / Mathematical Errors
# =====================================================================

class ShapeMismatchError(IMNFSException):
    """Raised when two arrays or vectors have incompatible shapes."""
    def __init__(self, shape_a=None, shape_b=None, message=None):
        msg = message or (
            f"Shape mismatch: {shape_a} vs {shape_b}. Arrays must be broadcastable or have the same shape."
        )
        super().__init__(msg)


class DivisionByZeroError(IMNFSException):
    """Raised when a division by zero occurs."""
    def __init__(self, message=None):
        msg = message or "Division by zero occurred during computation."
        super().__init__(msg)


class NormalizationError(IMNFSException):
    """Raised when normalization fails due to invalid denominator or empty input."""
    def __init__(self, message=None):
        msg = message or "Normalization failed due to zero denominator or invalid input."
        super().__init__(msg)


class CalculationError(IMNFSException):
    """Raised when a general numerical computation fails."""
    def __init__(self, message=None):
        msg = message or "Numerical computation failed due to invalid values or overflow."
        super().__init__(msg)


# =====================================================================
# Domain-Specific Errors (for NF, RNF, Decision-making)
# =====================================================================

class NFComputationError(IMNFSException):
    """Raised when NFSet-related computation fails (e.g., complement or intersection)."""
    def __init__(self, message=None):
        msg = message or "Error occurred during NFSet computation."
        super().__init__(msg)


class SimilarityComputationError(IMNFSException):
    """Raised when similarity computation fails or returns invalid results."""
    def __init__(self, message=None):
        msg = message or "Failed to compute similarity between NF-elements."
        super().__init__(msg)


class WeightComputationError(IMNFSException):
    """Raised when weight calculation (entropy or cross-entropy) produces invalid values."""
    def __init__(self, message=None):
        msg = message or "Weight computation failed — check entropy or cross-entropy results."
        super().__init__(msg)


class DecisionError(IMNFSException):
    """Raised when the decision-making process (ranking, selection) encounters an issue."""
    def __init__(self, message=None):
        msg = message or "Decision-making process failed. Invalid data or scoring result."
        super().__init__(msg)

