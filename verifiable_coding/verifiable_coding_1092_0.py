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
        
        # Compute total scores of other students
        totals = []
        for student in students:
            total = sum(student)
            totals.append(total)
        
        # Compute the current total of other students
        # We need to find the minimum score Sergey needs in the last exam
        # such that his total is strictly greater than at least (N-K) students' totals
        
        # Sort the totals
        totals.sort()
        
        # We need to find the minimum score x such that:
        # (sum of sergey's first E-1 scores + x) > totals[N-K-1]
        # because there are N-K students that can have lower or equal totals
        # and Sergey needs to be among the top K
        
        # The minimum x is such that:
        # sergey_total + x > totals[N-K-1]
        # x > totals[N-K-1] - sergey_total
        
        sergey_total = sum(sergey_scores)
        if N-K == 0:
            # All students are enrolled, Sergey needs to be among them
            # So he needs to have the highest total
            # But since he is not part of the students, we need to find the max total
            # and see if he can have a higher one
            max_total = max(totals)
            required = max_total + 1
            if required > M:
                results.append("Impossible")
            else:
                results.append(str(required))
            continue
        
        target = totals[N-K-1]
        required = target - sergey_total + 1
        if required > M:
            results.append("Impossible")
        else:
            results.append(str(required))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()