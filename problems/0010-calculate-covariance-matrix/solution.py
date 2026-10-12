import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

    covariance_matrix = np.array(vectors, dtype=float)

    avg = []
    
    for i in range(covariance_matrix.shape[0]):
        sum = 0
        for j in range(covariance_matrix.shape[1]):
            sum+=covariance_matrix[i][j]
        avg.append(sum/covariance_matrix.shape[1])


    for i in range(covariance_matrix.shape[0]):
         for j in range(covariance_matrix.shape[1]):
            covariance_matrix[i][j] -= avg[i]

    final_cov_mat = []
    for i in range(covariance_matrix.shape[0]):   
        rows = [] 
        for j in range(covariance_matrix.shape[0]):
            val = 0 
            for k in range(covariance_matrix.shape[1]):
                val += covariance_matrix[i][k] * covariance_matrix[j][k]
            rows.append(float(val/(covariance_matrix.shape[1] - 1)))
        final_cov_mat.append(rows)

    return final_cov_mat