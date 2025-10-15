import numpy as np
from .similarity_calculator import compute_similarity
from typing import List


def entropy_with_complement(vectors: List[List[float]], k: int) -> float:
    """
    Compute the entropy of each NF-element based on its complement vector (1 - x).

    The entropy is calculated as the mean similarity between each element
    and its complement across all NF-elements.

    Args:
        vectors (List[List[float]]): A list of NF-element vectors.
        k (int): The index of the membership degree to compute (0: Mu, 1: T, 2: I, 3: F).

    Returns:
        float: Mean entropy value for the given index k.
    """
    # Generate complement vectors (1 - x)
    complement_vectors = [[1 - x for x in vec] for vec in vectors]

    # Compute similarity between each element and its complement, take the k-th index
    similarities = [
        compute_similarity(vectors[i], complement_vectors[i])[k]
        for i in range(len(vectors))
    ]
    return np.mean(similarities)


def entropy_list(nf_elements: np.ndarray, k: int) -> List[float]:
    """
    Compute entropy values for a list of NF-elements.

    Each NF-element is represented as a set of membership vectors,
    and the entropy is computed using its complement.

    Args:
        nf_elements (np.ndarray): Array of NF-elements (each element is a list of vectors).
        k (int): The index of the membership degree to compute.

    Returns:
        List[float]: A list of entropy values for each NF-element.
    """
    return [entropy_with_complement(elem, k) for elem in nf_elements]


def cross_entropy_pairwise(vectors: List[List[float]], k: int) -> List[float]:
    """
    Compute pairwise cross-entropy between NF-elements.

    Cross-entropy is defined as the average dissimilarity (1 - similarity)
    between each element and all others in the same set.

    Args:
        vectors (List[List[float]]): A list of NF-element vectors.
        k (int): The index of the membership degree to compute.

    Returns:
        List[float]: Cross-entropy values for each element.
    """
    n = len(vectors)
    out = []
    for i in range(n):
        # Compute average dissimilarity (1 - similarity)
        temp = np.mean([
            1 - compute_similarity(vectors[i], vectors[j])[k]
            for j in range(n) if j != i
        ])
        out.append(temp)
    return out


def cross_entropy_list(nf_elements: np.ndarray, k: int) -> List[float]:
    """
    Compute average cross-entropy for a list of NF-elements.

    Each NF-element group contributes one mean cross-entropy value.

    Args:
        nf_elements (np.ndarray): Array of NF-elements (each element is a list of vectors).
        k (int): The index of the membership degree to compute.

    Returns:
        List[float]: Mean cross-entropy for each NF-element.
    """
    return [np.mean(cross_entropy_pairwise(elem, k)) for elem in nf_elements]
