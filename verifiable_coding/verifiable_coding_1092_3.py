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
        N, K, E, M = map(int, data[idx:idx+4])
        idx += 4
        students = []
        for _ in range(N-1):
            scores = list(map(int, data[idx:idx+E]))
            idx += E
            students.append(scores)
        sergey = list(map(int, data[idx:idx+E-1]))
        idx += E-1
        
        # Calculate total scores for all students (excluding Sergey)
        totals = []
        for s in students:
            total = sum(s)
            totals.append(total)
        
        # Sergey's current total (without last exam)
        sergey_total = sum(sergey)
        
        # We need to find the minimum score x such that Sergey's total (sergey_total + x) is among the top K
        # Sort the totals in descending order
        totals.sort(reverse=True)
        
        # The cutoff score for being in top K is the (N-K)th score (0-based)
        cutoff = totals[N-K-1] if N-K > 0 else 0
        
        # Find the minimum x such that sergey_total + x >= cutoff
        # But also, x can't exceed M
        min_x = max(0, cutoff - sergey_total)
        if min_x > M:
            results.append("Impossible")
        else:
            results.append(str(min_x))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()