from collections import Counter

def main():
    print("\n--- Day 1: Historian Hysteria ---")
    with open("input.txt","r") as f:
        data=f.readlines()
        print("Input read")

    list1,list2 = zip(*(map(int, pair.split()) for pair in data))
    total_distance = sum([abs(a-b) for a,b in zip(sorted(list1),sorted(list2))])
    print(F"\n--- Part One ---\nTotal Distance: {total_distance}")

    counts_right = Counter(list2)
    similiarity_score = sum([key * counts_right[key] for key in set(list1)])

    print(F"\n--- Part Two --- \nSimilarity Score = {similiarity_score}\n")


if __name__ == "__main__":
    main()