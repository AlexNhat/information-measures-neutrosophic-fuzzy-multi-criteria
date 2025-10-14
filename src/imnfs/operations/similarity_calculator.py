import numpy as np
from typing import List
from src.imnfs.measures import get_measures

def compute_similarity(a: np.ndarray, b: np.ndarray) ->List[float]:
    """
    Calculate all similarity measures between two NF-set vectors.

    Args:
        a (array-like): First NF-set vector.
        b (array-like): Second NF-set vector.

    Returns:
        List[float]: Similarity values for each measure.
    """
    similarity_list = get_measures()
    result = [sim.compute(a, b) for sim in similarity_list]

    return result
