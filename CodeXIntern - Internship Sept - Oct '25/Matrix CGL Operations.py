# matrix_tool.py
import numpy as np

def read_matrix(prompt="Enter matrix"):
    while True:
        try:
            rows = int(input(f"{prompt} - rows: "))
            cols = int(input(f"{prompt} - cols: "))
            print(f"Enter {rows} rows, each row's {cols} numbers separated by spaces.")
            mat = []
            for r in range(rows):
                row_in = input(f"Row {r+1}: ").strip().split()
                if len(row_in) != cols:
                    raise ValueError(f"Expected {cols} numbers, got {len(row_in)}")
                mat.append([float(x) for x in row_in])
            return np.array(mat)
        except ValueError as e:
            print("Input error:", e, "— please try again.")

def main_menu():
    print("\nMatrix Operations Tool")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Transpose")
    print("5) Determinant")
    print("6) Exit")

def run_tool():
    np.set_printoptions(precision=4, suppress=True)
    while True:
        main_menu()
        choice = input("Choose (1-6): ").strip()
        if choice == '1':
            print("Matrix A:")
            A = read_matrix("Matrix A")
            print("Matrix B:")
            B = read_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: matrices must have same shape to add.")
            else:
                print("A + B =\n", A + B)
        elif choice == '2':
            print("Matrix A:")
            A = read_matrix("Matrix A")
            print("Matrix B:")
            B = read_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: matrices must have same shape to subtract.")
            else:
                print("A - B =\n", A - B)
        elif choice == '3':
            print("Matrix A:")
            A = read_matrix("Matrix A")
            print("Matrix B:")
            B = read_matrix("Matrix B")
            if A.shape[1] != B.shape[0]:
                print(f"Error: multiplication requires A.columns == B.rows (got {A.shape[1]} != {B.shape[0]}).")
            else:
                print("A x B =\n", A.dot(B))
        elif choice == '4':
            print("Matrix A:")
            A = read_matrix("Matrix A")
            print("Transpose(A) =\n", A.T)
        elif choice == '5':
            print("Matrix A (must be square):")
            A = read_matrix("Matrix A")
            if A.shape[0] != A.shape[1]:
                print("Error: determinant defined only for square matrices.")
            else:
                det = np.linalg.det(A)
                print(f"determinant = {det:.6f}")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == '__main__':
    run_tool()
