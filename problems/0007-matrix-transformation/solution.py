import torch

def transform_matrix(A, T, S) -> torch.Tensor:
    """
    Perform the change-of-basis transform T⁻¹ A S and round to 3 decimals using PyTorch.
    Inputs A, T, S can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2×2 tensor or tensor(-1.) if T or S is singular.
    """
    A_t = torch.as_tensor(A, dtype=torch.float)
    T_t = torch.as_tensor(T, dtype=torch.float)
    S_t = torch.as_tensor(S, dtype=torch.float)
    
    det_T = T[0][0] * T[1][1] - T[0][1] * T[1][0]
    det_S = S[0][0] * S[1][1] - S[0][1] * S[1][0]

    if det_S == 0 or det_T == 0:
        return torch.tensor(-1)

    T_inverse = torch.tensor([[T_t[1][1], -T_t[0][1]], [-T_t[1][0], T_t[0][0]]]) / det_T

    result = torch.matmul(torch.matmul(T_inverse, A_t), S_t)

    return result.round(decimals=3)