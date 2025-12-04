from utils.util import open_file

def solve():
    contents = open_file('Day 1\input.txt')
    
    current = 50
    zero_count = 0

    for move in contents:
        direction, steps = move[0], int(move[1:])

        if direction == 'L':
            current -= steps
            if current < 0:
                current = (100 * (abs(current) // 100)) + current

        elif direction == 'R':
            current += steps
            if current > 99:
                current = current - (100 * (current // 100))
        
        if current == 0:
            zero_count += 1
    
    print("Password:", zero_count)

solve()