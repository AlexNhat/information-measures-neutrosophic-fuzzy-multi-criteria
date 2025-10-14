from typing import List
import numpy as np

class NFSet:
    """
    Neutrosophic Fuzzy Set (NFSet) with operations: subset, complement, intersection, union.
    Each element: [Mu, T, I, F]
    """

    def __init__(self, data: List[List[float]]):
        """
        Initialize NFSet with data.

        Args:
            data (List[List[float]]): NF-set elements.
        """
        self.data = np.array(data, dtype=float)

    def issubset(self, other: "NFSet") -> bool:
        """
        Check if this NF-set is a subset of another NF-set.

        Args:
            other (NFSet): Another NF-set to compare with.

        Returns:
            bool: True if self is subset of other, False otherwise.
        """
        return np.all(
            (self.data[:, 0] <= other.data[:, 0]) &  # Mu
            (self.data[:, 1] <= other.data[:, 1]) &  # T
            (self.data[:, 2] >= other.data[:, 2]) &  # I
            (self.data[:, 3] >= other.data[:, 3])    # F
        )

    def complement(self) -> "NFSet":
        """
        Compute the complement of this NF-set according to the original formula:
        Mu_new = 1 - Mu
        T_new = F
        I_new = 1 - I
        F_new = T
        """
        comp_data = np.stack([
            1 - self.data[:, 0],  # Mu_new
            self.data[:, 3],      # T_new
            1 - self.data[:, 2],  # I_new
            self.data[:, 1]       # F_new
        ], axis=1)
        return NFSet(comp_data)

    def intersection(self, other: "NFSet") -> "NFSet":
        """
        Compute intersection with another NF-set.

        Logic:
            min for truth-memberships (Mu, T)
            max for falsity-memberships (I, F)

        Args:
            other (NFSet): Another NF-set.

        Returns:
            NFSet: Intersection of self and other.
        """
        T = np.minimum(self.data[:, :2], other.data[:, :2])
        F = np.maximum(self.data[:, 2:], other.data[:, 2:])
        return NFSet(np.hstack([T, F]))

    def union(self, other: "NFSet") -> "NFSet":
        """
        Compute union with another NF-set.

        Logic:
            max for truth-memberships (Mu, T)
            min for falsity-memberships (I, F)

        Args:
            other (NFSet): Another NF-set.

        Returns:
            NFSet: Union of self and other.
        """
        T = np.maximum(self.data[:, :2], other.data[:, :2])
        F = np.minimum(self.data[:, 2:], other.data[:, 2:])
        return NFSet(np.hstack([T, F]))

    def __repr__(self):
        return f"NFSet(\n{self.data}\n)"
