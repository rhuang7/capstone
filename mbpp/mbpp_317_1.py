def check(candidate):
    assert candidate([1,1,2,3,4,4,5,1])==[[2, 1], 2, 3, [2, 4], 5, 1]
    assert candidate('automatically')==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y']
    assert candidate('python')==['p', 'y', 't', 'h', 'o', 'n']


def reflect_run_length(encoded_list):
    result = []
    i = 0
    while i < len(encoded_list):
        count = encoded_list[i]
        char = encoded_list[i + 1]
        result.append(char * count)
        i += 2
    return result

check(reflect_run_length)