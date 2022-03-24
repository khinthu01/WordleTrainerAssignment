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
    '''
    This function takes a n*n matrix and coordinates of an element in the matrix and accesses all its neighbours against the element to determine which out of these values is the largest and then returns the coordinates of the largest value

    :param matrix: n*n matrix of distinct integers
    :param coords: a tuple containing the coordinates of the element being accessed in the matrix

    :returns: a tuple which represents the coordinates of the largest value amount the element at coords and its neighbours

    :time complexity: O(1) since the maximum number of loops is 4 if the element at coords has 4 neighbours and hence this function has a constant time complexity
    :space complexity: O(1) 
    '''

    # determine the neighbours of the element at coords
    neighbours = get_neighbours(matrix, coords[0], coords[1])
    
    num_neighbours = len(neighbours)
    max_val = matrix[coords[0]][coords[1]]
    max_coords = coords

    # loop through all the neighbours and compare it to max_val which initially is equal to the element at coords
    # if one of the neighbours is larger than max_val then the value of max_val is replaced with that of the neighbour and the max_coords are also replaced with the coordinates of the neighbour
    for i in range(num_neighbours):
        cur_val = matrix[neighbours[i][0]][neighbours[i][1]]
        if cur_val > max_val:
            max_val = cur_val
            max_coords = neighbours[i]

    return max_coords


def local_maximum(M):
    '''
    This function takes a n*n matrix and returns a single pair of coordinates that contains the local maximum in the matrix. An element is considered to be a local maximum if it is larger than all its neighbours (left, above, right, and below the element).

    This function works by starting at the four corners of the matrix and then identify all the neighbours of each of the four points and then identifying the maximum value out of the groups of neighbours by calling get_local_max. If a neighbour is the largest then the point moves to its neighbours. This happens concurrently with all four points. The loop ends when the result of get_local_max is equal to the same coordinates that were inputted since that indicates that the element at those coordinates was larger than all its neighbours, hence making it a local maximum. 

    :param M: n*n matrix of distinct integers

    :returns: a list of length 2 which holds the coordinates of a local maximum. The output is in the format of [x,y] so that M[x][y] is a local maximum

    :time complexity: O(n) where n is the length of a row in the matrix, M
    :space complexity: O(1)
    '''
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

        # if coord_n == corner_n then that means those coords contain a local maximum and thus should be returned
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



