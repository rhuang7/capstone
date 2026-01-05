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
        K = int(data[idx+1])
        E = int(data[idx+2])
        M = int(data[idx+3])
        idx +=4
        
        students = []
        for _ in range(N-1):
            scores = list(map(int, data[idx:idx+E]))
            idx += E
            students.append(scores)
        
        sergey_scores = list(map(int, data[idx:idx+E-1]))
        idx += E-1
        
        # Compute total scores of all students without last exam
        total_scores = []
        for student in students:
            total = sum(student)
            total_scores.append(total)
        
        # Compute the threshold for being enrolled
        # We need to find the minimum score Sergey can get such that at least (N-K) students have total score <= his total
        # So we need to find the (N-K)th smallest total score among all students
        
        # Sort the total scores
        total_scores.sort()
        
        # The threshold is the (N-K)th smallest total score
        threshold = total_scores[N-K-1]
        
        # Sergey's current total without last exam
        sergey_total = sum(sergey_scores)
        
        # Find the minimum score Sergey needs in the last exam
        # His total after last exam = sergey_total + last_exam_score
        # We need sergey_total + last_exam_score > threshold
        # So last_exam_score > threshold - sergey_total
        # Since last_exam_score can be at most M, we check if it's possible
        required = threshold - sergey_total + 1
        if required > M:
            results.append("Impossible")
        else:
            results.append(str(required))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()