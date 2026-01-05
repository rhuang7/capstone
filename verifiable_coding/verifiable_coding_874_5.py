import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, M, S = map(int, data[idx:idx+3])
        idx += 3
        H = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Filter topics that can be studied in one day
        single_day = [h for h in H if h <= S]
        # Filter topics that can be studied in two days
        two_day = [h for h in H if h > S and h <= 2 * S]
        
        # Count how many single-day and two-day topics we can take
        count_single = len(single_day)
        count_two = len(two_day)
        
        # Try to maximize the number of topics
        max_topics = 0
        
        # Try all possible combinations of single and two-day topics
        # Since S is small (<=16), and H_i is small (<=50), we can try all possibilities
        for i in range(0, count_single + 1):
            for j in range(0, count_two + 1):
                # Total days needed: i + 2*j
                if i + 2 * j <= M:
                    max_topics = max(max_topics, i + j)
        
        results.append(str(max_topics))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()