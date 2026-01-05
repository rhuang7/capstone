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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We can perform any number of operations, each subtracting i from A_i
        # The sum of the sequence after operations must be 0
        # Let's compute the sum of A_i - i * k_i for some k_i >= 0
        # The sum is sum(A_i) - sum(i * k_i) = 0
        # So sum(A_i) must be >= 0 and the remainder after subtracting sum(i * k_i) must be 0
        # But since k_i can be any non-negative integer, we can choose k_i such that sum(i * k_i) = sum(A_i)
        # So the question becomes: can we find non-negative integers k_i such that sum(i * k_i) = sum(A_i)
        # This is equivalent to checking if sum(A_i) is non-negative and can be expressed as a sum of multiples of i's
        
        # Since N is small (<= 10), we can use a recursive approach or backtracking to check if it's possible
        
        # We'll use a recursive backtracking approach to check if it's possible to reach the target sum using the i's
        target = sum(A)
        if target < 0:
            results.append("NO")
            continue
        
        # We'll try all possible numbers of operations for each index
        # For each index i, we can choose how many times to subtract i from A_i
        # The maximum number of times we can subtract i is floor((A_i + i * k) / i)
        # But since we are trying to reach the target, we can try all possible numbers of operations for each index
        
        # We'll use a recursive function to check if it's possible to reach the target sum
        def can_reach(target, index):
            if target == 0:
                return True
            if index >= N:
                return False
            # Try all possible numbers of operations for this index
            # The maximum number of operations is floor((target) / i)
            i = index + 1
            max_ops = target // i
            for ops in range(0, max_ops + 1):
                if can_reach(target - ops * i, index + 1):
                    return True
            return False
        
        if can_reach(target, 0):
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()