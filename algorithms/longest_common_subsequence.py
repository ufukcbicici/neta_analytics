import numpy as np


class LCS:
    def __init__(self):
        pass

    @staticmethod
    def lcs(x, y):
        m = len(x)
        n = len(y)
        lcs_arr = np.zeros(shape=(m + 1, n + 1), dtype=np.int32)

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    lcs_arr[i, j] = 0
                elif x[i - 1] == y[j - 1]:
                    lcs_arr[i, j] = lcs_arr[i - 1, j - 1] + 1
                else:
                    lcs_arr[i, j] = max(lcs_arr[i - 1, j], lcs_arr[i, j - 1])

        lcs_container = [None] * lcs_arr[m, n]

        # Backtracking to find the LCS
        i = m
        j = n
        lcs_index = len(lcs_container) - 1
        while i > 0 and j > 0:
            # If current character in X[] and Y are same, then
            # current character is part of LCS
            if x[i - 1] == y[j - 1]:
                assert 0 <= lcs_index <= len(lcs_container) - 1
                lcs_container[lcs_index] = x[i - 1]
                i -= 1
                j -= 1
                lcs_index -= 1
            # If not same, then find the larger of two and
            # go in the direction of larger value
            elif lcs_arr[i - 1, j] > lcs_arr[i, j - 1]:
                i -= 1
            else:
                j -= 1
        return lcs_container

