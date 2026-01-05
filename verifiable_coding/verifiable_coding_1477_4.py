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
        # Try each possible character to remove and insert in the best possible position
        res = S
        for i in range(N):
            char = S[i]
            # Try inserting this character at every possible position
            for j in range(N):
                if j == i:
                    continue
                new_s = S[:i] + S[i+1:] + S[j] + S[j+1:]
                if new_s < res:
                    res = new_s
        print(res)

if __name__ == '__main__':
    solve()