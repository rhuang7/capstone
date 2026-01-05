import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        r = int(data[index])
        g = int(data[index+1])
        b = int(data[index+2])
        index += 3
        
        # The maximum number of days is determined by the sum of the two smaller piles
        # because Tanya can only eat two different colors each day.
        # The minimum of (sum of two smaller piles, total sum // 2) is the answer.
        total = r + g + b
        min_val = min(total // 2, sum(sorted([r, g, b])) - max(r, g, b))
        results.append(str(min_val))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()