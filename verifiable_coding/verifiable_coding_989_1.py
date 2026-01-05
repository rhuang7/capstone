import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index+1])
        K = int(data[index+2])
        index += 3
        
        total_games = X + Y
        serve_changes = total_games // K
        
        if serve_changes % 2 == 0:
            print("Chef")
        else:
            print("Paja")

if __name__ == '__main__':
    solve()