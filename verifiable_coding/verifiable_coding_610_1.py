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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        people = [i for i, val in enumerate(A) if val == 1]
        
        valid = True
        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                if people[j] - people[i] < 6:
                    valid = False
                    break
            if not valid:
                break
        
        results.append("YES" if valid else "NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()