class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        lenH = len(heights)
        maxArea = -1

        for i in range(lenH):
            while stack[-1] != -1 and heights[i] < heights[ stack[-1] ]:
                topEleIdx = stack.pop()
                topEle = heights[ topEleIdx ]
                area = topEle * (i - stack[-1] - 1)
                maxArea = max(area, maxArea)
            stack.append(i)
        
        # for remaining elements
        while stack[-1] != -1:
            topEleIdx = stack.pop()
            topEle = heights[ topEleIdx ]
            area = topEle * (lenH - stack[-1] - 1)
            maxArea = max(area, maxArea)

        return maxArea

