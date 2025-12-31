import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    cases = input[1:t+1]
    
    for n in cases:
        original = ""
        for ch in n:
            original += str(int(ch) - 2)
        print(original)
        
if __name__ == '__main__':
    solve()