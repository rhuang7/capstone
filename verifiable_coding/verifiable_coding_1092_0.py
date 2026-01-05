import sys
import math

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
        
        # Compute total scores of other students
        other_totals = []
        for student in students:
            total = sum(student)
            other_totals.append(total)
        
        # Compute the total of Sergey's first E-1 exams
        sergey_total = sum(sergey_scores)
        
        # Find the (N-K)th highest total score among other students
        other_totals.sort(reverse=True)
        cutoff = other_totals[K-1]
        
        # Find the minimum score Sergey needs in the last exam
        # To have his total >= cutoff
        min_score = max(0, cutoff - sergey_total)
        
        # Check if it's possible
        if min_score > M:
            results.append("Impossible")
        else:
            results.append(str(min_score))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()