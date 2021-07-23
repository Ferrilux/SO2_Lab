#!/usr/bin/env python3

import os
import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Invalid number of arguments')
        sys.exit(1)

    srcpath = sys.argv[1]
    destpath = sys.argv[2]

    if not os.path.isdir(srcpath):
        print(f'{srcpath}: file does not exist or is not a directory')
        sys.exit(2)

    if not os.path.isdir(destpath):
        print(f'{destpath}: file does not exist or is not a directory')
        sys.exit(3)

    for root, dirs, files in os.walk(srcpath):
        for filename in dirs + files:
            filepath = os.path.join(root, filename)
            destfile = os.path.join(
                destpath, filepath[filepath.index(srcpath) + len(srcpath):])
            if os.path.islink(filepath):
                target = os.path.realpath(filepath)
                os.symlink(target, destfile)
            elif os.path.isdir(filepath):
                os.mkdir(destfile)
            elif os.path.isfile(filepath):
                os.mknod(destfile)
