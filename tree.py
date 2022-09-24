#!/usr/bin/env python
# coding=utf-8
import os
import argparse

from RainbowPrint import RainbowPrint as rp

global_color = [rp.red, rp.green, rp.yellow, rp.blue, rp.magenta, rp.cyan]


# 传递prefix
def tree(rootDir, deep, max_deepth, prefix_line, show_hide_file):
    if deep > max_deepth:
        return
    for index, file in enumerate(os.listdir(rootDir)):
        if file.startswith(".") and not show_hide_file:
            # print(file)
            continue
        path = os.path.join(rootDir, file)
        parent = False
        prefix = "├──"
        if index == len(os.listdir(rootDir)) - 1:
            prefix = "└──"
            parent = True
        if deep == 0:
            prefix_line = ""

        if os.path.isdir(path):
            # file = rp.blue(file)
            file = global_color[deep % len(global_color)](file)
            prefix = global_color[deep % len(global_color)](prefix)
        out = prefix_line + "{} {}".format(prefix, file)
        print(out)
        if os.path.isdir(path):
            after = global_color[deep % len(global_color)]("│   ") if not parent else "    "
            # print("z" + after + "z" + str(parent) + str(index) + " " + str(len(os.listdir(rootDir)) - 1))
            tree(path, deep + 1, max_deepth, prefix_line + after, show_hide_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("For test the parser")
    parser.add_argument('path', default="./")
    parser.add_argument('-hide', '--hide', default=False, help='just for help')
    parser.add_argument('-max', '--max', type=int, default=10, help='just for help')

    args = parser.parse_args()

    print(".")
    tree(args.path, 0, args.max, "", args.hide)
