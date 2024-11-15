def count_zeros(matix):

    count_z = 0
    
    for string in matix:
        if string[0] > 0:
            break
        for el in string:
            if not el:
                count_z += 1
            else:
                break

    return count_z

if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    print(count_zeros(matrix))