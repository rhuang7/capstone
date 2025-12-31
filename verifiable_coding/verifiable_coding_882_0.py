import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        A = data[index]
        index += 1
        B = data[index]
        index += 1
        
        from collections import Counter
        countA = Counter(A)
        countB = Counter(B)
        
        common = 0
        for char in countA:
            if char in countB:
                common += min(countA[char], countB[char])
        print(common)

if __name__ == '__main__':
    solve()