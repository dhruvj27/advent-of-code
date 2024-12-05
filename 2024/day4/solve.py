
def count_part1(text):
    occurences = 0
    length = len(text)
    length_line = text.find('\n') + 1
    
    for pos, char in enumerate(text):
        if char != 'X':
            continue
        #Forward-search
        if (pos%length_line + 3 < length_line) and text[pos:pos+4] == 'XMAS':
            occurences +=1   
        #Backward-search
        if (pos%length_line > 2) and text[pos:pos-4:-1] == 'XMAS':
            occurences +=1
        #Upward-search
        if (pos//length_line > 2) and text[pos-length_line]=='M' and text[pos-length_line*2]=='A' and text[pos-length_line*3]=='S':
            occurences += 1
        #Downward-search
        if (pos + length_line*3 < length) and text[pos+length_line]=='M' and text[pos+length_line*2]=='A' and text[pos+length_line*3]=='S':
            occurences+=1
        #Upward and Backward-search
        if (pos%length_line > 2) and (pos//length_line > 2) and text[pos-length_line-1]=='M' and text[pos-length_line*2-2]=='A' and text[pos-length_line*3-3]=='S':
            occurences+=1
        #Upward and Forward-search
        if (pos%length_line+3 < length_line) and (pos//length_line > 2) and text[pos-length_line+1]=='M' and text[pos-length_line*2+2]=='A' and text[pos-length_line*3+3]=='S':
            occurences+=1
        #Downward and Backward-search
        if (pos%length_line > 2) and (pos + length_line*3 < length) and text[pos+length_line-1]=='M' and text[pos+length_line*2-2]=='A' and text[pos+length_line*3-3]=='S':
            occurences+=1
        #Downward and Forward-search
        if (pos%length_line+3 < length_line) and (pos + length_line*3 < length) and text[pos+length_line+1]=='M' and text[pos+length_line*2+2]=='A' and text[pos+length_line*3+3]=='S':
            occurences+=1
    return occurences

def count_part2(text):
    occurences = 0
    length = len(text)
    length_line = text.find('\n') + 1
    
    for pos,char in enumerate(text):
        if ((pos + length_line*2 + 2 < length) and (text[pos + length_line + 1] == 'A' )  #Check index and center 'A'
            and ((char == 'M' and text[pos+length_line*2 + 2] == 'S') or (char == 'S' and text[pos+length_line*2 + 2] == 'M')) #Check main diagonal
            and ((text[pos + 2] == 'M' and text[pos + length_line*2] == 'S') or (text[pos + 2] == 'S' and text[pos + length_line*2] == 'M'))):  #Check antidiagonal
            
            occurences +=1
    return occurences


def main():
    print("\n--- Day 4: Ceres Search ---")
    with open("input.txt","r") as f:
        text=f.read()
        print("Input read")
    
    print(f"\n--- Part One ---\nNo of occurences of 'XMAS': {count_part1(text)}")

    print(f"\n--- Part Two --- \nNo of occurences of X-'MAS': {count_part2(text)}\n")

        

if __name__ == '__main__':
    main()