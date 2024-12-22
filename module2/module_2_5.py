def get_matrix(n=2, m=2, value=1):
    # matrix = []
    # for _ in range(n):
    #     matrix.append([])
    #     for _ in range(m):
    #         matrix[-1].append(value)
    # return matrix
    return [[value for _ in range(m)] for _ in range(n)]

print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
