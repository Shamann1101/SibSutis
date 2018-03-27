from __future__ import division
from numba import cuda, float32
import numpy as np
from timeit import default_timer as time
import math

# Controls threads per block and shared memory usage.
# The computation will be done on blocks of TPBxTPB elements.
TPB = 16
N = 2 ** 10


def matrix_multiplication(first_matrix, second_matrix, new_matrix, accuracy=4):
    """
    Matrix multiplication
    :param first_matrix: list
    :param second_matrix: list
    :param accuracy: int Rounding accuracy of values in decimal places
    :return:
    """
    try:
        if len(first_matrix[0]) != len(second_matrix):
            raise ValueError(1)
        if type(accuracy) != int:
            raise TypeError
        if accuracy <= 0:
            raise ValueError(2)
    except ValueError as e:
        if 1 in e.args:
            print("The dimension of the matrices is not suitable for multiplication")
        elif 2 in e.args:
            print("The accuracy of calculation can not be negative or null")
    except TypeError:
        print("The accuracy type must be int")
    else:
        for i in range(len(first_matrix)):
            for j in range(len(second_matrix[0])):
                value = 0
                for k in range(len(second_matrix)):
                    value += first_matrix[i][k] * second_matrix[k][j]
                new_matrix[i][j] = round(value, accuracy)


@cuda.jit
def fast_matmul(A, B, C):
    """
    Perform matrix multiplication of C = A * B
    Each thread computes one element of the result matrix C
    """

    # Define an array in the shared memory
    # The size and type of the arrays must be known at compile time
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x, y = cuda.grid(2)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y

    if x >= C.shape[0] and y >= C.shape[1]:
        # Quit if (x, y) is outside of valid C boundary
        return

    # Each thread computes one element in the result matrix.
    # The dot product is chunked into dot products of TPB-long vectors.
    tmp = 0.
    for i in range(int(A.shape[1] / TPB)):
        # Preload data into shared memory
        sA[tx, ty] = A[x, ty + i * TPB]
        sB[tx, ty] = B[tx + i * TPB, y]

        # Wait until all threads finish preloading
        cuda.syncthreads()

        # Computes partial product on the shared memory
        for j in range(TPB):
            tmp += sA[tx, j] * sB[j, ty]

        # Wait until all threads finish computing
        cuda.syncthreads()

    C[x, y] = tmp


# The data array
A = np.random.random((N * 2, N * 3)).astype(np.float)
B = np.random.random((N * 3, N * 1)).astype(np.float)
height, _ = A.shape
_, width = B.shape
C = np.full((height, width), 0, np.float)
elements = height * width

A_global_mem = cuda.to_device(A)
B_global_mem = cuda.to_device(B)
C_global_mem = cuda.device_array((height, width))  # [32 x 16] matrix result

# Configure the blocks
threadsperblock = (TPB, TPB)
blockspergrid_x = int(math.ceil(A.shape[0] / threadsperblock[1]))
blockspergrid_y = int(math.ceil(B.shape[1] / threadsperblock[0]))
blockspergrid = (blockspergrid_x, blockspergrid_y)

# Start the kernel
print('Number of elements: %d' % elements)

ts = time()
matrix_multiplication(A, B, C)
te = time()

total_time = (te - ts)

print('Execution time %.4f' % total_time)
print('Throughput %.4f' % (elements / total_time))

ts = time()
fast_matmul[blockspergrid, threadsperblock](A_global_mem, B_global_mem, C_global_mem)
te = time()
res = C_global_mem.copy_to_host()

total_time = (te - ts)

print('Execution time %.4f' % total_time)
print('Throughput %.4f' % (elements / total_time))

assert C.all() == res.all()

"""
Execution time 6265.3620
Throughput 0.0460
Execution time 0.2679
Throughput 1074.8435
"""
