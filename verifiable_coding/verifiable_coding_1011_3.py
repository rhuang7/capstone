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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # Count uppercase and lowercase letters
        upper = sum(1 for c in s if c.isupper())
        lower = N - upper
        
        # Check if Chef could have sent the message
        chef_possible = (lower <= K) and (upper - K >= 0)
        
        # Check if brother could have sent the message
        brother_possible = (upper <= K) and (lower - K >= 0)
        
        if chef_possible and brother_possible:
            results.append("both")
        elif chef_possible:
            results.append("chef")
        elif brother_possible:
            results.append("brother")
        else:
            results.append("none")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()