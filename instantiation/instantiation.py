# -*- coding: utf-8 -*-

import logging
from sys import version_info
from warnings import warn

if version_info.major >= 3:
    from time import perf_counter as clock
else:
    from time import clock as clock


def main(iteractions=10000000):
    logging.basicConfig(level=logging.INFO)
    logging.info("Testing list instantiation with {} iteractions".format(iteractions))

    init = clock()
    for _ in range(iteractions):
        _ = list()

    finish = clock()
    logging.info("Instantiation using 'list()' took {}s".format(str(finish - init)))

    init = clock()
    for _ in range(iteractions):
        _ = []

    finish = clock()
    logging.info("Instantiation using '[]' took {}s".format(str(finish - init)))


if __name__ == "__main__":
    main()
