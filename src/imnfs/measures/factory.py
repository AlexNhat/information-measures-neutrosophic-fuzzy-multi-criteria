from typing import List
from .base import SimilarityMeasure
from .similarity import (
    Similarity1,
    Similarity2,
    Similarity3,
    Similarity4,
    Similarity5,
    Similarity6,
    Similarity7,
    Similarity8,
    Similarity9,
)

def get_measures(selected: List[str] = None) -> List[SimilarityMeasure]:
    """Get a list of similarity measures, optionally filtered by names.
    
    Args:
        selected: List of class names to include (e.g., ['Similarity1', 'Similarity2']).
        If None, return all measures.
    
    Returns:
        List of SimilarityMeasure instances.
    """
    all_measures = [
        Similarity1(),
        Similarity2(),
        Similarity3(),
        Similarity4(),
        Similarity5(),
        Similarity6(),
        Similarity7(),
        Similarity8(),
        Similarity9(),
    ]
    if selected:
        return [m for m in all_measures if m.__class__.__name__ in selected]
    return all_measures