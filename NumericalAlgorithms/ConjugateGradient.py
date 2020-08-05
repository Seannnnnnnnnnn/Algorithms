def conjugate_gradient(A, b, x_0, tol=1e-6, maxit=10000, cap_residuals=False):
    """ Implementation of the conjugate gradient algorithm """
    r_prev = b - A.dot(x_0)
    p_prev = r_prev
    k = 1

    if cap_residuals:
        residuals = []

    while k < maxit:
        k += 1
        alpha_k = (r_prev.T.dot(r_prev))*(1/p_prev.T.dot(A.dot(p_prev)))
        x_k = x_0 + alpha_k*p_prev
        r_k = r_prev - alpha_k*A.dot(p_prev)
        beta_k = r_k.T.dot(r_k)*(1/r_prev.T.dot(r_prev))
        p_k = r_k + beta_k*p_prev

        if abs(np.linalg.norm(r_k) - np.linalg.norm(r_prev)) < tol:
            break

        if cap_residuals:
            residuals.append(np.linalg.norm(r_k))
        # update iteration:
        p_prev, r_prev, x_0 = p_k, r_k, x_k

    if cap_residuals:
        return x_0, k, residuals
    else:
        return x_0, k
