import json
import pandas as pd
import numpy as np
from pathlib import Path

from imnfs.exceptions import (
    EmptyDataError,
    DataTypeError,
    InvalidTypeError,
    ShapeMismatchError,
)


class DataLoader:
    """Handles loading and validation of structured numeric data."""

    SUPPORTED_FORMATS = (".json", ".txt", ".csv", ".xlsx")

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self._validate_path()

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def _validate_path(self):
        """Check file existence and extension validity."""
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")

        if self.filepath.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise InvalidTypeError(
                var_name="file extension",
                expected_type=self.SUPPORTED_FORMATS,
                received_type=self.filepath.suffix,
                message=f"Unsupported file format '{self.filepath.suffix}'. "
                        f"Supported: {', '.join(self.SUPPORTED_FORMATS)}"
            )

    # --------------------------------------------------
    # Dispatcher
    # --------------------------------------------------

    def load(self) -> np.ndarray:
        """Dispatch file loading based on extension."""
        ext = self.filepath.suffix.lower()

        if ext == ".json":
            data = self._load_json()
        elif ext == ".txt":
            data = self._load_txt()
        elif ext == ".csv":
            data = self._load_csv()
        elif ext == ".xlsx":
            data = self._load_xlsx()
        else:
            raise InvalidTypeError(
                var_name="file extension",
                expected_type=self.SUPPORTED_FORMATS,
                received_type=ext
            )

        if data is None or len(data) == 0:
            raise EmptyDataError(f"No data found in file: {self.filepath}")

        return self._to_numpy(data)

    # --------------------------------------------------
    # File-specific loaders
    # --------------------------------------------------

    def _load_json(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError as e:
            raise DataTypeError(received_type="JSON", message=f"Invalid JSON file: {e}")

    def _load_txt(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                lines = [line.strip().split() for line in f if line.strip()]
            return lines
        except Exception as e:
            raise DataTypeError(received_type="TXT", message=f"Error reading TXT file: {e}")

    def _load_csv(self):
        try:
            df = pd.read_csv(self.filepath)
            return df.values.tolist()
        except Exception as e:
            raise DataTypeError(received_type="CSV", message=f"Error reading CSV file: {e}")

    def _load_xlsx(self):
        try:
            df = pd.read_excel(self.filepath)
            return df.values.tolist()
        except Exception as e:
            raise DataTypeError(received_type="XLSX", message=f"Error reading Excel file: {e}")

    # --------------------------------------------------
    # Convert & Validate
    # --------------------------------------------------

    def _to_numpy(self, data):
        """Convert data to NumPy array and ensure numeric values."""
        try:
            arr = np.array(data, dtype=float)
        except Exception:
            raise DataTypeError(
                received_type=type(data).__name__,
                expected_type="numeric matrix (list[list[float]])",
                message="Data contains non-numeric or invalid entries."
            )
            
        return arr


# =====================================================================
# Helper function (shortcut)
# =====================================================================

def load_data(filepath: str) -> np.ndarray:
    """
    Quick utility wrapper to load data file and return NumPy array.

    Example:
        >>> data = load_data("data/sample.json")
    """
    return DataLoader(filepath).load()
