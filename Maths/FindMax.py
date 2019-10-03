# NguyenU

def find_max(nums):
    maxNum = nums[0]
    for x in nums:
      if x > maxNum:
        maxNum = x
    print(maxNum)

def main():
  find_max([2, 4, 9, 7, 19, 94, 5])

if __name__ == '__main__':
  main()
