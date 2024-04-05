import numpy as np

# Transition matrix
mat = np.array([
    [1/3, 1/2, 0],
    [1/3, 0, 1/2],
    [1/3, 1/2, 1/2]
])

# Initial probability vector
int_mat = np.full((len(mat), 1), 1/len(mat))

# Damping factor
damping_factor = 0.8

# Probability vector with teleportation
teleportation_prob = np.full_like(int_mat, 1/len(mat))

# Perform iterative computation
i = 0
while True:
    new_mat = damping_factor * np.dot(mat, int_mat) + (1 - damping_factor) * teleportation_prob
    if np.allclose(new_mat, int_mat, rtol=1e-4):
        print("Converged!!")
        print(new_mat)
        break
    print(f"Iteration {i}: \n {new_mat}\n")
    int_mat = new_mat
    i += 1