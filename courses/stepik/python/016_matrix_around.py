# matrix01 = ['100']
# matrix02 = ['0', '1', '3']
# matrix03 = [['9', '5', '3'], ['0', '7', '-1'], ['-5', '2', '9']]
#
# print(len(matrix01))
# print(len(matrix02))
# print(len(matrix03))

def input_matrix():
    matrix = []
    while True:
        matrix_string = input()
        if matrix_string == 'end':
            break
        matrix_list_sreing = list(matrix_string.split())
        matrix.append(matrix_list_sreing)
    print(matrix)
    if len(matrix_list_sreing) == 1:
        return matrix_list_sreing
    return matrix


def output_matrix(matrix):
    for i in matrix:
        for j in i:
            print(str(j) + ' ', end='')
        print()
    # print(matrix)


def zero_matrix(number):
    matrix_zero = []
    matrix_zero = [[0 for j in range(number)] for i in range(number)]
    return matrix_zero


def matrix_operation(matrix, matrix2):
    end = len(matrix) - 1
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == end and j == end:
                matrix2[i][j] = int(matrix[i - 1][j]) + int(matrix[0][j]) + int(matrix[i][j - 1]) + int(matrix[i][0])
            elif j == end:
                matrix2[i][j] = int(matrix[i - 1][j]) + int(matrix[i + 1][j]) + int(matrix[i][j - 1]) + int(
                    matrix[i][0])
            elif i == end:
                matrix2[i][j] = int(matrix[i - 1][j]) + int(matrix[0][j]) + int(matrix[i][j - 1]) + int(
                    matrix[i][j + 1])
            else:
                matrix2[i][j] = int(matrix[i - 1][j]) + int(matrix[i + 1][j]) + int(matrix[i][j - 1]) + int(
                    matrix[i][j + 1])
    return matrix2


matrix = input_matrix()
#matrix = matrix03
if len(matrix) == 1:
    print(int(matrix[0])*4)
elif type(matrix[0]) != type(matrix):
    simple_matrix = [0 for i in matrix]
    for i in range(0, len(matrix)):
        if i == 0:
            simple_matrix[0] = int(matrix[1]) + int(matrix[-1]) + int(matrix[i]) * 2
            #print(f'{i=}')
        elif i == len(matrix)-1:
            simple_matrix[i] = int(matrix[i - 1]) + int(matrix[0]) + int(matrix[i]) * 2
            #print(f'{i=} {simple_matrix[i]} = + {matrix[0]}= ')
        else:
            #print(f'{i=}')
            simple_matrix[i] = int(matrix[i - 1]) + int(matrix[i + 1]) + int(i) * 2
    for i in simple_matrix:
        print(str(i) + ' ',  end = '')

else:
    matrix2 = zero_matrix(len(matrix))
    result = matrix_operation(matrix, matrix2)
    display = output_matrix(result)

# print(output_matrix(matrix))
# print(output_matrix(matrix2))
