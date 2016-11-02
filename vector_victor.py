from nose.tools import raises

class ShapeError(Exception):
    pass

def shape(vector):
    columns = len(vector)
    try:
        rows = len(vector[0])
        return (columns, rows)
    except:
        return (columns, )

def vector_add(vector1, vector2):
    if shape(vector1) == shape(vector2):
        new_list = [a + b for a, b in zip(vector1, vector2)]
        return new_list
    else:
        raise ShapeError

def vector_add_is_commutative():
    pass

def vector_sub(vector1, vector2):
    if shape(vector1)==shape(vector2):
        new_list = [a - b for a, b in zip(vector1, vector2)]
        return new_list
    else:
        raise ShapeError

def vector_sum(*args):
    shape_list = [shape(vector) for vector in args]
    if min(shape_list) == max(shape_list):
        new_list = []
        new_list = [sum(x) for x in zip(*args)]
        return new_list
    else:
        raise ShapeError

def dot(vector1, vector2):
    if shape(vector1) == shape(vector2):
        new_list = [a * b for a, b in zip(vector1, vector2)]
        return sum(new_list)
    else:
        raise ShapeError

def vector_multiply(vector1, scalar):
    new_list = [scalar * x for x in vector1]
    return new_list

def vector_mean(*args):
    mean_list =  [x *(1/len(args)) for x in vector_sum(*args)]
    return mean_list

def magnitude(vector1):
    squares_added = [x**2 for x in vector1]
    return (sum(squares_added))**(1/2)

def matrix_row(matrix1, row_num):
    return matrix1[row_num]

def matrix_col(matrix, col_num):
    new_list = [x[col_num] for x in matrix]
    return new_list

# def matrix_add(matrix1, matrix2):
#     new_row = vector_add(matrix1[x], matrix2[x])
#
#     print(new_row)











#ABCDEFG
