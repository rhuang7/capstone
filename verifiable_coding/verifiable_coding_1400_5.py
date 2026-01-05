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
        L = int(data[idx+1])
        R = int(data[idx+2])
        idx += 3
        
        # Minimum sum: all elements are 1
        min_sum = N * 1
        
        # Maximum sum: use the largest possible numbers that satisfy the conditions
        # The numbers must be powers of 2 (since if x is in the array, x/2 must also be in the array)
        # So the maximum sum is the sum of the first R powers of 2, each appearing once, and the rest are 1s
        # But we need to ensure that the number of unique elements is between L and R
        # So we take the first R powers of 2 (each appearing once), and fill the rest with 1s
        # However, if R is larger than the number of possible unique elements (which is limited by N), we need to adjust
        # The maximum number of unique elements is min(N, 20), since 2^20 is a large number and the constraints say R <= min(N, 20)
        max_unique = min(N, 20)
        max_unique = min(max_unique, R)
        
        # We need at least L unique elements, so we take the first L powers of 2, and fill the rest with 1s
        # But to maximize the sum, we take the first R powers of 2, and fill the rest with 1s
        # So the maximum sum is sum of first R powers of 2, each appearing once, and the rest are 1s
        # But if R is larger than the number of possible unique elements, we take all possible unique elements (up to 20)
        # So the maximum sum is sum of first R powers of 2, each appearing once, and the rest are 1s
        # But if R exceeds the number of possible unique elements, we take all possible unique elements (up to 20)
        max_unique = min(R, 20)
        
        # Calculate the sum of the first max_unique powers of 2
        max_sum = 0
        for i in range(max_unique):
            max_sum += (1 << i)  # 2^i
        
        # The remaining elements are 1s
        max_sum += (N - max_unique) * 1
        
        results.append(f"{min_sum} {max_sum}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()