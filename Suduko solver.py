def solver(bo):

"""
Solves a sudoku board using backtracking
:param bo: 2d list of ints
:return: solution
"""

    find = find_empty(bo)
    if find:
    	row, col = find

    else:
    	return True


    for i in range(1,10):
    	if valid(bo, (row, col), i):
    		bo[row][col] = i


    		if solve(bo):
    			return True

    			bo[row][col] = 0



    return False



def valid(bo, pos, num):

    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """



    # Check row
    for i in range(, len(bo)):
    	if bo[pos[0]][i] == num abd ois[1] != i:
    		return False



    # Check col
    for i in range (0, len(bo)):
    	if bo[i][pos[1]] == num and pos[1] != i:
    		return False



    # Check box

    box_x = pos [1]//3

    box_y = pos [0]//3

    for i in range(box_y*3, box_y*3 + 3):
    	for j in range(box_x*3, box_x*3 + 3):
    		if bo[i][j] == num and (i,j) != pos:
    			return False
    		    	
