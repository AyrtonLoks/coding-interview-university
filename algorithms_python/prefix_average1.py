def prefix_average1(S):  # Quadratic
    n = len(S)
    A = [0] * n  # create new list of n zeros
    for j in range(n):
        total = 0  # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1)  # record the average
    return A


print(prefix_average1([2, 3, 5, 3, 2, 6, 7, 2, 7, 8]))
