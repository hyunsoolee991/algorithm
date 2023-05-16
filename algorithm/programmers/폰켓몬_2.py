def solution(nums):
    tmp = dict()
    for num in nums:
        if num not in tmp:
            tmp[num] = 1

    if len(tmp) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(tmp)