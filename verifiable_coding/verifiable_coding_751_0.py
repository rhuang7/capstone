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
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        x = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Find indices of villages with electricity
        has_electricity = [i for i in range(n) if s[i] == '1']
        
        # If all villages have electricity, no wire needed
        if len(has_electricity) == n:
            results.append(0)
            continue
        
        # Find the first village without electricity
        first_no_electricity = 0
        while first_no_electricity < n and s[first_no_electricity] == '1':
            first_no_electricity += 1
        
        # Find the first village with electricity after the first no electricity
        next_with_electricity = first_no_electricity
        while next_with_electricity < n and s[next_with_electricity] == '0':
            next_with_electricity += 1
        
        # Calculate the distance between the first no electricity and the next with electricity
        min_wire_length = x[next_with_electricity] - x[first_no_electricity]
        results.append(min_wire_length)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()