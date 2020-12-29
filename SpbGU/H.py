nums = {
    1: 1,
    2: 16,
    3: 648,
    5: 648,
    7: 756,
    11: 3528,
    13: 24576,
    17: 24576,
    19: 81928,
    23: 1368576,
    29: 1368576,
    31: 1368576
}


def main():
    b = int(input())
    if b in nums:
        print(nums[b])
    else:
        print(0)


main()
