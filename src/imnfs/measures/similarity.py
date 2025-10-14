import numpy as np
import latexify
from .base import SimilarityMeasure

π = np.pi
e=np.e
def Delta(a: np.ndarray, b: np.ndarray)-> float:
    return a - b

def cot(x):
    return 1 / np.tan(x)
# --- Similarity 1 ---
class Similarity1(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_1"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        diff = Delta(a,b)
        t = np.cos(diff *π  / 4)
        out = (np.sqrt(2) + 1) / 4 * (np.sqrt(2) *np.sum(t) - 4)
        return out


# --- Similarity 2 ---
class Similarity2(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_2"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a,b))
        out = 1 - np.sum(t) / 4
        return out


# --- Similarity 3 ---
class Similarity3(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_3"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a,b))
        out = np.log2(2 - np.sum(t) / 4)
        return out


# --- Similarity 4 ---
class Similarity4(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_4"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a,b))
        out = 1 - np.log2(1 + np.sum(t) / 4)
        return out


# --- Similarity 5 ---
class Similarity5(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_5"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a,b))
        out = (e**(-np.sum(t) / 4) - e**(-1)) / (1 - e**(-1))
        return out


# --- Similarity 6 ---
class Similarity6(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_6"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a,b))
        out = 1 - np.sin(np.sum(t) * π / 8)
        return out


# --- Similarity 7 ---
class Similarity7(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_7"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a,b))
        out = np.cos(np.sum(t) * π / 8)
        return out


# --- Similarity 8 ---
class Similarity8(SimilarityMeasure):
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_8"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a,b))
        out = 1 - np.tan(np.sum(t) * π / 16)
        return out


# --- Similarity 9 ---
class Similarity9:
    @staticmethod
    @latexify.function(
        identifiers={"compute": "Similarity_9"},
        reduce_assignments=True,
        use_math_symbols=True
    )
    def compute(a: np.ndarray, b: np.ndarray) -> float:
        t = np.abs(Delta(a, b))
        out = cot(π / 4 + np.sum(t) * π / 16)
        return out