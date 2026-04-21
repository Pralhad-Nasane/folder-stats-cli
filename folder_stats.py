import os
import sys


def calculate_stats(folder_path):
    total_files = 0

    for root, dirs, files in os.walk(folder_path):
        total_files += len(files)
    return total_files


if __name__ == "__main__":
    if len(sys.argv) < 2:  
        print("Usage: python folder_stats.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.exists(folder_path):  
        print("Invalid folder path")
        sys.exit(1)

    total = calculate_stats(folder_path)
    print("Total files:", total)