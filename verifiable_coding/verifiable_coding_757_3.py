import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        S = data[index]
        index += 1
        
        vowels = {'A', 'E', 'I', 'O', 'U'}
        found = False
        
        # Check all cyclic permutations
        for i in range(N):
            # Create the cyclic permutation by rotating the string
            rotated = S[i:] + S[:i]
            # Check if any two vowels are adjacent
            has_vowel_pair = False
            for j in range(N):
                if rotated[j] in vowels and rotated[(j + 1) % N] in vowels:
                    has_vowel_pair = True
                    break
            if has_vowel_pair:
                found = True
                break
        
        print("Yes" if found else "No")

if __name__ == '__main__':
    solve()