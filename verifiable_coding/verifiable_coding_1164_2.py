import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    P = int(data[idx])
    idx += 1
    S = int(data[idx])
    idx += 1
    
    problems = []
    
    for i in range(P):
        sc = list(map(int, data[idx:idx+S]))
        idx += S
        ns = list(map(int, data[idx:idx+S]))
        idx += S
        
        # Sort subtasks by score
        sorted_subtasks = sorted(zip(sc, ns), key=lambda x: x[0])
        
        # Calculate n
        n = 0
        for k in range(S-1):
            if sorted_subtasks[k][1] > sorted_subtasks[k+1][1]:
                n += 1
        
        problems.append((n, i+1))  # (n, problem index)
    
    # Sort problems by difficulty
    problems.sort()
    
    # Output the problem indices in order
    for p in problems:
        print(p[1])

if __name__ == '__main__':
    solve()