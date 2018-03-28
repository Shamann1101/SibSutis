from __future__ import division
import sys
from numba import cuda, float32
import numpy as np
from timeit import default_timer as timeit
import time
import math

# Controls threads per block and shared memory usage.
# The computation will be done on blocks of TPBxTPB elements.
TPB = 16
LOGFILE = "log.txt"


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
    # The size and type of the arrays must be known at compile timeit
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


def iterate(start_time, mul=1, ah=2, aw=3, bh=3, bw=1):
    n = 2 ** (3 + mul)
    assert aw == bh
    ah, aw, bh, bw = ah*mul, aw*mul, bh*mul, bw*mul

    # The data array
    A = np.random.random((n * ah, n * aw)).astype(np.float)
    B = np.random.random((n * bh, n * bw)).astype(np.float)
    height_a, width_a = A.shape
    height_b, width_b = B.shape
    C = np.full((height_a, width_b), 0, np.float)
    elements = height_a * width_b

    A_global_mem = cuda.to_device(A)
    B_global_mem = cuda.to_device(B)
    C_global_mem = cuda.device_array((height_a, width_b))  # [32 x 16] matrix result

    # Configure the blocks
    threadsperblock = (TPB, TPB)
    blockspergrid_x = int(math.ceil(A.shape[0] / threadsperblock[1]))
    blockspergrid_y = int(math.ceil(B.shape[1] / threadsperblock[0]))
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    # Start the kernel
    # start = timeit()

    ts = timeit()
    matrix_multiplication(A, B, C)
    te = timeit()

    total_time = (te - ts)
    throughput = elements / total_time

    ts = timeit()
    fast_matmul[blockspergrid, threadsperblock](A_global_mem, B_global_mem, C_global_mem)
    te = timeit()
    res = C_global_mem.copy_to_host()

    total_time_c = (te - ts)
    throughput_c = elements / total_time_c

    assert C.all() == res.all()

    with open(LOGFILE, "a") as file:
        log = 'Start: {}\n' \
              'Dimension: [{}x{}] x [{}x{}]\n' \
              'CPU\n' \
              'Execution timeit: {:.4}\n'\
              'Throughput: {}\n'\
              'GPU\n' \
              'Execution timeit: {:.4}\n'\
              'Throughput: {}\n'\
            .format(
                time.ctime(start_time),
                height_a, width_a, height_b, width_b,
                total_time,
                throughput,
                total_time_c,
                throughput_c
            )
        print(log, file=file, sep="\n")


def main():
    iter1 = 1
    if len(sys.argv[1:]):
        iter1 = int(sys.argv.pop(1))

    for i in range(iter1):
        iterate(time.time(), i+1)

if __name__ == '__main__':
    main()
