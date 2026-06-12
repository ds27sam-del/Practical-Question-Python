# Adding 2 or 3 matrix eith user input



def print_matrix(matrix, name):
    """Matrix ko readable format mein print karta hai"""
    print(f"\n{name} looks like:")
    for row in matrix:
        print(row)

def add_matrices(matrices):
    """Sari matrices ko aapas mein plus (add) karta hai"""
    rows = len(matrices[0])
    cols = len(matrices[0][0])
    
    # Ek empty result matrix initialize kar rahe hain zero se
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for matrix in matrices:
        for i in range(rows):
            for j in range(cols):
                result[i][j] += matrix[i][j]
                
    return result

def main():
    print("=== Matrix Addition Program ===")
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))

    if r <= 0 or c <= 0:
        print("Rows and columns must be greater than 0!")
        return

    num_matrices = int(input("How many matrices do you want to add (2 or 3)? "))
    
    if num_matrices not in [2, 3]:
        print("Invalid choice! Please enter either 2 or 3.")
        return

    # Sari matrices ko store karne ke liye list
    all_matrices = []

    # 1. User se input lena aur save karna
    for i in range(1, num_matrices + 1):
        mat = create_matrix(r, c, i)
        all_matrices.append(mat)

    # 2. User ko unki banayi hui matrices dikhana
    print("\n===============================")
    for i, mat in enumerate(all_matrices, 1):
        print_matrix(mat, f"Matrix {i}")
    print("===============================")

    # 3. Operation perform karna (Plus/Addition)
    print("\nPerforming Addition...")
    result_matrix = add_matrices(all_matrices)
    
    # 4. Final output dikhana
    print_matrix(result_matrix, "The RESULTANT Matrix (After Addition)")

if __name__ == "__main__":
    main()