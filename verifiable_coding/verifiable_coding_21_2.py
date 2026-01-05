import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = list(map(int, data[index:index + n]))
        index += n
        
        original_set = set(s)
        min_k = -1
        
        for k in range(1, 1024):
            new_set = set()
            for num in s:
                new_set.add(num ^ k)
            if new_set == original_set:
                min_k = k
                break
        
        print(min_k)

if __name__ == '__main__':
    solve()