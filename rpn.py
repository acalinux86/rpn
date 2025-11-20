#!/usr/bin/env python3

import sys

def shift_args(argv) -> str:
    if (len(argv) == 0):
        print(f"[ERROR] Nothing to Pop")
        exit(1)
    else:
        return argv.pop(0)

def main() -> int:
    argv = sys.argv[:]
    subcommand = shift_args(argv)
    if len(sys.argv) <= 0:
        print("[ERROR] Usage: %s <input_file>" % subcommand)
        return 1

    path = shift_args(argv)
    with open(path, "r") as f:
        print(f.read())
    return 0

if __name__ == "__main__":
    ret = main()
    exit(ret)
