from typing import List
import numpy as np
from imnfs.model.nfs import NFSet
from imnfs.exceptions import (
    EmptyDataError,
    DataTypeError,
    InvalidIndexError,
    NFComputationError,
)


class RNF:
    """
    RNF (Refined Neutrosophic Fuzzy operations) class
    - Stores NF-set data internally
    - Provides selective complement for specified indices
    """

    def __init__(self, nfs: NFSet, cost: list):
        """
        Initialize RNF with NFSet data.

        Args:
            nfs (NFSet): NFSet object containing NF-set elements
            cost (list): List of indices to apply complement
        """
        if not isinstance(nfs, NFSet):
            raise DataTypeError(type(nfs), "NFSet")

        if cost is None:
            raise EmptyDataError("Cost index list cannot be None.")

        if not all(isinstance(i, int) for i in cost):
            raise DataTypeError("Invalid element in cost list — must be integers.")

        if len(cost) == 0:
            self.data = nfs.data
        else:
            self.data = self.rnf(nfs, cost)

    # ----------------------------------------------------------------------
    # Core Operations
    # ----------------------------------------------------------------------

    def neg(self, vector):
        """Compute complement (negation) of a single NF-element."""
        if not isinstance(vector, (list, np.ndarray)):
            raise DataTypeError(type(vector))
        return 1 - np.array(vector, dtype=float)

    def rnf(self, nfs: NFSet, indices: List[int]):
        """Apply complement to elements at specified indices."""
        result = nfs.data.copy()

        for i in indices:
            if i < 0 or i >= len(result):
                raise InvalidIndexError(i)
            try:
                result[i] = self.neg(result[i])
            except Exception as e:
                raise NFComputationError(f"Complement at index {i} failed: {e}")

        return result
