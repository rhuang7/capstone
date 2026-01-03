import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    wealth = list(map(int, data[1:]))
    
    ranks = []
    for i in range(N):
        current = wealth[i]
        count = 0
        for j in range(i+1):
            if wealth[j] > current:
                count += 1
        ranks.append(str(count + 1))
    
    print('\n'.join(ranks))

if __name__ == '__main__':
    solve()