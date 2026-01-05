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
        
        count = 0
        freq = {}
        
        for char in A:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in B:
            if char in freq and freq[char] > 0:
                count += 1
                freq[char] -= 1
        
        print(count)

if __name__ == '__main__':
    solve()