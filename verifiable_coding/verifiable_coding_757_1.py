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
            # Check if there are at least two vowels adjacent
            has_vowel = False
            for j in range(N):
                if rotated[j] in vowels:
                    has_vowel = True
                    if j < N - 1 and rotated[j+1] in vowels:
                        found = True
                        break
                elif has_vowel and j < N - 1 and rotated[j+1] in vowels:
                    found = True
                    break
            if found:
                break
        
        print("Yes" if found else "No")

if __name__ == '__main__':
    solve()