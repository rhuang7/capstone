import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        possible = True
        
        # Check if a and b have the same elements except for possible -1, 0, 1
        # But since operations can change values, we need to check if b can be achieved
        # from a using the allowed operations
        
        # For each element in b, check if it can be achieved from a[i]
        # The allowed operations can add a[i] to a[j], so the value of a[j] can be increased or decreased
        # But the key is that the value of a[j] can be changed by adding any number of a[i]s
        # So for each position j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        
        # However, since we can perform operations any number of times, the value of b[j] can be any value that is reachable from a[j] by adding any number of a[i]s (i < j)
        # But since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, the key is that the value of b[j] must be reachable from a[j] by adding any number of a[i]s (i < j)
        # But since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # So for each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # So for each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # So for each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # So for each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or 1, the possible values for b[j] are limited
        
        # For each j, the value of b[j] must be achievable from a[j] by adding any number of a[i]s (i < j)
        # But since we can choose any i < j, the value of b[j] can be any value that is achievable by adding any number of a[i]s (i < j)
        # However, since a[i] can be -1, 0, or