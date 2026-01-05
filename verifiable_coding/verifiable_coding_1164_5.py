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
        sc_sorted = [x[0] for x in sorted_subtasks]
        ns_sorted = [x[1] for x in sorted_subtasks]
        
        # Calculate n
        n = 0
        for k in range(S - 1):
            if ns_sorted[k] > ns_sorted[k + 1]:
                n += 1
        
        problems.append((n, i + 1))  # (n, problem index)
    
    # Sort by difficulty (n, then problem index)
    problems.sort()
    
    for n, idx in problems:
        print(idx)

if __name__ == '__main__':
    solve()