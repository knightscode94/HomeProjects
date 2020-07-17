print("Welcome input your puzzle using 0 for the blanks")
l1 = input("input First row of numbers: ")
l2 = input("input Second row of numbers: ")
l3 = input("input Third row of numbers: ")
l4 = input("input Fourth row of numbers: ")
l5 = input("input Fifth row of numbers: ")
l6 = input("input Sixth row of numbers: ")
l7 = input("input Seventh row of numbers: ")
l8 = input("input Eighth row of numbers: ")
l9 = input("input Ninth row of numbers: ")
ln1 = l1.split()
ln2 = l2.split(" ")
ln3 = l3.split(" ")
ln4 = l4.split(" ")
ln5 = l5.split(" ")
ln6 = l6.split(" ")
ln7 = l7.split(" ")
ln8 = l8.split(" ")
ln9 = l9.split(" ")
int(ln1)
board = [
    [ln1],
    [ln2],
    [ln3],
    [ln4],
    [ln5],
    [ln6],
    [ln7],
    [ln8],
    [ln9]
]

def solve(bo):
# optional print code
    # print(bo)
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(len(bo)): # row
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])): # col
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j]) # row,col
            else:
                print(str(bo[i][j]) + " ", end="")



def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row,col

    return None

print_board(board)
solve(board)
print("________________________")
print_board(board)
