import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    ids = input[1:T+1]
    
    result = []
    for id in ids:
        if id == 'B':
            result.append("BattleShip")
        elif id == 'b':
            result.append("BattleShip")
        elif id == 'C':
            result.append("Cruiser")
        elif id == 'c':
            result.append("Cruiser")
        elif id == 'D':
            result.append("Destroyer")
        elif id == 'd':
            result.append("Destroyer")
        elif id == 'F':
            result.append("Frigate")
        elif id == 'f':
            result.append("Frigate")
        else:
            result.append("Unknown")
    
    for line in result:
        print(line)

if __name__ == '__main__':
    solve()