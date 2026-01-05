import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    m = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(m):
        n = int(data[idx])
        T = int(data[idx+1])
        a = int(data[idx+2])
        b = int(data[idx+3])
        idx += 4
        
        types = list(map(int, data[idx:idx+n]))
        idx += n
        t = list(map(int, data[idx:idx+n]))
        idx += n
        
        easy = []
        hard = []
        for i in range(n):
            if types[i] == 0:
                easy.append(t[i])
            else:
                hard.append(t[i])
        
        easy.sort()
        hard.sort()
        
        max_points = 0
        
        for s in range(0, T + 1):
            # Check if all mandatory problems by s are solved
            # Check easy problems
            e = 0
            time = 0
            for ti in easy:
                if ti > s:
                    break
                if time + a <= s:
                    e += 1
                    time += a
                else:
                    break
            # Check hard problems
            h = 0
            time = 0
            for ti in hard:
                if ti > s:
                    break
                if time + b <= s:
                    h += 1
                    time += b
                else:
                    break
            if e + h == len(easy) + len(hard):
                max_points = max(max_points, e + h)
        
        results.append(max_points)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()