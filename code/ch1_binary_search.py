def binary_search(nums: range, target: int):
    low = 0
    high = len(nums) - 1
    steps = 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Guess {mid}")
        guess = nums[mid]
        if guess == target:
            print(f"Steps to get to {target}", steps)
            return mid
        if guess > target:
            high = mid - 1
            steps += 1
        else:
            low = mid + 1
            steps += 1
    return None


if __name__ == "__main__":
    my_list = range(10e10)
    binary_search(my_list, 666)
