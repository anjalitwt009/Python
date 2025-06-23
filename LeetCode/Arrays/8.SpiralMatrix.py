# MEDIUM



# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:

# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:

# Input: n = 1
# Output: [[1]]

 

# Constraints:

#     1 <= n <= 20



def generateMatrix(self,n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0]*n for _ in range(n)]
        
        L, R = 0, n-1
        T, B = 0, n-1
        val = 1

        while L <= R and T <= B:
            # Fill top row
            for c in range(L, R+1):
                mat[T][c] = val
                val += 1
            T += 1

            # Fill right column
            for r in range(T, B+1):
                mat[r][R] = val
                val += 1
            R -= 1

            # Fill bottom row (check if still valid)
            if T <= B:
                for c in range(R, L-1, -1):
                    mat[B][c] = val
                    val += 1
                B -= 1

            # Fill left column (check if still valid)
            if L <= R:
                for r in range(B, T-1, -1):
                    mat[r][L] = val
                    val += 1
                L += 1

        return mat
