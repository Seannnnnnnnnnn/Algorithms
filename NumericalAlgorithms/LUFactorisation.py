""" An implementaition of algorithms for LU Decomposiiton. All functions perform LU Decomposition in-place. """

import numpy as np


def lu_kij(a: np.ndarray) -> np.ndarray:
    """ implements the lu kij version of lu decomposition """
    n = len(a)
    for k in range(n):
        for i in range(k+1, n):
            a[i, k] = a[i, k]/a[k, k]
            for j in range(k+1, n):
                a[i, j] = a[i, j] - a[i, k]*a[k, j]

    return a


def lu_ikj(a: np.ndarray) -> np.ndarray:
    """ implements the lu ikj version of lu decomposition """
    n = len(a)
    for i in range(1, n):
        for k in range(1, i-1):
            a[i, k] = a[i, k]/a[k, k]
            for j in range(k+1, n):
                a[i, j] = a[i, j] - (a[i, k]*a[k, j])

    return a


def lu_banded(a: np.ndarray, b: int) -> np.ndarray:
    """ implements banded lu decomposition, where b is the bandwidth of A """
    n = len(a)
    for i in range(1, n):
        for k in range(max(1, b-1), i - 1):
            a[i, k] = a[i, k] / a[k, k]
            for j in range(k + 1, min(i+b, n)):
                a[i, j] = a[i, j] - (a[i, k] * a[k, j])

    return a


if __name__ == '__main__':
    A = np.array([[2, 2, 9],
                  [4, 6, 15],
                  [-6, -8, -13]])

    print(lu_kij(A))
    print()
    print(lu_ikj(A))
    print()
