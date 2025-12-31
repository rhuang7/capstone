import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    friends = list(map(int, data[1:n+1]))
    game = list(map(int, data[n+1:]))
    
    from collections import defaultdict
    count = defaultdict(int)
    
    for num in friends:
        count[num] += 1
    
    for num in game:
        if count[num] == 0:
            print(num)
            return
        else:
            count[num] -= 1
    
    print(game[-1])

if __name__ == '__main__':
    solve()