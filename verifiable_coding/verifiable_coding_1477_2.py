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
        # Try all possible positions to remove and insert
        result = S
        for i in range(N):
            for j in range(N):
                if i != j:
                    new_s = S[:i] + S[j:i] + S[i] + S[j+1:]
                    if new_s < result:
                        result = new_s
        print(result)

if __name__ == '__main__':
    solve()