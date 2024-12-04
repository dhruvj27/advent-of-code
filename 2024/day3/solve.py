import re

def main():
    print("\n--- Day 3: Mull It Over ---\n")
    with open("input.txt","r",encoding = "utf-16") as f:
        data=f.read()
    matches = re.findall(r"mul\((\d+)+,(\d+)\)",data)
    result = sum(int(x)*int(y) for x,y in matches)
    print(f"Part One: {result}")

    enabled_data = re.sub(r'don\'t\(\)((?s:.)*?)do\(\)','do()',data)
    
    conditional_matches = re.findall(r"mul\((\d+)+,(\d+)\)",enabled_data)
    conditional_result = sum(int(x)*int(y) for x,y in conditional_matches)
    print(f"Part Two: {conditional_result}\n")
   
if __name__ == "__main__":
    main()