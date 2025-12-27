def check(candidate):
    assert candidate([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert candidate([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert candidate([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'


def find_min_index_record(tuples):
    if not tuples:
        return None
    min_val = min(tuples, key=lambda x: x[1])
    return min_val

check(find_min_index_record)