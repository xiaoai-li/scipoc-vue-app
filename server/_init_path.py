import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.append(path)
        # print(sys.path)

this_dir = osp.dirname(__file__)

lib_path = osp.join(this_dir, './', 'scipoc')
add_path(lib_path)
