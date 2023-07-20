#!/usr/bin/python3
""" """

import sys


file__size, count = 0, 0
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {key: 0 for key in codes}


def display_stats(stats, file_size):
    print("File size: {:d}".format(file__size))
    for key, value in sorted(stats.items()):
        if v:
            print("{}: {}".format(key, value))


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_num = data[-2]
                if status_num in stats:
                    stats[status_num] += 1
            except BaseException:
                pass
            try:
                file__size += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                display_stats(stats, file__size)
        display_stats(stats, file__size)
    except KeyboardInterrupt:
        display_stats(stats, file__size)
        raise
