from __future__ print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")
