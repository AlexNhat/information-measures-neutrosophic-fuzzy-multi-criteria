from typing import List, Union
import numpy as np
from imnfs.exceptions import (
    EmptyDataError,
    DataTypeError,
    ShapeMismatchError,
    NFComputationError,
)


class NFSet:
    """
    Neutrosophic Fuzzy Set (NFSet) with operations:
    subset, complement, intersection, union.
    Each element: [Mu, T, I, F]
    """

    def __init__(self, data: Union[List[List[float]], np.ndarray]):
        """
        Initialize NFSet with data.

        Args:
            data (List[List[float]] | np.ndarray): NF-set elements.
        """
        if data is None or (isinstance(data, (list, np.ndarray)) and len(data) == 0):
            raise EmptyDataError("NFSet cannot be initialized with empty data.")

        if not isinstance(data, (list, np.ndarray)):
            raise DataTypeError(type(data))

        arr = np.array(data, dtype=float)
        self.data = arr

    # ----------------------------------------------------------------------
    # Logical / Set Operations
    # ----------------------------------------------------------------------

    def issubset(self, other: "NFSet") -> bool:
        """Check if this NF-set is a subset of another NF-set."""
        if not isinstance(other, NFSet):
            raise DataTypeError(type(other), "NFSet")

        if self.data.shape != other.data.shape:
            raise ShapeMismatchError(self.data.shape, other.data.shape)

        return np.all(
            (self.data[:, 0] <= other.data[:, 0]) &  # Mu
            (self.data[:, 1] <= other.data[:, 1]) &  # T
            (self.data[:, 2] >= other.data[:, 2]) &  # I
            (self.data[:, 3] >= other.data[:, 3])    # F
        )

    def complement(self) -> "NFSet":
        """Compute the complement of this NF-set."""
        try:
            comp_data = np.stack([
                1 - self.data[:, 0],  # Mu_new
                self.data[:, 3],      # T_new
                1 - self.data[:, 2],  # I_new
                self.data[:, 1]       # F_new
            ], axis=1)
            return NFSet(comp_data)
        except Exception as e:
            raise NFComputationError(f"Failed to compute complement: {e}")

    def intersection(self, other: "NFSet") -> "NFSet":
        """Compute intersection with another NF-set."""
        if self.data.shape != other.data.shape:
            raise ShapeMismatchError(self.data.shape, other.data.shape)
        try:
            T = np.minimum(self.data[:, :2], other.data[:, :2])
            F = np.maximum(self.data[:, 2:], other.data[:, 2:])
            return NFSet(np.hstack([T, F]))
        except Exception as e:
            raise NFComputationError(f"Intersection failed: {e}")

    def union(self, other: "NFSet") -> "NFSet":
        """Compute union with another NF-set."""
        if self.data.shape != other.data.shape:
            raise ShapeMismatchError(self.data.shape, other.data.shape)
        try:
            T = np.maximum(self.data[:, :2], other.data[:, :2])
            F = np.minimum(self.data[:, 2:], other.data[:, 2:])
            return NFSet(np.hstack([T, F]))
        except Exception as e:
            raise NFComputationError(f"Union failed: {e}")

    def __repr__(self):
        return f"NFSet(\n{self.data}\n)"
