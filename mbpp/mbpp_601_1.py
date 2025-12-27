def check(candidate):
    assert candidate([Pair(5, 24), Pair(15, 25),Pair(27, 40), Pair(50, 60)], 4) == 3
    assert candidate([Pair(1, 2), Pair(3, 4),Pair(5, 6), Pair(7, 8)], 4) == 4
    assert candidate([Pair(19, 10), Pair(11, 12),Pair(13, 14), Pair(15, 16), Pair(31, 54)], 5) == 5


def longest_chain(pairs):
    pairs.sort(key=lambda x: x[1])
    chain = []
    for pair in pairs:
        if not chain or chain[-1][1] <= pair[0]:
            chain.append(pair)
    return chain

check(longest_chain)