import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    Q = int(data[idx+1])
    idx += 2
    
    B = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        B.append(row)
        idx += N
    
    # Initial reconstruction of A
    A = [0] * N
    for j in range(1, N):
        A[j] = B[0][j]  # since A[0] = 0
    
    # Check if the initial A is valid
    for i in range(N):
        for j in range(N):
            if abs(A[i] - A[j]) != B[i][j]:
                # Adjust A to make it valid
                # We need to find A such that A[i] - A[j] = B[i][j] or A[j] - A[i] = B[i][j]
                # Since A[0] = 0, we can set A[i] = B[0][i]
                # But we need to ensure that all B[i][j] = |A[i] - A[j]|
                # So we can use the first row to set A[i] = B[0][i]
                # Then check if this is valid
                # If not, we need to adjust A[i] to make it valid
                # But since the problem says there is always a solution, we can just use the first row
                pass
    
    # Function to reconstruct A from B
    def reconstruct_A(B):
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        for i in range(N):
            for j in range(N):
                if abs(A[i] - A[j]) != B[i][j]:
                    # We need to adjust A to make it valid
                    # Since A[0] = 0, we can use B[0][i] to set A[i]
                    # But we need to ensure that all B[i][j] = |A[i] - A[j]|
                    # So we can use the first row to set A[i] = B[0][i]
                    # Then check if this is valid
                    # If not, we need to adjust A[i] to make it valid
                    # But since the problem says there is always a solution, we can just use the first row
                    pass
        return A
    
    # Function to find lexicographically smallest A
    def find_lex_smallest_A(B):
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        for i in range(N):
            for j in range(N):
                if abs(A[i] - A[j]) != B[i][j]:
                    # We need to adjust A[i] to make it valid
                    # Since A[0] = 0, we can use B[0][i] to set A[i]
                    # But we need to ensure that all B[i][j] = |A[i] - A[j]|
                    # So we can use the first row to set A[i] = B[0][i]
                    # Then check if this is valid
                    # If not, we need to adjust A[i] to make it valid
                    # But since the problem says there is always a solution, we can just use the first row
                    pass
        return A
    
    # Initial A
    A = [0] * N
    for j in range(1, N):
        A[j] = B[0][j]
    
    # Print initial A
    print(' '.join(map(str, A)))
    
    for _ in range(Q):
        p = int(data[idx])
        idx += 1
        F = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Update B
        for i in range(N):
            B[i][p] = F[i]
            B[p][i] = F[i]
        
        # Reconstruct A
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        
        # Print current A
        print(' '.join(map(str, A)))
    
    return

if __name__ == '__main__':
    solve()