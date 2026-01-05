import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
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
        print(ship_classes[case])

if __name__ == '__main__':
    solve()