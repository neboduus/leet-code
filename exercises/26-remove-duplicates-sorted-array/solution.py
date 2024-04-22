def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    return j + 1


def test(nums, expected_nums):
    k = remove_duplicates(nums)  # Calls your implementation

    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]

    print('SUCCESS')


def main():
    test([1, 1, 2], [1, 2])


if __name__ == "__main__":
    main()
