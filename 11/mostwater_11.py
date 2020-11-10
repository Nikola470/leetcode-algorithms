class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_container = 0

        for i in range(len(height) - 1):
            for j in range(1, len(height)):
                if height[i] < height[j]:
                    min = height[i]
                else:
                    min = height[j]
                if min * (j - i) > max_container:
                    max_container = min * (j - i)
        return max_container


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    test = Solution()
    print(test.maxArea(height))
