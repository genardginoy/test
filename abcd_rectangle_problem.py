

# ABCD is a rectangle
# Inputs

A = [2, 2]
B = [4, 2]
C = [4, 6]
D = [2, 6]

# Cordinates
cordinates = [[[2, 3], [2, 4]], [[2, 4], [2, 7]], [
    [2, 2], [4, 2]], [[2, 4], [4, 4]], [[5, 2], [5, 5]]]


# Solution

max_x_range = [A[0], B[0]]  # maxmum range of x

max_y_range = [A[1], C[1]]  # maxmum range of y

bottom_x = A[1]
top_x = C[1]
left_y = A[0]
right_y = C[0]


for cord in cordinates:

    # Get if cordinates is less than max x and max y  or false
    if max_x_range[0] <= cord[0][0] <= max_x_range[1] and max_y_range[0] <= cord[0][1] <= max_y_range[1] and \
            max_x_range[0] <= cord[1][0] <= max_x_range[1] and max_y_range[0] <= cord[1][1] <= max_y_range[1]:

        if cord[0][0] == cord[1][0]:
            if cord[0][0] == left_y or cord[0][0] == right_y:
                print("True")
            else:
                print("False")

        elif cord[0][1] == cord[1][1]:
            if cord[0][1] == bottom_x or cord[0][1] == top_x:
                print("True")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")
