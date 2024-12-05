import re

def main():
    print("\n--- Day 3: Mull It Over ---")
    with open("input.txt","r",encoding = "utf-16") as f:
        data=f.read()
        print("Input read")

    # Part 1
    matches = re.findall(r"mul\((\d+)+,(\d+)\)",data)
    result = sum(int(x)*int(y) for x,y in matches)
    print(f"\n--- Part One ---\nSum of all valid multiplications: {result}")

    # Part 2
    enabled_data = re.sub(r'don\'t\(\)((?s:.)*?)do\(\)','do()',data)
    conditional_matches = re.findall(r"mul\((\d+)+,(\d+)\)",enabled_data)
    conditional_result = sum(int(x)*int(y) for x,y in conditional_matches)
    print(f"\n--- Part Two ---\nSum of enabled valid multiplications: {conditional_result}\n")
   
if __name__ == "__main__":
    main()