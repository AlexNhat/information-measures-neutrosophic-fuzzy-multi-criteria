import numpy as np
from imnfs.model import RNF
from imnfs.operations import compute_normalized_scores
from imnfs.exceptions import InvalidTypeError, InvalidIndexError, CalculationError


class DecisionMaker:
    """
    DecisionMaker handles the final stage of NF-based MCDM:
    computes scores, ranks alternatives, and identifies the best one.
    """

    def __init__(self, rnf: RNF, index: int):
        """
        Initialize DecisionMaker.

        Args:
            rnf (RNF): RNF object (contains 3D NF data array)
            index (int): Index of the component (Mu/T/I/F)
        """
        if not isinstance(rnf, RNF):
            raise InvalidTypeError("rnf must be an instance of RNF.")
        if not isinstance(index, int):
            raise InvalidTypeError("index must be an integer.")
        if not (0 <= index < 4):
            raise InvalidIndexError("index must be between 0 and 3 (Mu/T/I/F).")

        self.rnf = rnf
        self.index = index

    def rank(self) -> np.ndarray:
        """
        Rank all alternatives in ascending order based on their final scores.

        Returns:
            np.ndarray: Rank indices (1 = lowest rank)
        """
        try:
            scores = compute_normalized_scores(self.rnf, self.index)
            if not isinstance(scores, np.ndarray):
                raise CalculationError("compute_normalized_scores must return a NumPy array.")
            return np.argsort(scores) + 1
        except Exception as e:
            raise CalculationError(f"Error during ranking computation: {e}")

    def best_alternative(self) -> int:
        """
        Return the index of the best alternative (highest score).

        Returns:
            int: Index of the best alternative (1-based)
        """
        try:
            scores = compute_normalized_scores(self.rnf, self.index)
            if not isinstance(scores, np.ndarray):
                raise CalculationError("compute_normalized_scores must return a NumPy array.")
            return int(np.argmax(scores) + 1)
        except Exception as e:
            raise CalculationError(f"Error during best alternative selection: {e}")
