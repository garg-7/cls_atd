import os
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, 'LightCNN')
source = os.path.join(path, 'data')

t = dir_path.rsplit('/', 1)[0]
path = os.path.join(t, 'static')
dest = os.path.join(path, 'extracted')
copytree(source, dest)
