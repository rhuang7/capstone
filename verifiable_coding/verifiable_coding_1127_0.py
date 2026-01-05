import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        parts = case.split()
        if len(parts) == 1:
            # Only first name
            formatted = parts[0].decode().capitalize()
        else:
            # Format all parts except last
            formatted_parts = []
            for i in range(len(parts) - 1):
                first_char = parts[i].decode()[0].upper()
                formatted_parts.append(f"{first_char}.")
            # Add last part properly capitalized
            last_part = parts[-1].decode().capitalize()
            formatted = ''.join(formatted_parts) + ' ' + last_part
        print(formatted)

if __name__ == '__main__':
    solve()