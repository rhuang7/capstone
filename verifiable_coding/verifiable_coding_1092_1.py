import sys
import bisect

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
        
        sergey_scores = list(map(int, data[idx:idx+E-1]))
        idx += E-1
        
        # Compute total scores for all students except Sergey
        totals = []
        for s in students:
            total = sum(s)
            totals.append(total)
        
        # Compute the total of other students
        other_totals = totals
        
        # Compute the total of Sergey without last exam
        sergey_total = sum(sergey_scores)
        
        # We need to find the minimum score x such that Sergey's total (sergey_total + x) is among the top K totals
        # We need to find the minimum x where at least (N-K) students have total <= sergey_total + x
        
        # Sort other totals
        other_totals.sort()
        
        # Find the (N-K)th smallest total
        cutoff = other_totals[N-K-1]
        
        # The minimum x is max(0, cutoff - sergey_total + 1)
        required = cutoff - sergey_total + 1
        if required <= 0:
            results.append("Impossible")
        else:
            if required > M:
                results.append("Impossible")
            else:
                results.append(str(required))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()