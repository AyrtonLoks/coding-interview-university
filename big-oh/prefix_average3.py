def prefix_average3(S):  # Linear
    n = len(S)
    A = [0] * n  # create new list of n zeros
    total = 0  # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]  # update prefix sum to include S[j]
        A[j] = total / (j+1)  # compute average based on current sum
    return A


print(prefix_average3([2, 3, 5, 3, 2, 6, 7, 2, 7, 8]))
