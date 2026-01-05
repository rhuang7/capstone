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
        
        total_students = []
        for student in students:
            total = sum(student)
            total_students.append(total)
        
        # Compute the threshold
        threshold = sum(total_students) - (N - K) * M
        # Compute Sergey's current total
        sergey_total = sum(sergey)
        
        # Find the minimum score Sergey needs in the last exam
        min_score = 0
        for i in range(N-1):
            # Compute the total of the i-th student
            total_i = total_students[i]
            # Compute the total of Sergey if he gets 'score' in the last exam
            # We want to find the minimum 'score' such that Sergey's total is >= threshold
            # and at least (N-K) students have total <= Sergey's total
            # So we need to find the minimal 'score' such that:
            # sergey_total + score >= threshold
            # and at least (N-K) students have total <= sergey_total + score
            # We can binary search on 'score' from 0 to M
            low = 0
            high = M
            best = M + 1
            while low <= high:
                mid = (low + high) // 2
                current_total = sergey_total + mid
                count = 0
                for total in total_students:
                    if total <= current_total:
                        count += 1
                if count >= N - K:
                    best = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if best <= M:
                min_score = min(min_score, best)
        
        if min_score <= M:
            results.append(str(min_score))
        else:
            results.append("Impossible")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()