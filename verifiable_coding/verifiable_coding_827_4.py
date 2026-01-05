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
        idx += 2
        S = data[idx]
        idx += 1
        
        # Preprocess the string to count 'a's and 'b's in each segment
        a_count = 0
        b_count = 0
        total_ab = 0
        
        # Count the number of 'a's and 'b's in the original string
        a_total = S.count('a')
        b_total = S.count('b')
        
        # For each occurrence of 'a' in the original string, count how many 'b's are after it
        # and multiply by K (since the string is repeated K times)
        # Also, account for the fact that 'a's in the same position in different repetitions can pair with 'b's in other repetitions
        # So, for each 'a' in the original string, it can pair with all 'b's in the original string multiplied by K
        # And also, each 'a' can pair with all 'b's in the original string multiplied by (K - 1) for the other repetitions
        # But this is not correct, need to think differently
        
        # Correct approach:
        # For each 'a' in the original string, it can pair with all 'b's in the original string multiplied by K (each repetition)
        # But also, each 'a' in the original string can pair with all 'b's in the original string multiplied by (K - 1) for the other repetitions
        # So total is a_total * b_total * K * (K + 1) // 2
        
        # Wait, no. Let's think again.
        # The total number of 'ab' pairs is the number of 'a's multiplied by the number of 'b's in the entire string.
        # But the entire string is S repeated K times.
        # So the total number of 'a's is a_total * K
        # The total number of 'b's is b_total * K
        # But the 'a's and 'b's are not necessarily in order, so we need to count the number of 'a's before each 'b' in the entire string.
        
        # So, we need to count for each 'b' in the entire string, how many 'a's are before it in the entire string.
        # This can be done by counting the number of 'a's in the original string and multiplying by K (for each repetition)
        # And for each 'b' in the original string, we can count how many 'a's are before it in the original string, and multiply by K (for each repetition)
        
        # So, for each 'b' in the original string, count the number of 'a's before it in the original string, then multiply by K (for each repetition)
        # Also, for each 'a' in the original string, count the number of 'b's after it in the original string, then multiply by K (for each repetition)
        
        # So, we need to precompute for each position in the original string:
        # - the number of 'a's before it
        # - the number of 'b's after it
        
        a_prefix = [0] * (N + 1)
        b_suffix = [0] * (N + 1)
        
        a_count = 0
        for i in range(N):
            a_prefix[i+1] = a_count
            if S[i] == 'a':
                a_count += 1
        
        b_count = 0
        for i in range(N-1, -1, -1):
            b_suffix[i] = b_count
            if S[i] == 'b':
                b_count += 1
        
        total = 0
        for i in range(N):
            if S[i] == 'a':
                total += b_suffix[i] * K
            elif S[i] == 'b':
                total += a_prefix[i] * K
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()