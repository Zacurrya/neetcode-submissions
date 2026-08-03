class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(row):
            l, r = 0, len(row)-1

            while l<=r:
                m = l + ((r-l) // 2)
                if row[m] == target:
                    return True
                elif target < row[m]:
                    r = m-1
                else:
                    l = m+1

        for row in matrix:
            if binSearch(row):
                return True


        # target not found
        return False