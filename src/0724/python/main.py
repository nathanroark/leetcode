# driver file to test the leetcode problem

from solution import Solution


def main():
    print("Example 1:")
    print("Input: nums = [1, 7, 3, 6, 5, 6]")
    nums = [1, 7, 3, 6, 5, 6]
    print(Solution().pivotIndex(nums))
    print("-----------------------------\n")

    print("Example 2:")
    print("Input: nums = [1, 2, 3]")
    nums = [1, 2, 3]
    print(Solution().pivotIndex(nums))
    print("-----------------------------\n")

    print("Example 3:")
    print("Input: nums = [2, 1, -1]")
    nums = [2, 1, -1]
    print(Solution().pivotIndex(nums))
    print("-----------------------------\n")

    print("Example 4:")
    print("Input: nums = [0, 0, 0, 0, 1]")
    nums = [0, 0, 0, 0, 1]
    print(Solution().pivotIndex(nums))
    print("-----------------------------\n")

    print("Example 5:")
    print("Input: nums = [-1, -1, -1, 0, 1, 1]")
    nums = [-1, -1, -1, 0, 1, 1]
    print(Solution().pivotIndex(nums))
    print("-----------------------------\n")

    print("Example 6:")
    print("Input: nums = [-1, -1, -1, -1, -1, 0]")
    nums = [-1, -1, -1, -1, -1, 0]
    print(Solution().pivotIndex(nums))
    print("-----------------------------\n")

    print("Example 7:")
    print("Input: nums = [-1, -1, -1, -1, -1, -1]")
    nums = [-1, -1, -1, -1, -1, -1]
    print(Solution().pivotIndex(nums))
    print("-----------------------------\n")


if __name__ == "__main__":
    main()
