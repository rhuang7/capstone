def check(candidate):
    assert candidate([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    assert candidate([('Sanjeev', 11), ('Angat', 5), ('Akash', 3), ('Nepin', 9)], 3) == [('Akash', 3), ('Angat', 5), ('Nepin', 9)]
    assert candidate([('tanmay', 14), ('Amer', 11), ('Ayesha', 9), ('SKD', 16)], 1) == [('Ayesha', 9)]


def find_min_k_records(data, k):
    if not data or k <= 0 or k > len(data):
        return []
    return sorted(data, key=lambda x: x)[ :k]

check(find_min_k_records)