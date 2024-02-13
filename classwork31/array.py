def get_array(nums, target):
    start = -1
    end = -1

    for i in range(len(nums)):
        if nums[i] == target:
            start = i
            break

    if start == -1:
        return [start, end]

    for i in reversed(range(start, len(nums))):
        if nums[i] == target:
            end = i
            break

    return [start, end]


print(get_array([1, 2, 3, 4, 7, 4, 7, 4, 4], 4))
