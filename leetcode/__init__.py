def two_sum(nums: list[int], target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    count = len(nums)

    for index in range(count-1):
        if index is count-2:
            sum_a = nums[index] + nums[index+1]
            if sum_a == target:
                return [index, index+1]
            return []
        for each in range(index+1, count):
            sum_a = nums[index] + nums[each]
            if sum_a == target:
                return [index, each]


if __name__ == '__main__':
    nums_ = [11, 15, 2, 17]
    print(type(nums_))
    target_ = 9
    a = two_sum(nums_, target_)
    print(a)
