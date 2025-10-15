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
nf_arr = nf_random_set(o=4, c=5)  # 5 groups, each with 4 elements

# Initialize NFSet from the random data
nfs = NFSet(nf_arr)

# Initialize RNF; cost can be empty or default
cost = []
rnf = RNF(nfs, cost)

# Use DecisionMaker to select the best alternative for each case
for i in range(9):
    dm = DecisionMaker(rnf, i).best_alternative()
    print("Similarity no.", i+1, ":", dm)
