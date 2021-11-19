#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    num = len(sys.argv)
    for i in range(1, num):
        sum += int(sys.argv[i])
    print(sum)
