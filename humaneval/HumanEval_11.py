

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if the lengths of the input strings are equal
    if len(a) != len(b):
        return ""
    
    # Perform XOR on each pair of bits
    result = []
    for bit_a, bit_b in zip(a, b):
        if bit_a == '1' and bit_b == '1':
            result.append('0')
        elif bit_a == '1' or bit_b == '1':
            result.append('1')
        else:
            result.append('0')
    
    return ''.join(result)

check(string_xor)