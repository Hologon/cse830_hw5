from sorting import *
import timeit
from functools import partial
import matplotlib.pyplot as plt


# Timing method inspired by
# https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
def main():
    ITERATIONS = 100
    REPEATS = 5
    N = 200

    ks = list(range(N+1))
    hybrid_times = []
    best_k, min_time = None, float("inf")
    for k in ks:
        ts = timeit.Timer(partial(test_sort, hybrid_sort, N, k)).repeat(REPEATS, ITERATIONS)
        t = (min(ts) / ITERATIONS) * 1e6
        hybrid_times.append(t)

        if t < min_time:
            best_k = k
            min_time = t

    print(f"The threshold (k) which produces the fastest runtime is {best_k}")

    plt.xlabel("Hybrid Sort Threshold (k)")
    plt.ylabel("Runtime (μs)")
    plt.plot(ks, hybrid_times, label="Hybrid Sort")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
