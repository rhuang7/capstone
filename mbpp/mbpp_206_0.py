def check(candidate):
    assert candidate(("DSP ", "IS ", "BEST ", "FOR ", "ALL ", "UTS")) == ('DSP IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL UTS')
    assert candidate(("RES ", "IS ", "BEST ", "FOR ", "ALL ", "QESR")) == ('RES IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL QESR')
    assert candidate(("MSAM", "IS ", "BEST ", "FOR ", "ALL ", "SKD")) == ('MSAMIS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL SKD')


def adjacent_element_concatenation(tuples_list):
    result = []
    for i in range(len(tuples_list) - 1):
        tuple1 = tuples_list[i]
        tuple2 = tuples_list[i + 1]
        concatenated = ""
        for j in range(min(len(tuple1), len(tuple2))):
            concatenated += str(tuple1[j]) + str(tuple2[j])
        result.append(concatenated)
    return result

check(adjacent_element_concatenation)