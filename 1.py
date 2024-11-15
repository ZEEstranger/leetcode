# a = [1, 2, 5, 13, 16]
# b = [2, 4, 6, 8, 10, 20]


def conc_2_array(list_1: list, list_2: list):
    
    list_conc = []
    ind_1 = 0
    ind_2 = 0
    
    while ind_1 != len(list_1) and ind_2 != len(list_2):
        if list_1[ind_1] < list_2[ind_2]:
            list_conc.append(list_1[ind_1])
            ind_1 += 1
        else:
            list_conc.append(list_2[ind_2])
            ind_2 += 1
    
    if ind_1 < len(list_1):
        for i in range(ind_1, len(list_1)):
            list_conc.append(list_1[i])

    if ind_2 < len(list_2):
        for i in range(ind_2, len(list_2)):
            list_conc.append(list_2[i])

    return list_conc

if __name__ == '__main__':

    a = [1, 2, 5, 13, 16]
    b = [2, 4, 6, 8, 10, 20]

    res = conc_2_array(a, b)
    print(res)