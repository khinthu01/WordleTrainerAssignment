
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
    else:
        neighbours.append((row+1, col))
        neighbours.append((row, col+1))
        neighbours.append((row, col-1))
        neighbours.append((row-1, col))

    return neighbours

def get_local_max(matrix, coords):
    neighbours = get_neighbours(matrix, coords[0], coords[1])
    
    corners = len(neighbours)
    max_val = matrix[coords[0]][coords[1]]
    max_coords = coords

    for i in range(corners):
        cur_val = matrix[corners[i][0]][corners[i][1]]
        if cur_val > max_val:
            max_val = cur_val
            max_coords = corners[i]

    if max_val == matrix[coords[0]][coords[1]]:
        return True

    return max_coords


def local_maximum(matrix):
    n = len(matrix)
    
    corner_1 = (0,0)
    corner_2 = (0, n-1)
    corner_3 = (n-1, 0)
    corner_4 = (n-1, n-1)

    for _ in range(n):
        corner_1 = get_local_max(matrix, corner_1)
        corner_2 = get_local_max(matrix, corner_2)
        corner_3 = get_local_max(matrix, corner_3)
        corner_4 = get_local_max(matrix, corner_4)

        if corner_1:
            return corner_1
        elif corner_2:
            return corner_2
        elif corner_3:
            return corner_3
        elif corner_4:
            return corner_4
