def twoSum(nums: list[int], target: int) -> list[int]:
    index = {}

    for i, num in enumerate(nums):
        comp = target - num

        if comp in index:
            return [index[comp], i]

        index[num] = i

ans = twoSum([3,2,4],6)
print(ans)
