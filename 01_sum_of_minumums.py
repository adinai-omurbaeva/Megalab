def sum_of_minimums(numbers):
    result = sum([min(nums) for nums in numbers])
    return result