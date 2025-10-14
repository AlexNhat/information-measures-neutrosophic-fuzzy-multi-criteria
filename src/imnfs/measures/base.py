from abc import ABC, abstractmethod
import numpy as np

class SimilarityMeasure(ABC):
    @staticmethod
    @abstractmethod
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        """Compute similarity between two NFS vectors."""
        pass
