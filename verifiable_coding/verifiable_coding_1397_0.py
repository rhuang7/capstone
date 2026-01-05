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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the array
        A.sort()
        
        # Find the longest increasing subsequence (LIS)
        # But since the array is sorted, the LIS is the length of the array
        # However, we need to find the minimum M such that the LIS is maximized
        # When the array is sorted, the LIS is the length of the array
        # But when we repeat the array M times, the LIS can be increased
        # If the array is strictly increasing, then the LIS is N*M
        # If the array is not strictly increasing, then the LIS is the length of the longest increasing subsequence in the original array multiplied by M
        
        # Find the length of the longest increasing subsequence in the original array
        lis = 1
        for i in range(1, N):
            if A[i] > A[i-1]:
                lis += 1
            else:
                break
        
        # If the array is strictly increasing, then the maximum LIS is N*M
        # So we need to find the minimum M such that the LIS is maximized
        # But since the array is sorted, the LIS is the length of the array
        # So the maximum possible LIS is N*M
        # So the minimum M is 1
        
        # If the array is not strictly increasing, then the LIS is the length of the longest increasing subsequence in the original array
        # So we need to find the minimum M such that the LIS is maximized
        # The maximum possible LIS is the length of the longest increasing subsequence in the original array multiplied by M
        # So the minimum M is 1
        
        # But wait, the problem says that the sequence B is A*M, which is appending A M times
        # So the LIS of B is the length of the longest increasing subsequence in the original array multiplied by M
        # So the maximum possible LIS is the length of the longest increasing subsequence in the original array multiplied by M
        # So the minimum M is 1 if the longest increasing subsequence is already maximized
        
        # But if the array is not strictly increasing, then the LIS of B is the length of the longest increasing subsequence in the original array multiplied by M
        # So the minimum M is 1 if the longest increasing subsequence is already maximized
        
        # So the answer is 1 if the array is strictly increasing, else 2
        
        if A[-1] > A[0]:
            results.append(1)
        else:
            results.append(2)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()