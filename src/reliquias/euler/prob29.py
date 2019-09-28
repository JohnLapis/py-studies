def main(la,lb):
    nums = {}

    for a in range(2,la+1):
        b = 2
        if a in nums:
            b = int(lb / nums[a]) + 1
        while b <= lb:
            nums[a**b] = b
            b += 1

    return len(nums)


if __name__ == '__main__':
    print(main(100, 100))
