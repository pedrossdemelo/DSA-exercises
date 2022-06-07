# https://leetcode.com/problems/product-of-array-except-self/


def productExceptSelf(nums):
    result = [0] * len(nums)
    result[0] = 1

    # Calculate the product of all nums before index, with 1 as the default
    last_prefix_product = 1
    for i in range(len(nums) - 1):
        last_prefix_product *= nums[i]
        result[i + 1] = last_prefix_product

    # Calculate the product of all nums after index, with 1 as the default
    last_postfix_product = 1
    for i in range(len(nums) - 1, 0, -1):
        last_postfix_product *= nums[i]
        result[i - 1] *= last_postfix_product

    return result


print(productExceptSelf([1, 2, 3, 4, 9]))
