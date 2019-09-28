def sum_diags(order):
    """
    Excluding the 1 in the middle, if you devide the matrix in half
(left and right), you will see that the sum of the numbers in one half
is equal to the sum of the numbers in the other half. Thus, only one half
needs to be calculated. Here, I'm going to calculate the top-right diagonal
and then the bottom-right based on the former.
    The top-right diagonal (9, 25, 49, 81, ...) has
many patterns and can be represented in many ways. The simplest one is as
the square of the first odd numbers (3^3, 5^5, 7^7, ..., 1001^1001). The sum of this
diagonal can found by n * (4*n**2 - 1) / 3.
    And the bottom-right diagonal has the pattern of being equal to the
last one minus a multiple of six (3^3-6*1, 5^5-6*2, 7^7-6*3, ..., 1001^1001-6*500).
To find the sum, we need to do some algebra.
    
    d1 = 3^3 + 5^5 + 7^7, ..., 1001^1001
    d2 = s1 - 6*(501*250)
    (an+a1)*n/2 = 1+2+3+4,...+500=501*500/2

    And the sum of the four diagonals is (s1+s2)*2+1
"""
    n = (order - 1) / 2
    d1 = (n+1) * (4* (n+1) **2 - 1) / 3 - 1

    d2 = d1 - 3*(n+1)*n
    return (d1+d2)*2 + 1


if __name__ == '__main__':
    matrix_order = 1001
    print(sum_diags(1001))
