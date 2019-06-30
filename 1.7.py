# Zero out rows and columns that have at least one 0. Assuming the matrix is
# represented as a nested list.

def zero_out(mat):
    zero_out_i = set()
    zero_out_j = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                zero_out_i.add(i)
                zero_out_j.add(j)
    for i in zero_out_i:
        mat[i] = [0]*len(mat[i])
    for j in zero_out_j:
        for i in range(len(mat)):
            mat[i][j] = 0
    return mat

if __name__ == '__main__':
    test1 = [[1,4,6],[2,0,7],[3,5,8]]
    print(zero_out(test1))

    test2 = []
    print(zero_out(test2))

    test3 = [[3,6,2],[1,2,3],[0,1,6],[5,5,4],[1,4,5],[1,0,6]]
    print(zero_out(test3))