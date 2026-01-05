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
        
        # Calculate total scores for all students except Sergey
        total_scores = []
        for s in students:
            total = sum(s)
            total_scores.append(total)
        
        # Calculate the total of other students
        other_total = sum(total_scores)
        
        # Calculate the total of Sergey without last exam
        sergey_total = sum(sergey)
        
        # We need to find the minimum score x such that Sergey's total with x is enough to be in top K
        # The threshold is the (N-K)th highest total score
        # We need to find the minimum x such that sergey_total + x >= threshold
        
        # Sort the other totals in descending order
        other_total.sort(reverse=True)
        
        # Find the threshold
        threshold = other_total[K-1]
        
        # Find the minimum x such that sergey_total + x >= threshold
        required = max(0, threshold - sergey_total)
        
        # Check if it's possible
        if required > M:
            results.append("Impossible")
        else:
            results.append(str(required))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()