import math
import numpy as np
from timeit import default_timer as timer
from numba import vectorize, jit, cuda


@vectorize(['float64(float64, float64)'], target='cuda')
def gpu_intensive_operation(a, b):
    """
    This function is supposed to mock a GPU intensive job
    :return:
    """
    return math.sqrt(a) ** math.sqrt(b)


def main():
    print('GPU intensive load')
    vec_size = 100000000
    a = b = np.array(np.random.sample(vec_size), dtype=np.float64)
    c = np.zeros(vec_size, dtype=np.float64)
    start = timer()
    c = gpu_intensive_operation(a, b)
    duration = timer() - start
    print(duration)


if __name__ == "__main__":
    main()
