class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Check if the rectangles overlap along both X and Y dimensions
        has_x_overlap = min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])
        has_y_overlap = min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])
        
        return has_x_overlap and has_y_overlap