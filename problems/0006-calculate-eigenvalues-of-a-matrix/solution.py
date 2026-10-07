import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2x2 matrix using PyTorch.
    Input: 2x2 tensor; Output: 1-D tensor with the two eigenvalues in descending order (highest to lowest).
    """
    eigenvalues, eigenvectors = torch.linalg.eig(matrix)

    return torch.sort(eigenvalues.real, descending=True)[0]
