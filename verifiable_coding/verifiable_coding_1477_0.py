import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        S = data[index]
        index += 1
        
        # Find the lexicographically smallest string by performing at most one operation
        # Try each character as the one to move
        result = S
        for i in range(N):
            # Remove the character at position i
            char = S[i]
            # Try inserting it at every possible position
            for j in range(N):
                if j == i:
                    continue
                new_str = S[:i] + S[i+1:] + S[j] + S[j+1:]
                if new_str < result:
                    result = new_str
        print(result)
        
if __name__ == '__main__':
    solve()