def check(candidate):
    assert candidate([1,1,2,3,4,4.3,5,1])==[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
    assert candidate('automatically')==[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
    assert candidate('python')==[[1, 'p'], [1, 'y'], [1, 't'], [1, 'h'], [1, 'o'], [1, 'n']]


def reflect_run_length(encoded):
    result = []
    i = 0
    while i < len(encoded):
        count = encoded[i]
        char = encoded[i + 1]
        result.append(char * count)
        i += 2
    return result

check(reflect_run_length)