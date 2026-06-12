# Program to multiply the 2 matrix

def mult_matrix(mat1,mat2):
    result = [[0 for _ in range(2)] for _ in range (2)]

    for i in range (2):
        for j in range(2):
            for k in range(3):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result

def main():
    mat1=[[1,2,3],
          [4,5,6]]
    mat2=[[7,8],
          [9,10],
          [11,12]]
    
    result_mat=mult_matrix(mat1,mat2)

    if isinstance(result_mat,str):
        print(result_mat)
    else:
        print("Result of matrix multiplication " )
        for row in result_mat:
            print(row)

if __name__=="__main__":
    main()