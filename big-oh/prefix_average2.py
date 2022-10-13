def prefix_average2(S):  # Quadratic
    n = len(S)
    A = [0] * n  # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)  # record the average
    return A


print(prefix_average2([2, 3, 5, 3, 2, 6, 7, 2, 7, 8]))
