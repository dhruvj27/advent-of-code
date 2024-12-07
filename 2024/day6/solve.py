
def is_loop(map,position,direction):
    length_line = map.index('\n') + 1
    length = len(map)
    rotate = {'up':'right', 'right':'down', 'down':'left','left':'up'}
    
    def next(position, direction):       # Find next position of guard
        return [position-length_line, position+1, position+length_line, position-1][['up','right','down','left'].index(direction)]
    def out_of_map(pos):                 # Calculate if position is out of map
        return pos < 0 or pos > length or map[pos]=='\n' 
   
    hit = set()
    while True:
        next_pos = next(position, direction)
        if out_of_map(next_pos):
            return False
        if map[next_pos] == '#':
            if (next_pos, direction) in hit:       # Check if cuurent obstacle has been hit before
                return True
            hit.add((next_pos,direction))
            direction=rotate[direction]
        else:
            position=next_pos

def guard_path(map,position,direction):
    length_line = map.index('\n') + 1
    length = len(map)
    rotate = {'up':'right', 'right':'down', 'down':'left','left':'up'}

    def next(position, direction):       # Find next position of guard
        return [position-length_line, position+1, position+length_line, position-1][['up','right','down','left'].index(direction)]
    def out_of_map(pos):                 # Calculate if position is out of map
        return pos < 0 or pos > length or map[pos]=='\n' 
    
    while True:
        map[position]='X'            # Mark current position as visited
        next_pos = next(position, direction)
        if out_of_map(next_pos):     # Check if guard willbe out of map
            return map
        if map[next_pos] == '#':     # check if there's an obstacle ahead
            direction=rotate[direction]
        else:
            position=next_pos

def main():
    print("\n--- Day 6: Guard Gallivant ---")
    with open("input.txt","r") as f:
        text=f.read()
        print("Input read")

    map = list(text)
    length = len(map)
    length_line = map.index('\n') + 1

    start_position = map.index('^')
    start_direction  = 'up'
    
    final_map = guard_path(map, start_position, start_direction)
    distinct_positions = final_map.count("X")

    print(f"\n--- Part One ---\nNo of occurences of 'XMAS': {distinct_positions}")

    possible_new_obstacles = 0
    for position, mark in enumerate(final_map):
        if position != start_position and mark=='X':
            map[position]='#'
            possible_new_obstacles+=is_loop(map,start_position,'up')
            map[position]='X'
    
    print(f"\n--- Part Two --- \nNo of occurences of X-'MAS': {possible_new_obstacles}\n")
    

if __name__ == '__main__':
    main()