import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        while idx < len(data) and data[idx].strip() == b'':
            idx += 1
        if idx >= len(data):
            break
        N = int(data[idx])
        idx += 1
        word_to_bool = {}
        for _ in range(N):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            line = data[idx].split()
            idx += 1
            w = line[0].decode()
            s = int(line[1])
            if (w, s) in word_to_bool:
                word_to_bool[(w, s)] += 1
            else:
                word_to_bool[(w, s)] = 1
        
        total = 0
        for key in word_to_bool:
            total += word_to_bool[key]
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()