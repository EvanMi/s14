# -*- coding:utf-8 -*-
# Author: Evan Mi


def threeSumClosest( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) < 3:
        return 0

    closest_sum = nums[0] + nums[1] + nums[2]
    nums.sort()
    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                elif k != len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    if abs(target-(nums[i]+nums[j]+nums[k])) < abs(target-closest_sum):
                        closest_sum = nums[i]+nums[j]+nums[k]
                    while nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > target:
                    if abs(target - (nums[i]+nums[j]+nums[k])) < abs(target-closest_sum):
                        closest_sum = nums[i]+nums[j]+nums[k]
                    while nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] == target:
                    return target

    return closest_sum

print(threeSumClosest([1,2,5,10,11],12))
