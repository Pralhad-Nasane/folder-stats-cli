import os
import sys


def calculate_stats(folder_path): 
    total_files = 0
    total_size = 0 

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path) 

    return total_files, total_size 


if __name__ == "__main__":
    folder_path = sys.argv[1]
    files, size = calculate_stats(folder_path) 
    print("Total files:", files)
    print("Total size (bytes):", size) 