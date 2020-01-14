def array_left_rotation(a, n, k):
    list = []
    i = 0
    while (len(list) < n):
        if (k < n):
            list.append(a[k-n])
            k = k + 1
        else:
            list.append(a[i])
            i = i +1
    return list
