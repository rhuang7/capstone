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
        
        # Calculate total scores for all students except Sergey
        totals = []
        for s in students:
            total = sum(s)
            totals.append(total)
        
        # Add Sergey's current total (without last exam)
        sergey_total = sum(sergey_scores)
        
        # We need to find the minimum score x such that Sergey's total + x is among the top K
        # We will try all possible x from 0 to M and check if it's possible
        
        # Sort the totals
        totals.sort()
        
        # Find the threshold for being in the top K
        # The (N-K)th smallest total is the cutoff
        cutoff = totals[N-K-1]
        
        # We need to find the minimum x such that sergey_total + x > cutoff
        # If there are multiple students with total > cutoff, we need to ensure that Sergey's total is among the top K
        
        # Try all possible x from 0 to M
        min_x = M + 1
        for x in range(M + 1):
            total = sergey_total + x
            # Count how many students have total > cutoff
            count = 0
            for t in totals:
                if t > cutoff:
                    count += 1
            if count + 1 >= K:
                min_x = x
                break
        
        if min_x <= M:
            results.append(str(min_x))
        else:
            results.append("Impossible")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()