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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # The first person can start on day 1
        days = 1
        current = 1  # number of people who know the contest
        # We need to reach N people
        while current < N:
            # The number of people who can tell others is current
            # Each of them can tell up to A[i] people
            # But we only need to tell (N - current) people
            total = 0
            for i in range(current):
                total += A[i]
                if total >= (N - current):
                    break
            days += 1
            current += (N - current)
        
        results.append(days)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()