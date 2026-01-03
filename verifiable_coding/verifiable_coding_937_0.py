import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        s = data[i]
        valid = True
        cook = 0
        eat = 0
        sleep = 0
        
        for c in s:
            if c == 'C':
                if cook > 0:
                    valid = False
                    break
                cook += 1
            elif c == 'E':
                if cook == 0 or eat > 0:
                    valid = False
                    break
                eat += 1
            elif c == 'S':
                if cook == 0 or eat == 0 or sleep > 0:
                    valid = False
                    break
                sleep += 1
        
        results.append("yes" if valid else "no")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()