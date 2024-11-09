from sorting import *
import timeit
from functools import partial
import matplotlib.pyplot as plt


# Timing method inspired by
# https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
def main():
    ITERATIONS = 100
    REPEATS = 5
    MAX_N = 1000

    ns = []
    insertion_times = []
    merge_times = []
    for n in range(5, MAX_N+1, 5):
        ins_ts = timeit.Timer(partial(test_sort, insertion_sort, n)).repeat(REPEATS, ITERATIONS)
        ins_t = (min(ins_ts) / ITERATIONS) * 1e6

        merge_ts = timeit.Timer(partial(test_sort, merge_sort, n)).repeat(REPEATS, ITERATIONS)
        merge_t = (min(merge_ts) / ITERATIONS) * 1e6

        ns.append(n)
        insertion_times.append(ins_t)
        merge_times.append(merge_t)

    plt.xlabel("Array Size (n)")
    plt.ylabel("Runtime (μs)")
    plt.plot(ns, insertion_times, label="Insertion Sort")
    plt.plot(ns, merge_times, label="Merge Sort")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
