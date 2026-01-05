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
        
        # For a string to be a doublindrome, each character must appear even number of times
        # Because each half must be a palindrome, and each half has exactly half the characters
        # of the original string
        valid = True
        for char, freq in count.items():
            if freq % 2 != 0:
                valid = False
                break
        
        print("YES" if valid else "NO")

if __name__ == '__main__':
    solve()