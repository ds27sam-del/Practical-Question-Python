# Program to Transpose a matrix.

def mat_tr(mat):
    r,c=len(mat),len(mat[0])
    result=[[0 for _ in range(r)] for _ in range(c)]

    for i in range(r):
        for j in range(c):
            result[j][i]=mat[i][j]
    return result

def main():
    mat=[
        [1,2,3],
        [4,5,6]
    ]

    transposed = mat_tr(mat)

    for row in transposed:
        print(row)

if __name__=="__main__":
    main()