import numpy as np
from typing import List
from .entropy_calculator import entropy_list, cross_entropy_pairwise
from src.imnfs.model import RNF


def compute_weight(rnf: RNF, index: int) -> List[float]:
    """
    Compute normalized weights for NF-elements based on entropy and cross-entropy.

    Args:
        rnf (RNF): RNF object containing NF-set data
        index (int): Index of component (Mu, T, I, F) to use in entropy calculations

    Returns:
        List[float]: Normalized weights (sum equals 1)
    """

    # Compute entropy values for the NF-set at the given index
    entropy_vals = np.array(entropy_list(rnf.data, index))

    # Compute cross-entropy values pairwise for the NF-set at the given index
    cross_entropy_vals = np.array(cross_entropy_pairwise(rnf.data, index))

    # Combine entropy and cross-entropy to compute raw weights
    # Formula: raw_weight = 1 - entropy + cross_entropy
    raw_weights = 1 - entropy_vals + cross_entropy_vals

    # Normalize weights so that their sum equals 1
    normalized_weights = raw_weights / np.sum(raw_weights)

    # Convert to list for compatibility with legacy code
    return normalized_weights.tolist()
