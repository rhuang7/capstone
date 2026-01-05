import sys

def solve():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        c = data[i]
        if c == 'B':
            results.append("BattleShip")
        elif c == 'b':
            results.append("BattleShip")
        elif c == 'C':
            results.append("Cruiser")
        elif c == 'c':
            results.append("Cruiser")
        elif c == 'D':
            results.append("Destroyer")
        elif c == 'd':
            results.append("Destroyer")
        elif c == 'F':
            results.append("Frigate")
        elif c == 'f':
            results.append("Frigate")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()