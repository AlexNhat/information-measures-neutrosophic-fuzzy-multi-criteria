# Examples

This page walks you through using the `imnfs` library to perform multi-criteria decision-making (MCDM) with neutrosophic fuzzy sets (NF-sets). We'll focus on generating sample data, initializing the necessary objects, and evaluating decisions using the 9 similarity measures.

You'll learn how to:
- Generate random NF-set data for testing.
- Initialize `NFSet` and `RNF` objects.
- Use `DecisionMaker` to compute and select the best alternative for each similarity measure.
- Interpret the results for decision support.

While this section is by no means a comprehensive guide to the library's features, it will give you a solid idea of the basics and how to apply them to your own MCDM problems. Let's get started!

## Info: The Art of Handling Uncertainty
Building reliable MCDM models under uncertainty is challenging. NF-sets provide a powerful way to model imprecise, indeterminate, and inconsistent data. The `imnfs` library simplifies this by offering tools for similarity-based information measures (entropy, cross-entropy) and decision algorithms. Designing your data and criteria carefully ensures accurate and robust outcomes.

## Preparing the Environment
Before getting started, make sure you've:
- Installed Python 3.10 or higher.
- Installed the library via pip:  
  ```
  pip install git+https://github.com/AlexNhat/information-measures-neutrosophic-fuzzy-multi-criteria.git
  ```

Tip: Download the Code  
The runnable code for this example can be found in the repository's examples/ folder or adapted from the snippets below.

## Overview
We'll implement the example in the following steps:
- Create a function to generate random NF-set data.
- Initialize the NF-set and reduced NF representation (RNF).
- Evaluate decisions using all 9 similarity measures and print the best alternatives.

## Getting Started
We'll implement the entire example in a single script, but in real-world use cases, you might split it into modules for better organization.

```python
import random
from imnfs import DecisionMaker, NFSet, RNF

def nf_random_set(o, c, seed=7):
    """
    Generate a nested list representing an NF-set with random values.
    
    The structure is [c][o][4]:
        - c: number of outer groups (e.g., criteria or cases)
        - o: number of elements in each group
        - 4: NF parameters (T, I, F, Mu or similar)
    
    Each value is a random float between 0.1 and 0.9.
    
    Args:
        o (int): Number of elements in the innermost list
        c (int): Number of outer lists
        seed (int, optional): Random seed for reproducibility. Defaults to 7.

    Returns:
        list: Nested list [c][o][4] with random floats
    """
    random.seed(seed)
    out = []

    # Loop through each group (outer list)
    for _ in range(c):
        out_c = []

        # Loop through each element in the group
        for _ in range(o):
            # Create a list of 4 random floats between 0.1 and 0.9
            out_o = [random.randint(1, 9)/10 for _ in range(4)]
            out_c.append(out_o)

        # Append the group to the output list
        out.append(out_c)
    
    return out


# ------------------------
# Create a sample NF-set
# ------------------------
nf_arr = nf_random_set()
# Initialize NFSet from the random data
nfs = NFSet(nf_arr)

# Initialize RNF; cost can be empty or default
cost = []
rnf = RNF(nfs, cost)

# Use DecisionMaker to select the best alternative for each case
for i in range(9):
    dm = DecisionMaker(rnf, i).best_alternative()
    print("Similarity no.", i+1, ":", dm)
```

### Sample Data Generation
The `nf_random_set` function creates a nested list simulating NF-set data. With `seed=7`, `o=4` (alternatives), and `c=5` (criteria), the generated `nf_arr` looks like this:

```
[[[0.6, 0.3, 0.7, 0.1], [0.2, 0.9, 0.2, 0.6], [0.1, 0.9, 0.4, 0.1], [0.2, 0.7, 0.7, 0.2]],
 [[0.4, 0.2, 0.9, 0.7], [0.1, 0.2, 0.4, 0.1], [0.7, 0.1, 0.4, 0.1], [0.9, 0.3, 0.5, 0.7]],
 [[0.3, 0.9, 0.2, 0.5], [0.9, 0.3, 0.2, 0.4], [0.6, 0.2, 0.9, 0.2], [0.1, 0.4, 0.8, 0.9]],
 [[0.7, 0.6, 0.8, 0.8], [0.6, 0.5, 0.4, 0.3], [0.4, 0.2, 0.5, 0.9], [0.8, 0.6, 0.8, 0.5]],
 [[0.2, 0.2, 0.9, 0.7], [0.3, 0.6, 0.3, 0.8], [0.7, 0.1, 0.2, 0.9], [0.6, 0.6, 0.6, 0.8]]]
```

Each sublist represents [Mu, T, I, F] for an alternative under a criterion.

### Initializing NFSet and RNF
- `NFSet(nf_arr)`: Creates the neutrosophic fuzzy set from the data matrix.
- `RNF(nfs, cost)`: Reduces the NF-set, incorporating costs (empty list for no costs).

### Evaluating Decisions
The loop evaluates the 9 similarity measures and selects the best alternative using  

`DecisionMaker(rnf, i).best_alternative()`.  

Example Output:  
```
Similarity no. 1 : 2
Similarity no. 2 : 2
Similarity no. 3 : 2
Similarity no. 4 : 2
Similarity no. 5 : 2
Similarity no. 6 : 2
Similarity no. 7 : 2
Similarity no. 8 : 2
Similarity no. 9 : 2
```

This ranks alternatives per measure, helping identify the optimal choice under uncertainty.

For real-world applications, replace random data with actual NF-matrix from your domain (e.g., student GPAs for subject selection as in the paper).