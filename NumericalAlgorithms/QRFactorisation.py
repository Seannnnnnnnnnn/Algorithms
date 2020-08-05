""" we implement the different methods of QR factorisation and compare their performance  """
import numpy as np


def modified_qr_factorization(matrix):
    """ Implements the 'standard' Gram-Schmidt Algorithm """
    m, n = matrix.shape

    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = matrix[:, j]

        for i in range(j-1):
            q = Q[:, i]
            R[i, j] = q.dot(v)
            v = v - R[i, j] * q

        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R


def qr_factorization(matrix):
    """ Implements the modified Gram-Schmidt Algorithm - improving numerical stability """
    m, n = matrix.shape

    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = matrix[:, j]

        for i in range(j-1):
            q = Q[:, i]
            R[i, j] = q.dot(matrix[:, j])
            v = v - R[i, j] * q

        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R


def householder_qr(R):
    """ implementation of Full QR factorisation as per lecture notes """
    m, n = R.shape
    Q = np.eye(m)
    for i in range(n):
        H = np.eye(m)
        H[i:, i:] = make_householder_matrix(R[i:, i])
        Q = np.dot(Q, H)
        R = np.dot(H, R)
    return Q, R


def make_householder_matrix(a):
    """ generates the ith Householder Matrix in our sequence of transformations """
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H


def in_built(matrix):
    """ performs QR factorisation using the in-built householder transfrom by SciPy """
    return np.linalg.qr(matrix)


def vandermonde():
    """ returns the Vandermone matrix - as it is 'notoriously ill-conditioned' it forms a good basis for comparison """
    m = 100
    n = 15
    t = np.linspace(0, 1, m, endpoint=True)

    # the numpy method for producing the vandermonde matrix returns along the wrong way, hence we use the flip method.
    return np.flip(np.vander(t, n), 1)


def test_grams():
    V = vandermonde()
    print("Standard Graham-Shmidt:")
    output = qr_factorization(V)
    q, r = output[0], output[1]
    print(np.linalg.norm(np.matmul(q.transpose(), q) - np.eye(15)))
    print(np.linalg.norm(V - np.matmul(q, r)))

    print("\n\nModified Graham-Schmidt:")
    output = modified_qr_factorization(V)
    q, r = output[0], output[1]
    print(np.linalg.norm(np.matmul(q.transpose(), q) - np.eye(15)))
    print(np.linalg.norm(V - np.matmul(q, r)))

    print("\n\nIn built QR factorisation using Numpy:")
    output = in_built(V)
    q, r = output[0], output[1]
    print(np.linalg.norm(np.matmul(q.transpose(), q) - np.eye(15)))
    print(np.linalg.norm(V - np.matmul(q, r)))

    print("\n\nHouseholder:")
    output = householder_qr(V)
    q, r = output[0], output[1]
    print(np.linalg.norm(np.matmul(q.transpose(), q) - np.eye(100)))
    print(np.linalg.norm(V - np.matmul(q, r)))
    return


if __name__ == '__main__':
    """ tests some matrices """
    test_grams()
