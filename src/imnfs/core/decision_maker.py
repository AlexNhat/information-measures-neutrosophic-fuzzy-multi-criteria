import numpy as np
from imnfs.model import RNF
from imnfs.operations import compute_normalized_scores

class DecisionMaker:
    """
    DecisionMaker handles the final stage of NF-based MCDM:
    computes scores, ranks alternatives, and identifies the best one.
    """

    def __init__(self, rnf: RNF, index: int):
        """
        Initialize DecisionMaker.

        Args:
            rnf: RNF object (contains 3D data array)
            index (int): Index of the component (Mu/T/I/F)
        """
        self.rnf = rnf
        self.index = index

    def rank(self) -> np.ndarray:
        """
        Rank all alternatives in ascending order based on their final scores.

        Returns:
            np.ndarray: Rank indices (1 = lowest rank)
        """
        scores = compute_normalized_scores(self.rnf, self.index)
        return np.argsort(scores) + 1

    def best_alternative(self) -> int:
        """
        Return the index of the best alternative (highest score).

        Returns:
            int: Index of the best alternative (1-based)
        """
        scores = compute_normalized_scores(self.rnf, self.index)
        return int(np.argmax(scores) + 1)

