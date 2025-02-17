def generate_pattern(row):
    for i in range(1,row + 1):
        if i  % 2 != 0:
            print('+' * i)
        else:
            print('-' * i)
        
def main():
    row = int(input("enter number of rows"))
    generate_pattern(row)

if __name__ == "__main__":
    main()