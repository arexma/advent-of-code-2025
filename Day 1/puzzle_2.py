from utils.util import open_file
from math import ceil

def solve():
    contents = open_file('Day 1/input.txt')
    
    current = 50
    zero_count = 0

    for move in contents:
        direction, steps = move[0], int(move[1:])

        if direction == 'L':
            for i in range(steps):
                current -= 1
                if current == 0:
                    zero_count += 1
                if current < 0:
                    current = 99

        elif direction == 'R':
            for i in range(steps):
                current += 1
                if current > 99:
                    current = 0
                if current == 0:
                    zero_count += 1

    print("Password:", zero_count)

solve()