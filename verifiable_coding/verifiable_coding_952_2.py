import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_values = {'a': 1, 'e': 5, 'i': 9, 'o': 15, 'u': 21}
    
    total_cost = 0
    
    for s in data:
        for c in s:
            if c in vowels:
                continue
            # Find the minimum cost to change this consonant to any vowel
            min_cost = float('inf')
            for vowel in vowels:
                cost = abs(vowel_values[vowel] - ord(c) + 1)
                if cost < min_cost:
                    min_cost = cost
            total_cost += min_cost
    
    print(total_cost)

if __name__ == '__main__':
    solve()