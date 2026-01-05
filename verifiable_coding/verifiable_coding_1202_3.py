import sys

def solve():
    data = sys.stdin.buffer.read().decode().strip()
    calorie_counts = {
        'D': 238,
        'T': 244,
        'M': 138,
        'B': 279,
        'C': 186
    }
    total_calories = sum(calorie_counts[c] for c in data)
    
    running = 0
    cycling = 0
    walking = 0
    
    # Try to use running first
    running_kms = total_calories // 50
    remaining = total_calories % 50
    running = running_kms
    
    # Try to use cycling next
    cycling_kms = remaining // 5
    remaining = remaining % 5
    cycling = cycling_kms
    
    # Use walking for the rest
    walking = remaining / 0.5
    
    print(int(running))
    print(int(cycling))
    print(int(walking))

if __name__ == '__main__':
    solve()