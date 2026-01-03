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
        
        # Generate all possible strings by moving one character
        # to any position (including before or after)
        min_str = S
        for i in range(N):
            char = S[i]
            # Remove the character
            new_str = S[:i] + S[i+1:]
            # Try inserting it at every possible position
            for j in range(len(new_str) + 1):
                candidate = new_str[:j] + char + new_str[j:]
                if candidate < min_str:
                    min_str = candidate
        print(min_str)

if __name__ == '__main__':
    solve()