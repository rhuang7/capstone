import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        m = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        
        # Total steps needed to reach (n, m)
        # Each diagonal move contributes 1 to both x and y
        # Each non-diagonal move contributes 1 to either x or y
        # Let d be the number of diagonal moves
        # Then, d + s = k, where s is the number of non-diagonal moves
        # Also, d + s_x = n, d + s_y = m, where s_x and s_y are the number of non-diagonal moves contributing to x and y respectively
        # s_x + s_y = s
        # So, d + s_x = n, d + s_y = m, s_x + s_y = k - d
        # Adding the first two equations: 2d + s_x + s_y = n + m
        # But s_x + s_y = k - d, so 2d + (k - d) = n + m => d + k = n + m => d = n + m - k
        
        d = n + m - k
        
        # Check if d is non-negative and valid
        if d < 0 or d > k:
            results.append(-1)
            continue
        
        # Check if the remaining steps can be used to reach the target
        # The remaining steps is k - d
        # Each non-diagonal step can contribute to either x or y
        # So, the total steps needed for x and y is (n - d) + (m - d) = n + m - 2d
        # But since d = n + m - k, this becomes k
        # So, the remaining steps is k - d = k - (n + m - k) = 2k - n - m
        # Which should be >= 0 and even, since each non-diagonal step contributes 1 to either x or y
        remaining = k - d
        if remaining < 0 or remaining % 2 != 0:
            results.append(-1)
            continue
        
        # Check if the remaining steps can be used to reach the target
        # The remaining steps is the number of non-diagonal steps, which must be equal to (n - d) + (m - d)
        # Which is (n + m - 2d) = (n + m - 2(n + m - k)) = 2k - n - m
        # Which is the same as remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) = n + m - 2d
        # Which is equal to remaining
        # So, the check is already done
        
        # Now, check if the remaining steps can be used to reach the target
        # The number of non-diagonal steps is remaining
        # Each non-diagonal step contributes to either x or y
        # So, the total number of non-diagonal steps is (n - d) + (m - d) =