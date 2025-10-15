# Project Setup Instructions

This document provides instructions to set up the `imnfs` project.

## Prerequisites

- **Python**: Version >=3.10, <3.12
- **Poetry**: Version >=2.0.0, <3.0.0

## Installation Steps

1. **Install Poetry**  
   If Poetry is not installed, use **one of the following methods**:

   **Method 1: Official installer**

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   
   **Method 2: Using pip**

   ```bash
   pip install poetry
   ```

   Verify the installation:
   ```bash
   poetry --version
   ```

2. **Clone the Project Repository**  
   Clone the repository:
   ```bash
   git clone https://github.com/AlexNhat/information-measures-neutrosophic-fuzzy-multi-criteria.git
   ```

3. **Set Up the Virtual Environment**  
   Create a virtual environment and install dependencies:
   ```bash
   poetry install
   ```

4. **Activate the Virtual Environment**  
   Activate the Poetry virtual environment:
   ```bash
   poetry shell
   ```