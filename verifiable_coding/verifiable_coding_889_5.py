import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        D = int(data[index])
        index += 1
        S = data[index]
        index += 1
        
        present = 0
        proxy = 0
        for i in range(D):
            if S[i] == 'P':
                present += 1
            elif S[i] == 'A':
                # Check if can mark as present by proxy
                if i > 1 and i < D - 1:
                    if (S[i-1] == 'P' or S[i-2] == 'P') and (S[i+1] == 'P' or S[i+2] == 'P'):
                        proxy += 1
                        present += 1
        required = (D * 3) // 4
        if present >= required:
            print(0)
        else:
            needed = required - present
            if needed <= proxy:
                print(needed)
            else:
                print(-1)

if __name__ == '__main__':
    solve()