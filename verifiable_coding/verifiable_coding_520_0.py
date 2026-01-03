import sys

def solve():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    cases = data[1:T+1]
    ship_classes = {
        'B': 'BattleShip',
        'b': 'BattleShip',
        'C': 'Cruiser',
        'c': 'Cruiser',
        'D': 'Destroyer',
        'd': 'Destroyer',
        'F': 'Frigate',
        'f': 'Frigate'
    }
    for case in cases:
        print(ship_classes.get(case, 'Unknown'))

if __name__ == '__main__':
    solve()