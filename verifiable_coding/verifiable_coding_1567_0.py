import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        S = data[index + 1]
        index += 2
        
        from collections import Counter
        
        count = Counter(S)
        odd_count = 0
        
        for ch in count:
            if count[ch] % 2 != 0:
                odd_count += 1
        
        if odd_count > 2:
            print("NO")
        else:
            print("YES")
            
if __name__ == '__main__':
    solve()