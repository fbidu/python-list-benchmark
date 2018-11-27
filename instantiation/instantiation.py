# -*- coding: utf-8 -*-

from sys import version_info

if version_info.major >= 3:
    from time import perf_counter as clock
else:
    from time import clock as clock


def main(iteractions=10000000):
    print("Testing list instantiation with {} iteractions".format(iteractions))

    init = clock()
    for _ in range(iteractions):
        _ = list()

    finish = clock()
    print("Instantiation using 'list()' took {}s".format(str(finish - init)))

    init = clock()
    for _ in range(iteractions):
        _ = []

    finish = clock()
    print("Instantiation using '[]' took {}s".format(str(finish - init)))

if __name__ == "__main__":
    main()
