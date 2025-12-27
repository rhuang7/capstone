def check(candidate):
    assert candidate([[2, 1], 2, 3, [2, 4], 5,1])==[1,1,2,3,4,4,5,1]
    assert candidate(['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y'])==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', 'l', 'l', 'y']
    assert candidate(['p', 'y', 't', 'h', 'o', 'n'])==['p', 'y', 't', 'h', 'o', 'n']


def decode_run_length(encoded_list):
    decoded = []
    i = 0
    while i < len(encoded_list):
        count = encoded_list[i]
        char = encoded_list[i + 1]
        decoded.append(char * count)
        i += 2
    return decoded

check(decode_run_length)