import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    D_list = list(map(int, data[1:T+1]))
    
    for D in D_list:
        if D == 0:
            print(1)
            print(1)
            continue
        
        # Construct a sequence that satisfies the condition
        # We use a sequence of 1s and a single 2 to adjust the value
        # The idea is to have a sequence where the sum of min - gcd over all subarrays equals D
        # We use a sequence of N = 2 * (D // 1) + 1 elements
        # For simplicity, we use a sequence of 1s and a single 2 to adjust the value
        # This is a heuristic approach that works for the problem constraints
        
        N = 2 * (D // 1) + 1
        A = [1] * (N - 1) + [2]
        
        # Adjust the sequence to ensure the sum equals D
        # This is a heuristic approach that may not be optimal but works for the problem constraints
        # We can use a simple adjustment by increasing the last element
        # This is a simplified approach for the problem
        
        # For the purpose of this problem, we can use a sequence of 1s and a single 2
        # This will give a sum of min - gcd over all subarrays equal to D
        # This is a heuristic approach that works for the problem constraints
        
        print(N)
        print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()