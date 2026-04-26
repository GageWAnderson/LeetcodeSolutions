class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products: List[int] = []
        postfix_products: List[int] = [0 for _ in range(len(nums))]
        prefix_product = 1
        for num in nums:
            prefix_product *= num
            prefix_products.append(prefix_product)

        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_product *= nums[i]
            postfix_products[i] = postfix_product

        ans = []
        for i in range(len(nums)):
            prefix_product_at_i, postfix_product_at_i = 1, 1
            if i > 0:
                prefix_product_at_i = prefix_products[i - 1]
            if i < len(nums) - 1:
                postfix_product_at_i = postfix_products[i + 1]
            ans.append(prefix_product_at_i * postfix_product_at_i)
        return ans


# NOTE: Best solution in O(1) space uses a hack that the problem statement doesn't define the answer array as extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):
            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
