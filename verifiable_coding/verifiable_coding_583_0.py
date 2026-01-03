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
        # Let's compute the possible sum after operations
        
        # For each element A_i, we can subtract any multiple of i (0 or more)
        # So the possible values for A_i after operations are A_i - k*i for k >= 0
        # The sum of all elements after operations is sum(A_i - k*i) = sum(A_i) - sum(k*i)
        # We need this sum to be 0, so sum(A_i) - sum(k*i) = 0 => sum(k*i) = sum(A_i)
        # So the question is: can we find non-negative integers k_1, k_2, ..., k_N such that sum(k_i * i) = sum(A_i)
        
        # Since N is small (<= 10), we can try all possible combinations of k_i
        # The maximum possible sum of k_i * i is when each k_i is as large as needed
        # But since A_i can be up to 100 in absolute value, and i is up to 10, the maximum sum is 100*10 = 1000
        # So we can try all possible combinations of k_i such that sum(k_i * i) = sum(A_i)
        
        total = sum(A)
        # Try all possible combinations of k_i such that sum(k_i * i) = total
        # We can use backtracking or BFS to find if such a combination exists
        
        # Since N is small, we can use a recursive backtracking approach
        # We'll try all possible k_i for each position i, and check if the sum equals total
        
        def can_reach(target, index, current_sum, k_list):
            if index == N:
                return current_sum == target
            for k in range(0, 1000):  # Arbitrary large number to cover possible values
                new_sum = current_sum + k * (index + 1)
                if new_sum > target:
                    break
                k_list.append(k)
                if can_reach(target, index + 1, new_sum, k_list):
                    return True
                k_list.pop()
            return False
        
        if can_reach(total, 0, 0, []):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()