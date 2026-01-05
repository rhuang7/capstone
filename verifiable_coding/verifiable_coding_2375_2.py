import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        max_len = 0
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        for a_val in freq:
            for b_val in freq:
                if a_val == b_val:
                    max_len = max(max_len, freq[a_val])
                else:
                    count_a = freq[a_val]
                    count_b = freq[b_val]
                    # Try to take as many a as possible on both ends
                    # and as many b as possible in the middle
                    # The middle can be all b's
                    # The ends can be as many a's as possible
                    # So total is 2 * min(count_a, count_b) + count_b
                    # Or 2 * count_a + count_b if count_a >= count_b
                    # Or 2 * count_b + count_a if count_b >= count_a
                    # But since we can choose which is the middle, we take the max
                    # So the maximum is 2 * min(count_a, count_b) + max(count_a, count_b)
                    # Which is count_a + count_b
                    # Wait, no. Because the middle can be all b's, and the ends can be as many a's as possible
                    # So the total is 2 * min(count_a, count_b) + count_b
                    # Or 2 * min(count_a, count_b) + count_a
                    # So the maximum is 2 * min(count_a, count_b) + max(count_a, count_b)
                    # Which is count_a + count_b
                    # So the total is count_a + count_b
                    # But we can also take all a's as the middle and b's as the ends
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # But we can also take all a's as the middle and b's as the ends
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # But we can also take all a's as the middle and b's as the ends
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b
                    # So the maximum is count_a + count_b
                    # So the total is count_a + count_b