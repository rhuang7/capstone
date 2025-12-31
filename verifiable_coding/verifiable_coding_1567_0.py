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
        
        for char, freq in count.items():
            if freq % 2 != 0:
                odd_count += 1
        
        if odd_count > 2:
            print("NO")
            continue
        
        # Check if the string can be rearranged to form a doublindrome
        # For a doublindrome, each half must be a palindrome
        # So, each character must appear an even number of times (or at most two characters with odd counts)
        # But for the halves to be palindromes, each character must appear even number of times in the entire string
        # So, the total count of each character must be even
        # So, we check if all characters have even counts
        
        valid = True
        for char, freq in count.items():
            if freq % 2 != 0:
                valid = False
                break
        
        if valid:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()