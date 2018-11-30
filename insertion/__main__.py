"""
Which one is faster?

l = []
l.append(1)

or

l = []
l.insert(len(l), 1)
"""
from sys import argv
from time import perf_counter


def main(iteractions=1000000):

    """
    Testing the append method
    """
    l = []
    start = perf_counter()

    for i in range(iteractions):
        l.append(i)

    finish = perf_counter()
    print("Append of {0} items took {1:.4f}s".format(iteractions, finish - start))

    """
    Testing the extend method
    """
    l = []
    start = perf_counter()

    for i in range(iteractions):
        l.extend([i])

    finish = perf_counter()
    print("Extend of {0} items took {1:.4f}s".format(iteractions, finish - start))

    """
    Testing the insert method
    """
    l = []
    start = perf_counter()

    for i in range(iteractions):
        l.insert(i, i)

    finish = perf_counter()
    print("Insert of {0} items took {1:.4f}s".format(iteractions, finish - start))


if __name__ == "__main__":
    if len(argv) > 1 and argv[1].isnumeric():
        main(iteractions=int(argv[1]))
    else:
        main()
