import functools
def sort_using_count(c1, c2):
    if c1 == c2 :
        return 0
    elif c1 > c2:
        return 1
    else:
        return -1



count_sort = [1, 3, 1, 4, 1, 2, 3, 2 , 4, 6 , 7, 8,]
sorted_arr = sorted(count_sort, key=functools.cmp_to_key(sort_using_count))
print(sorted_arr)
