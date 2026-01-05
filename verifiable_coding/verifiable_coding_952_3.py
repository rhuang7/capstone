import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    vowels = {'a': 1, 'e': 5, 'i': 9, 'o': 15, 'u': 21}
    
    total_cost = 0
    for s in data:
        for c in s:
            if c in vowels:
                continue
            # Find the closest vowel to the current character
            pos = ord(c) - ord('a') + 1
            min_diff = float('inf')
            for vowel in vowels:
                diff = abs(vowels[vowel] - pos)
                if diff < min_diff:
                    min_diff = diff
            total_cost += min_diff
    print(total_cost)

if __name__ == '__main__':
    solve()