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
        lis = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Construct the number
        num = []
        prev = 0
        for i in range(n):
            if i == 0:
                num.append(str(9 - lis[i]))
            else:
                if lis[i] > lis[i - 1]:
                    num.append(str(9 - lis[i]))
                else:
                    num.append(str(9 - lis[i] + 1))
        
        results.append(''.join(num))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()