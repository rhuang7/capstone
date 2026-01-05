import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        count = 0
        zero_count = 0
        one_count = 0
        
        for c in s:
            if c == '0':
                zero_count += 1
                one_count = 0
            else:
                one_count += 1
                zero_count = 0
        
        count = zero_count * one_count
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()