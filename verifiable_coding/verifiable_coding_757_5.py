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
        
        for i in range(N):
            # Check if any two vowels are adjacent in the cyclic permutation
            # The cyclic permutation is S[i:] + S[:i]
            # Check all consecutive pairs in this permutation
            has_vowel = False
            for j in range(N):
                if S[(i + j) % N] in vowels:
                    has_vowel = True
                else:
                    if has_vowel:
                        found = True
                        break
                    has_vowel = False
            if found:
                break
        
        print("Yes" if found else "No")

if __name__ == '__main__':
    solve()