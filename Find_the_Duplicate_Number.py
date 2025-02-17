def duplicate(num: list[int]) -> int:
    size = len(num)
    slow, fast = num[0], num[0]

    while True:
        slow = num[slow]
        fast = num[num[fast]]
        if slow == fast:
            break

    slow = num[0]
    while slow != fast:
        slow = num[slow]
        fast = num[fast]

    return slow

ans = duplicate([1,3,4,2,2])
print(ans)
