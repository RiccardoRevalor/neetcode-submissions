class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS -1

        while l <= r:
            m = (l+r) // 2
            m_i_translated = m // COLS
            m_j_translated = m % COLS

            selected = matrix[m_i_translated][m_j_translated]

            if selected == target: return True
            elif selected < target:
                l = m+1
            else:
                r = m-1


        return False


        