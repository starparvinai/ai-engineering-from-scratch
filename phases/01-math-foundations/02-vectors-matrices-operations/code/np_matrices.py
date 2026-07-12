import numpy as np

# --- Basic operations ---
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A + B =\n", A + B)                 # element-wise add
print("A * B (element-wise) =\n", A * B)  # ← note: `*` is element-wise!
print("A @ B (matrix multiply) =\n", A @ B)  # ← use `@` for matmul
print("A.T =\n", A.T)                     # transpose is just `.T`

# --- Determinant & inverse ---
print("det(A) =", np.linalg.det(A))
print("A^-1 =\n", np.linalg.inv(A))
print("I =\n", np.eye(2))                 # identity

# --- Broadcasting ---
matrix = np.array([[1, 2, 3], [4, 5, 6]])   # (2, 3)
bias   = np.array([10, 20, 30])              # (3,)
print("matrix + bias =\n", matrix + bias)   # broadcasts to (2, 3)

# --- Two-layer forward pass — same as your Python demo ---
np.random.seed(42)
x  = np.random.randn(3, 1)
W1 = np.random.randn(4, 3)
b1 = np.zeros((4, 1))
W2 = np.random.randn(2, 4)
b2 = np.zeros((2, 1))

z1 = W1 @ x + b1
h1 = np.maximum(0, z1)         # ReLU: element-wise max
z2 = W2 @ h1 + b2

print(f"Layer 1: {W1.shape} @ {x.shape} = {z1.shape}")
print(f"Layer 2: {W2.shape} @ {h1.shape} = {z2.shape}")
print("Output z2:\n", z2)