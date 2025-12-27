def check(candidate):
    assert candidate([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert candidate([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert candidate([99, 15, 13, 47]) == [13, 15, 47, 99]


def comb_sort(arr):
    def is_swap_needed(a, b):
        return a > b

    def swap(a, b):
        arr[a], arr[b] = arr[b], arr[a]

    n = len(arr)
    gap = n
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap * 1.3)
        gap = min(gap, n - 1)

        swapped = False
        for i in range(0, n - gap, gap):
            if is_swap_needed(arr[i], arr[i + gap]):
                swap(i, i + gap)
                swapped = True

    return arr

check(comb_sort)