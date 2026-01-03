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
    
    # Prioritize running
    running = total_calories // 50
    remaining = total_calories % 50
    
    # Prioritize cycling
    cycling = remaining // 5
    remaining %= 5
    
    # Remaining is for walking
    walking = remaining / 0.5
    
    print(running)
    print(cycling)
    print(walking)

if __name__ == '__main__':
    solve()