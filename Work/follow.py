import os
import time
import csv

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

if __name__ == '__main__':

    lines = follow()
    rows = csv.reader(lines)
    for row in rows:
        print(row)




