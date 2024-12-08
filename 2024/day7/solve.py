
from math import ceil, log


def concatenate(num1,num2):
    return num1*10**ceil(log(num2+1,10)) + num2

def is_true_1(operands, result):
    if len(operands) == 1:
        return operands[0] == result
    summ = operands[0] + operands[1]
    if summ <= result and is_true_1([summ,*operands[2:]],result):
        return True
    product = operands[0] * operands[1]
    if product <= result and is_true_1([product,*operands[2:]],result):
        return True 
    return False

def is_true_2(operands, result):
    if len(operands) == 1:
        return operands[0] == result
    summ = operands[0] + operands[1]
    if summ <= result and is_true_2([summ,*operands[2:]],result):
        return True
    product = operands[0] * operands[1]
    if product <= result and is_true_2([product,*operands[2:]],result):
        return True 
    joined = concatenate(operands[0],operands[1])
    if joined <= result and is_true_2([joined,*operands[2:]],result):
        return True 
    return False


def main():
    print("\n--- Day 6: Bridge Repair ---")
    with open("input.txt","r") as f:
        lines = f.readlines()
        print("Input read")

    
    total1 = total2 = 0
    for line in lines:
        result ,operands = line.split(':')
        result = int(result)
        operands = [int(operand) for operand in operands.split()]
        total1 += result * is_true_1(operands, result)
        total2 += result * is_true_2(operands, result)
    
    print(f"\n--- Part One ---\nTotal calibration result: {total1}")
    print(f"\n--- Part Two --- \nTotal calibration result: {total2}\n")

if __name__ == "__main__":
    main()