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
    
    # Prioritize running first
    while total_calories > 0:
        if total_calories >= 50:
            running += 1
            total_calories -= 50
        elif total_calories >= 5:
            cycling += 1
            total_calories -= 5
        elif total_calories >= 0.5:
            walking += 1
            total_calories -= 0.5
        else:
            break
    
    print(running)
    print(cycling)
    print(walking)

if __name__ == '__main__':
    solve()