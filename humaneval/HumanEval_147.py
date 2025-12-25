def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361



def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    mod_counts = [0, 0, 0]
    for num in a:
        mod_counts[num % 3] += 1
    
    count = 0
    # Count triples where all three elements are congruent to 0 mod 3
    count += mod_counts[0] * (mod_counts[0] - 1) * (mod_counts[0] - 2) // 6
    # Count triples where all three elements are congruent to 1 mod 3
    count += mod_counts[1] * (mod_counts[1] - 1) * (mod_counts[1] - 2) // 6
    # Count triples where all three elements are congruent to 2 mod 3
    count += mod_counts[2] * (mod_counts[2] - 1) * (mod_counts[2] - 2) // 6
    # Count triples where elements are congruent to 0, 1, 2 mod 3
    count += mod_counts[0] * mod_counts[1] * mod_counts[2]
    
    return count

check(get_max_triples)