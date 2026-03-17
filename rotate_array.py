def rotate(A, K):
    N = len(A)
    if N == 0:
        return A

    K %= N  # handle K > N

    def reverse(start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1

    reverse(0, N - 1)
    reverse(0, K - 1)
    reverse(K, N - 1)

    return A


arr = [1, 2, 3, 4, 5, 6, 7]

print(rotate(A=arr, K=89000))
