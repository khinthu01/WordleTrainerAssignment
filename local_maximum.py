def local_maximum(matrix):
    n = len(matrix)
    i = n//2
    j = i

    while (i >= 0 and i < n) and (j >= 0 and j < n):
        max_val = matrix[i][j]
        max_idx = [i, j]
        
        neighbors = [(i-1, j), (i+1, j), (i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j+1), (i, j+1), (i+1, j+1)]

        for coord in neighbors:
            if coord[0] < 0 or coord[0] >= n or coord[1] < 0 or coord[1] >= n:
                neighbors.pop(neighbors.index(coord))

        for coord in neighbors:
            value = matrix[coord[0]][coord[1]]
            if value > max_val:
                max_val = value
                max_idx = [coord[0], coord[1]]

        if max_idx == [i, j]:
            return max_idx
