nums = [2,7,11,15]
target = 9
def twosum(nums, target):
    hash_map = {}  # number → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i


    return[]
print(twosum(nums,target))


