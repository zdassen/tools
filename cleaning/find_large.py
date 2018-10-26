# -*- coding: utf-8 -*-
#
# find_large.py
#
import os


def find_large(target_dir, thres_mb=20, max_depth=3):
    """指定以上のサイズのディレクトリを探す"""
    _find(target_dir, thres_mb, 0, max_depth)


def _find(target_dir, thres_mb, depth=0, max_depth=3):
    """ディレクトリ走査用の関数"""

    # 深さが ( 開始位置からの ) 上限に達した場合は終了 
    if depth > max_depth:
        return

    pathes = os.listdir(target_dir)
    for path in pathes:

        # isdir() を動作させるためにここで join() する
        path = os.path.join(target_dir, path)

        if os.path.isdir(path):

            # ディレクトリのサイズを計算する
            total_size = 0.0
            with os.scandir(path) as it:
                for entry in it:
                    total_size += entry.stat().st_size

            # 指定以上のサイズのディレクトリ名を表示する
            if total_size > thres_mb * 1000 * 1000:
                filename = os.path.basename(path)
                print("%s%s (%.2fMB)" % (
                    " " * 4 * depth, filename, total_size / 1000 / 1000
                ))

            _find(path, thres_mb, depth + 1, max_depth)

        # end of if os.path.isdir(path) ...
    # end of for path in pathes ...


def main():
    target_dir = "C:\\workspace\\c#\\"
    find_large(target_dir, thres_mb=0.1, max_depth=1)


if __name__ == '__main__':
    # main()
    pass