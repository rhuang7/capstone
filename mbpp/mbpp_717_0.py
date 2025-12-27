def check(candidate):
    assert candidate([4, 2, 5, 8, 6])== 2.23606797749979
    assert candidate([1,2,3,4,5,6,7])==2.160246899469287
    assert candidate([5,9,10,15,6,4])==4.070217029430577


def standard_deviation(data):
    if not data:
        return 0.0
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)
    return variance ** 0.5

check(standard_deviation)