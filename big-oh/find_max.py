def find_max(data):
    biggest = data[0]  # The initial value to beat
    for val in data:  # For each value:
        if val > biggest:  # if it is greater than the best so far,
            biggest = val  # we have found a new best (so far)
    return biggest


print(find_max([1, 3, 24, 5, 3, 65, 33, 45, 6]))
