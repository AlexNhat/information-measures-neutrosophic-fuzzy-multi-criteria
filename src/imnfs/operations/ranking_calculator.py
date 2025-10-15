import numpy as np
from imnfs.model import RNF
from .similarity_calculator import compute_similarity
from .weight_calculator import compute_weight  # assuming compute_weight is here


def compute_positive_similarity_scores(rnf: RNF, index: int) -> list:
    """
    Compute positive scores for each column of the NF-set.

    Args:
        rnf: RNF object or 3D array of NF-elements
        index (int): index of component to use

    Returns:
        List of positive scores per column
    """
    # Define positive reference vector
    pos = np.array([1, 1, 0, 0], dtype=float)
    
    weights = np.array(compute_weight(rnf, index))
    out = []
    
    for i in range(rnf.data.shape[1]):
        temp = np.sum([weights[j] * compute_similarity(rnf.data[j][i], pos)[index]
                    for j in range(rnf.data.shape[0])])
        out.append(temp)

    return out


def compute_negative_similarity_scores(rnf: RNF, index: int) -> list:
    """
    Compute negative scores for each column of the NF-set.

    Args:
        rnf: RNF object or 3D array of NF-elements
        index (int): index of component to use

    Returns:
        List of negative scores per column
    """
    # Define negative reference vector
    neg = np.array([0, 0, 1, 1], dtype=float)

    weights = np.array(compute_weight(rnf, index))
    out = []

    for i in range(rnf.data.shape[1]):
        temp = np.sum([weights[j] * compute_similarity(rnf.data[j][i], neg)[index]
                    for j in range(rnf.data.shape[0])])
        out.append(temp)

    return out


def compute_normalized_scores(rnf: RNF, index: int) -> list:
    """
    Compute final scores for each column as Spos / (Spos + Sneg).

    Args:
        rnf: RNF object or 3D array of NF-elements
        index (int): index of component to use

    Returns:
        List of normalized scores per column
    """
    spos_scores = np.array(compute_positive_similarity_scores(rnf, index))
    sneg_scores = np.array(compute_negative_similarity_scores(rnf, index))

    # calculate score
    scores = spos_scores / (spos_scores + sneg_scores)

    return scores.tolist()
