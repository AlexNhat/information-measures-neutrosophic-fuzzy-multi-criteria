from typing import List
from .nfs import NFSet  # Import NFSet class containing the NF-set data

class RNF:
    """
    RNF (Refined Neutrosophic Fuzzy operations) class
    - Stores NF-set data internally
    - Provides methods to compute negation (complement) of elements
    - Allows selective complement for specified elements
    """

    def __init__(self, nfs: NFSet, cost: list):
        """
        Initialize RNF with NFSet data.

        Args:
            nfs (NFSet): NFSet object containing NF-set elements
            cost (list): List of indices to apply complement
                    If empty, the data remains unchanged
        """
        # If no indices are provided, keep the original data
        if len(cost) == 0:
            self.data = nfs.data
        else:
            # If indices are provided, apply selective complement
            self.data = self.rnf(nfs, cost)

    def neg(self, vector):
        """
        Compute the complement (negation) of a single NF-element.

        Args:
            vector: A single NF-element (array or list)

        Returns:
            np.ndarray: NF-element after complement
        """
        return 1 - vector

    def rnf(self, nfs: NFSet, indices: List):
        """
        Apply complement to elements at specified indices.

        Args:
            indices (List): List of element indices to complement

        Returns:
            np.ndarray: NF-set with selected elements complemented
        """
        # Make a copy to avoid modifying the original data
        result = nfs.data.copy()
        for i in indices:
            # Ensure the index is valid
            if 0 <= i < len(result):
                result[i] = self.neg(result[i])
        return result
