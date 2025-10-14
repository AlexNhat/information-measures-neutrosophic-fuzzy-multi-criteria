import numpy as np
from .similarity_calculator import compute_similarity

def entropy_with_complement(vectors, k):
    """
    Tính entropy của từng phần tử dựa trên vector phần bù (1 - x).
    
    Args:
        vectors: List các vector NF-element
        k: Index của chỉ số Mu/T/I/F cần tính
    Returns:
        float: Trung bình entropy
    """
    complement_vectors = [[1 - x for x in vec] for vec in vectors]
    return np.mean([compute_similarity(vectors[i], complement_vectors[i])[k] 
                    for i in range(len(vectors))])


def entropy_list(nf_elements, k):
    """
    Tính entropy cho danh sách các NF-element.
    
    Args:
        nf_elements: List các NF-element (mỗi phần tử là list vector)
        k: Index của chỉ số cần tính
    Returns:
        List[float]: Entropy của từng phần tử
    """
    return [entropy_with_complement(elem, k) for elem in nf_elements]


def cross_entropy_pairwise(vectors, k):
    """
    Tính cross-entropy giữa các phần tử (1 - similarity) theo từng cặp.
    
    Args:
        vectors: List các vector NF-element
        k: Index của chỉ số cần tính
    Returns:
        List[float]: Cross-entropy cho từng phần tử
    """
    n = len(vectors)
    out = []
    for i in range(n):
        temp = sum(1 - compute_similarity(vectors[i], vectors[j])[k] for j in range(n) if j != i)
        out.append(temp / (n - 1))
    return out


def cross_entropy_list(nf_elements, k):
    """
    Trung bình cross-entropy cho danh sách các NF-element.
    
    Args:
        nf_elements: List các NF-element
        k: Index của chỉ số cần tính
    Returns:
        List[float]: Trung bình cross-entropy cho từng phần tử
    """
    return [np.mean(cross_entropy_pairwise(elem, k)) for elem in nf_elements]
