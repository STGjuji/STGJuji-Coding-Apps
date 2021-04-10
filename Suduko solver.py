def solver(bo):

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
    for i in range(0, len(bo)):
    	if bo[pos[0]][i] == num and ois[1] != i:
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




    return True



    def find_empty(bo):



    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None




def print_board(bo):



    for i in range(len(bo)):
    	if i % 3 == 0 and i != 0:
    		print("- - - - - - - - - - - - - -")

    	for j in range(len(bo[0])):
    		if j % 3 == 0:
    			print(" | ",end="")


    		if j == 8:
    			print(bo[i][j], end="\n")
    		else:
    			print(str(bo[i][j]) + " ", end="")




