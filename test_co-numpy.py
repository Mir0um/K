import numpy as np

def create_matrix(size_x, size_y):
    matrix = np.zeros((size_y, size_x), dtype=str)
    matrix.fill("-")
    return matrix

def update_matrix(matrix, pos_x, pos_y):
    print("Position", pos_x, pos_y)
    matrix_af = np.copy(matrix)
    matrix_af[pos_y][pos_x] = "#"
    print(matrix_af)

    row_labels = "@," + ",".join(str(i) for i in range(len(matrix_af[0])))
    print(row_labels)

    for i, row in enumerate(matrix_af):
        row_str = str(i) + ","
        row_str += ",".join(str(el) for el in row)
        print(row_str)

def main():
    size_x, size_y = int(input("Size X >")), int(input("Size Y >"))

    print(size_x, size_y)

    matrix = create_matrix(size_x, size_y)

    while True:
        pos_x, pos_y = int(input("Position X >")), int(input("Position Y >"))
        update_matrix(matrix, pos_x, pos_y)

if __name__ == "__main__":
    main()
