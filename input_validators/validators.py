#!/usr/bin/env python3
import re
import sys

try:
    N = int(sys.stdin.readline())
except:
    # first line containing N, is not an integer
    sys.exit(43)

try:
    elements = sys.stdin.readline().split()
except:
    # something went wrong
    sys.exit(43)

if N != len(elements):
    # N is false, and our input cannot be validated on length
    sys.exit(43)

try:
    i = int(sys.stdin.readline())
except:
    # k is not an integer
    sys.exit(43)

for _ in range(i):
    try:
        j = sys.stdin.readline()
    except:
        # k too small
        sys.exit(43)

    if len(j.split()) != 3:
        # error in our test data
        sys.exit(43)
     

try:
    k = sys.stdin.readline().split()
except:
    sys.exit(43)

if len(k) != 1:
    # there is more than one goal
    sys.exit(43)

    
# everything seems okay!
sys.exit(42)
