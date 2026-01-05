import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    S_list = data[1:T+1]
    
    total = 0
    for S in S_list:
        n = len(S)
        total += n * (n - 1) // 2  # Total number of pairs (i, i+1) in all possible substrings
        
        # Count the number of adjacent pairs that are equal in the original string
        equal_pairs = 0
        for i in range(n - 1):
            if S[i] == S[i + 1]:
                equal_pairs += 1
        
        # For each flip, the number of adjacent pairs that change is at most 2
        # So total contribution is equal_pairs * 2
        total += equal_pairs * 2
    
    print(total)

if __name__ == '__main__':
    solve()