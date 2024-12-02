
def is_safe(report):
    sorted_report = sorted(report)
    return ((report == sorted_report or report == sorted_report[::-1]) 
            and all([abs(report[i]-report[i-1]) in range(1,4) for i in range(1,len(report))]))
       

def main():
    print("\n--- Day 2: Red-Nosed Reports ---")
    with open("input.txt","r") as f:
        data=f.readlines()
        print("Input read")

    reports = [list(map(int, report.split())) for report in data]
    
    count_safe = sum([is_safe(report) for report in reports])
    print(F"\n--- Part One ---\nSafe reports: {count_safe}")

    for report in reports:
        if not is_safe(report): #Could count overall safe reports here if part 1 answer was not required
            count_safe += any([is_safe(report[:i] + report[i+1:]) for i in range(len(report))])

    print(F"\n--- Part Two --- \nUpdated Safe reports: {count_safe}\n")


if __name__ == "__main__":
    main()