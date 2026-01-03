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
        n = int(data[index])
        index += 1
        l = list(map(int, data[index:index + n]))
        index += n
        
        count = {}
        for length in l:
            count[length] = count.get(length, 0) + 1
        
        frames = 0
        for length in count:
            if count[length] >= 2:
                frames += count[length] // 2
        results.append(frames)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()