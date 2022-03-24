def get_neighbours(matrix, row, col):
    '''
    This function takes a n*n matrix and the row and column values and evaluates the neighbours that the element at the particular row and column has. 

    :param matrix: n*n matrix
    :param row: the row at which the target element is located
    :param col: the column at which the target element is located

    :returns: a list of tuples where all the tuples are coordinates of all the neighbours of the target element. The neighbours are elements immediately to the left, to the right, above and below the target element

    :time complexity: O(1) 
    :space complexity: O(1)
    '''
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


def local_maximum(M):
    n = len(M)
    
    corner_1 = (0,0)
    corner_2 = (0, n-1)
    corner_3 = (n-1, 0)
    corner_4 = (n-1, n-1)

    for i in range(n):
        coord_1 = get_local_max(M, corner_1)
        coord_2 = get_local_max(M, corner_2)
        coord_3 = get_local_max(M, corner_3)
        coord_4 = get_local_max(M, corner_4)

        if coord_1 == corner_1:
            return [coord_1[0], coord_1[1]]
        else:
            corner_1 = coord_1

        if coord_2 == corner_2:
            return [coord_2[0], coord_2[1]]
        else:
            corner_2 = coord_2
        
        if coord_3 == corner_3:
            return [coord_3[0], coord_3[1]]
        else:
            corner_3 = coord_3

        if coord_4 == corner_4:
            return [coord_4[0], coord_4[1]]
        else:
            corner_4 = coord_4



