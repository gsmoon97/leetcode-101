class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find products of all numbers that precede the current number (i.e., self)
        pre_products = []
        pre_product = 1
        for num in nums:
            pre_products.append(pre_product)
            pre_product *= num
        
        # find products of all numbers that follows the current number (i.e., self)
        post_products = []
        post_product = 1
        for num in reversed(nums):  # reverse the list to process from back to front
            post_products.append(post_product)
            post_product *= num
        post_products.reverse()  # reverse the order to align with the corresponding numbers (O(n))

        # multiply the corresponding "pre-product" and "post-product"
        return [pre * post for pre, post in zip(pre_products, post_products)]