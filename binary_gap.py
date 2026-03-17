def solution(N):
    """
    Binary Gaps in numbers
    O(log N)
    """
    max_gap = 0
    current_gap = -1  # -1 means we haven't started counting

    while N > 0:
        if N & 1:  # found a '1'
            if current_gap != -1:
                max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            if current_gap != -1:
                current_gap += 1

        N >>= 1  # shift right

    return max_gap


print(solution(788849388673))
