import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N, K = int(data[index]), int(data[index+1])
        index += 2
        s = data[index]
        index += 1
        
        # Calculate the number of uppercase and lowercase letters
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