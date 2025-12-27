def check(candidate):
    assert candidate(['aaa','bbb','ccc','bbb','aaa','aaa']) == 'bbb'
    assert candidate(['abc','bcd','abc','bcd','bcd','bcd']) == 'abc'
    assert candidate(['cdma','gsm','hspa','gsm','cdma','cdma']) == 'gsm'


def second_most_repeated(strings):
    from collections import Counter
    
    if not strings:
        return None
    
    count = Counter(strings)
    if len(count) < 2:
        return None
    
    sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_counts[1][0] if sorted_counts[1][1] > 0 else None

check(second_most_repeated)