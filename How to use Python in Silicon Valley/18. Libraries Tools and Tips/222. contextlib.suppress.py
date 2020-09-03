import contextlib
import os

print(os.getcwd())

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')