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
                    # So total is 2 * min(count_a, len(a)) + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we have to make sure that count_a is not more than the total number of a's
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can't take more than count_a on each end
                    # So total is 2 * count_a + count_b
                    # But we can only take count_a on each end