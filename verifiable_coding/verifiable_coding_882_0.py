import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        A = data[index]
        B = data[index + 1]
        index += 2
        
        from collections import Counter
        count_A = Counter(A)
        count_B = Counter(B)
        
        common = 0
        for char in count_A:
            if char in count_B:
                common += min(count_A[char], count_B[char])
        print(common)

if __name__ == '__main__':
    solve()