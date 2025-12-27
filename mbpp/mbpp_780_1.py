def check(candidate):
    assert candidate([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
    assert candidate([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
    assert candidate([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]


def find_combinations_sum(target, tuples):
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(tuple(path))
            return
        for i in range(start, len(tuples)):
            if tuples[i] <= remaining:
                path.append(tuples[i])
                backtrack(i, path, remaining - tuples[i])
                path.pop()
    
    result = []
    backtrack(0, [], target)
    return result

check(find_combinations_sum)