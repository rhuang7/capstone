def check(candidate):
    assert candidate([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert candidate([(10,20), (15,2), (5,10)] )==200
    assert candidate([(11,44), (10,15), (20,5), (12, 9)] )==484


def max_product_from_pairs(tuples_list):
    if not tuples_list or len(tuples_list) < 2:
        return None  # Not enough tuples to form a pair
    
    max_product = float('-inf')
    
    for i in range(0, len(tuples_list), 2):
        if i + 1 >= len(tuples_list):
            break
        tuple1 = tuples_list[i]
        tuple2 = tuples_list[i + 1]
        
        product = 1
        for a, b in [(tuple1[0], tuple2[0]), (tuple1[1], tuple2[1])]:
            product *= a * b
        
        if product > max_product:
            max_product = product
    
    return max_product if max_product != float('-inf') else None

check(max_product_from_pairs)