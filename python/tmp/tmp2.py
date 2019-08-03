raw, col = [int(i) for i in input().split()]

matrix = []

for r in range(raw):
    matrix_raw = [int(i) for i in input().split()]
    matrix.append(matrix_raw)

def get_max_index(l):
    max_val = 0
    max_i = 0
    for i in l:
        if isinstance(l[i], list):
            tmp_val, tmp_i = get_max_index(l[i])
            if tmp_val > max_val:
                max_val = tmp_val
                max_i = (max_i, tmp_i)
        else
            if l[i] > max_val:
                max_val = l[i]
                max_i = i
    return (max_val, max_i)

print(get_max_index(matrix))
