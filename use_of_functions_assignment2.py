import math

def Avg(lst):
    return sum(lst) / sum(1 for _ in lst)

def sumSqDiff(lst, avg):
    ssd = sum((x - avg) ** 2 for x in lst)
    return ssd

def main():
    numbers = [10, 20, 30, 40, 50]  
    count = sum(1 for _ in numbers)  
    avg = Avg(numbers)
    ssd = sumSqDiff(numbers, avg)
    std_dev = math.sqrt(ssd / count)
    print("Standard Deviation:", std_dev)

main()