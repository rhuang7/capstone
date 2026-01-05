import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        count = 0
        freq = {}
        for num in a:
            current = num
            while current % 2 == 0:
                current //= 2
                if current in freq:
                    freq[current] += 1
                else:
                    freq[current] = 1
        
        for key in freq:
            if key % 2 == 0:
                count += freq[key]
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()