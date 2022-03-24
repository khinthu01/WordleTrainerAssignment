
def get_neighbours(matrix, row, col):

    neighbours = []
    n = len(matrix)

    if row == 0:
        neighbours.append((row+1, col))
        if col == 0:
            neighbours.append((row, col+1))
        elif col == n-1:
            neighbours.append((row, col-1))
        else:
            neighbours.append((row, col+1))
            neighbours.append((row, col-1))
    elif row == n-1:
        neighbours.append((row-1, col))
        if col == 0:
            neighbours.append((row, col+1))
        elif col == n-1:
            neighbours.append((row, col-1))
        else:
            neighbours.append((row, col+1))
            neighbours.append((row, col-1))
    elif col == 0:
        neighbours.append((row+1, col))
        neighbours.append((row, col+1))
        neighbours.append((row-1, col))
    elif col == n-1:
        neighbours.append((row+1, col))
        neighbours.append((row, col-1))
        neighbours.append((row-1, col))
    else:
        neighbours.append((row+1, col))
        neighbours.append((row, col+1))
        neighbours.append((row, col-1))
        neighbours.append((row-1, col))

    return neighbours

def get_local_max(matrix, coords):
    neighbours = get_neighbours(matrix, coords[0], coords[1])
    
    num_neighbours = len(neighbours)
    max_val = matrix[coords[0]][coords[1]]
    max_coords = coords

    for i in range(num_neighbours):
        cur_val = matrix[neighbours[i][0]][neighbours[i][1]]
        if cur_val > max_val:
            max_val = cur_val
            max_coords = neighbours[i]

    return max_coords


def local_maximum(matrix):
    n = len(matrix)
    
    corner_1 = (0,0)
    corner_2 = (0, n-1)
    corner_3 = (n-1, 0)
    corner_4 = (n-1, n-1)

    for i in range(n):
        coord_1 = get_local_max(matrix, corner_1)
        coord_2 = get_local_max(matrix, corner_2)
        coord_3 = get_local_max(matrix, corner_3)
        coord_4 = get_local_max(matrix, corner_4)

        if coord_1 == corner_1:
            return corner_1
        else:
            corner_1 = coord_1

        if coord_2 == corner_2:
            return corner_2
        else:
            corner_2 = coord_2
        
        if coord_3 == corner_3:
            return corner_3
        else:
            corner_3 = coord_3

        if coord_4 == corner_4:
            return corner_4
        else:
            corner_4 = coord_4


M = [[1, 2, 27, 28, 29, 30, 22],
[3, 4, 25, 26, 31, 32, 35],
[5, 6, 23, 24, 33, 34, 47],
[7, 8, 21, 49, 46, 36, 48],
[9, 10, 19, 20, 37, 38, 45],
[11, 12, 17, 18, 39, 40, 44],
[13, 14, 15, 16, 41, 42, 43]]

print(local_maximum(M))