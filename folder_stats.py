import os
import sys


def calculate_stats(folder_path):
    total_files = 0

    for root, dirs, files in os.walk(folder_path):
        total_files += len(files)

    return total_files


if __name__ == "__main__":
    folder_path = sys.argv[1]
    total = calculate_stats(folder_path)
    print("Total files:", total)
